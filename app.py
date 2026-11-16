"""Aplikasi Flask: klasifikasi jamur beracun / bisa dimakan dengan Decision Tree.

Model (Pipeline: imputasi -> one-hot -> DecisionTreeClassifier) dimuat dari folder model/.
Model bisa diganti tanpa mengubah kode dengan variabel lingkungan MODEL_FILE, contoh:
    MODEL_FILE=jamur_dt_model_b.joblib python app.py
"""
import json
import os
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

from labels import FEATURES, FITUR_MODEL, KELAS, URUTAN_KELOMPOK, jelaskan_kondisi, judul_pendek

BASE_DIR = Path(__file__).resolve().parent
MODEL_FILE = os.environ.get("MODEL_FILE", "jamur_dt_model_a.joblib")
NAMA_MODEL = {"jamur_dt_model_a.joblib": "Model A (pohon tanpa batas)",
              "jamur_dt_model_b.joblib": "Model B (pruned, max_depth=4)"}

app = Flask(__name__)
model = joblib.load(BASE_DIR / "model" / MODEL_FILE)
contoh = json.loads((BASE_DIR / "model" / "contoh_input.json").read_text(encoding="utf-8"))
metrik = json.loads((BASE_DIR / "model" / "metrik.json").read_text(encoding="utf-8"))

# Kelompokkan fitur untuk tampilan formulir: [(nama kelompok, [(fitur, judul, [(kode, label), ...]), ...]), ...]
KELOMPOK_FORM = []
for grup in URUTAN_KELOMPOK:
    isi = [(f, FEATURES[f][1], list(FEATURES[f][2].items())) for f in FITUR_MODEL if FEATURES[f][0] == grup]
    if isi:
        KELOMPOK_FORM.append((grup, isi))


def validasi(data):
    """Pastikan semua fitur terisi dengan kode yang dikenal. Mengembalikan (baris, daftar_error)."""
    baris, error = {}, []
    for f in FITUR_MODEL:
        nilai = (data.get(f) or "").strip()
        if not nilai:
            error.append(f"{judul_pendek(f)} belum dipilih.")
        elif nilai not in FEATURES[f][2]:
            error.append(f"Nilai '{nilai}' tidak dikenal untuk {judul_pendek(f)}.")
        else:
            baris[f] = nilai
    return baris, error


def prediksi(baris):
    """Prediksi satu jamur beserta jalur keputusan yang dilalui pohon."""
    X = pd.DataFrame([baris], columns=FITUR_MODEL)
    pra, pohon = model.named_steps["pra"], model.named_steps["pohon"]
    proba = model.predict_proba(X)[0]
    kelas = int(model.predict(X)[0])

    Xt = pra.transform(X)
    nama_kolom = pra.get_feature_names_out()
    t = pohon.tree_
    jalur, daun = [], None
    for node in pohon.decision_path(Xt).indices:
        if t.children_left[node] == t.children_right[node]:
            daun = node
            continue
        kolom = t.feature[node]
        jalur.append(jelaskan_kondisi(nama_kolom[kolom], Xt[0, kolom] > 0.5))

    diimputasi = baris.get("stalk-root") == "?"
    return {
        "kelas": "p" if kelas == 1 else "e",
        "label": KELAS["p" if kelas == 1 else "e"],
        "peluang_beracun": float(proba[1]),
        "peluang_aman": float(proba[0]),
        "keyakinan": float(proba.max()),
        "jalur": jalur,
        "sampel_daun": int(t.n_node_samples[daun]),
        "stalk_root_diimputasi": diimputasi,
    }


@app.get("/")
def index():
    return render_template("index.html", kelompok=KELOMPOK_FORM, contoh=contoh, nilai={}, hasil=None, error=[],
                           nama_model=NAMA_MODEL.get(MODEL_FILE, MODEL_FILE), metrik=metrik)


@app.post("/predict")
def predict():
    baris, error = validasi(request.form)
    hasil = None if error else prediksi(baris)
    return render_template("index.html", kelompok=KELOMPOK_FORM, contoh=contoh, nilai=request.form, hasil=hasil,
                           error=error, nama_model=NAMA_MODEL.get(MODEL_FILE, MODEL_FILE), metrik=metrik)


@app.post("/api/predict")
def api_predict():
    """Endpoint JSON, mis. untuk pengujian: kirim objek {fitur: kode} dan terima hasil prediksi."""
    baris, error = validasi(request.get_json(silent=True) or {})
    if error:
        return jsonify({"error": error}), 400
    return jsonify(prediksi(baris))


@app.get("/health")
def health():
    return jsonify({"status": "ok", "model": MODEL_FILE})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
