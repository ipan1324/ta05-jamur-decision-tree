# TA-05: Klasifikasi Jamur Beracun dan Bisa Dimakan dengan Decision Tree

Tugas Akhir 05 mata praktikum **Pembelajaran Mesin** (Modul 05: Algoritma Decision Tree).
Aplikasi web Flask yang mengklasifikasikan jamur sebagai *beracun* atau *bisa dimakan* dari 21 ciri fisiknya,
lengkap dengan **jalur keputusan pohon** yang menjelaskan alasan prediksi.

> Hanya untuk keperluan belajar. Jangan jadikan hasil model ini dasar memutuskan apakah jamur aman dimakan.

## Isi repositori

```
.
├── app.py                      # Aplikasi Flask (halaman formulir, /predict, /api/predict, /health)
├── labels.py                   # Kamus label Indonesia untuk fitur dan kategori
├── templates/index.html        # Antarmuka (Bootstrap 5, tema gelap)
├── static/                     # Bootstrap CSS lokal (aplikasi tidak butuh CDN)
├── data/mushrooms.csv          # Dataset UCI Mushroom (8.124 baris)
├── notebook/TA05_Decision_Tree_Jamur.ipynb   # Analisis lengkap (sudah dijalankan, output tersimpan)
├── model/
│   ├── jamur_dt_model_a.joblib # Model A: pohon tanpa batas (dipakai aplikasi)
│   ├── jamur_dt_model_b.joblib # Model B: pruned, max_depth=4
│   ├── metrik.json             # Ringkasan metrik dan aturan jika-maka
│   └── contoh_input.json       # Contoh input untuk tombol contoh di aplikasi
├── figures/                    # Semua grafik hasil notebook dan tangkapan layar aplikasi
├── requirements.txt  Procfile  .python-version
```

## Menjalankan secara lokal

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell;  Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py                   # buka http://localhost:5000
```

Versi `scikit-learn` pada `requirements.txt` sengaja dikunci (1.9.1) karena file `.joblib` dibuat dengan versi tersebut.
Jika memakai versi lain, jalankan ulang notebook agar model dilatih dan disimpan ulang.

Mengganti model yang dipakai aplikasi (tanpa mengubah kode):

```powershell
$env:MODEL_FILE="jamur_dt_model_b.joblib"; python app.py
```

Menjalankan notebook: `pip install jupyter` lalu `jupyter notebook notebook/TA05_Decision_Tree_Jamur.ipynb`.

## Deploy

**Railway:** push repositori ke GitHub, buat project baru dari repo tersebut. Railway membaca `requirements.txt` dan `Procfile`
(`gunicorn app:app`). Setelah build selesai, buat domain publik di tab *Settings > Networking*.

**Render:** *New > Web Service*, hubungkan repo, `Build Command: pip install -r requirements.txt`,
`Start Command: gunicorn app:app`.

Cek `https://<domain-anda>/health`; jawabannya harus `{"status":"ok", ...}`.

## Hasil ringkas

| | Model A (tanpa batas) | Model B (max_depth=4) |
|---|---|---|
| Kedalaman / jumlah daun | 6 / 13 | 4 / 11 |
| Akurasi latih | 100% | 99,98% |
| Akurasi uji | 100% | 99,88% |
| Akurasi CV 5-fold | 100% | 99,85% |
| Jamur beracun diprediksi aman (FN) | 0 | 3 |

Pada dataset ini Model A **tidak overfit**: pola jamur sangat terpisah sehingga pohon yang tumbuh bebas pun hanya sedalam 6 tingkat dan
tetap sempurna di data uji. Penjelasan lengkap ada di notebook dan laporan.

## API singkat

Kirim satu objek berisi 21 fitur (kode huruf dataset). Contoh jamur beracun:

```bash
curl -X POST http://localhost:5000/api/predict -H "Content-Type: application/json" \
     -d '{"cap-shape": "x", "cap-surface": "f", "cap-color": "y", "bruises": "f", "odor": "f", "gill-attachment": "f", "gill-spacing": "c", "gill-size": "b", "gill-color": "g", "stalk-shape": "e", "stalk-root": "b", "stalk-surface-above-ring": "k", "stalk-surface-below-ring": "k", "stalk-color-above-ring": "n", "stalk-color-below-ring": "n", "veil-color": "w", "ring-number": "o", "ring-type": "l", "spore-print-color": "h", "population": "y", "habitat": "d"}'
```

Respons berisi `label`, `peluang_beracun`, `peluang_aman`, `jalur` (aturan yang dilalui pohon), dan `sampel_daun`.
Kode kategori yang valid untuk tiap fitur ada di `labels.py`.
