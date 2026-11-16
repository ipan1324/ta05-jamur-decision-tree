"""Kamus label (Indonesia) untuk fitur dataset Mushroom (UCI).
Dipakai bersama oleh notebook analisis dan aplikasi Flask."""

KELAS = {"e": "Bisa dimakan", "p": "Beracun"}

_WARNA_TUDUNG = {"n": "Cokelat", "b": "Krem (buff)", "c": "Kayu manis", "g": "Abu-abu", "r": "Hijau",
                 "p": "Merah muda", "u": "Ungu", "e": "Merah", "w": "Putih", "y": "Kuning"}
_WARNA_INSANG = {"k": "Hitam", "n": "Cokelat", "b": "Krem (buff)", "h": "Cokelat tua", "g": "Abu-abu",
                 "r": "Hijau", "o": "Oranye", "p": "Merah muda", "u": "Ungu", "e": "Merah",
                 "w": "Putih", "y": "Kuning"}
_WARNA_BATANG = {"n": "Cokelat", "b": "Krem (buff)", "c": "Kayu manis", "g": "Abu-abu", "o": "Oranye",
                 "p": "Merah muda", "e": "Merah", "w": "Putih", "y": "Kuning"}
_PERMUKAAN_BATANG = {"f": "Berserat (fibrous)", "y": "Bersisik (scaly)", "k": "Seperti sutra (silky)", "s": "Halus (smooth)"}

# fitur -> (kelompok, judul, {kode: label})
FEATURES = {
    "cap-shape": ("Tudung jamur", "Bentuk tudung (cap-shape)",
                  {"b": "Lonceng (bell)", "c": "Kerucut (conical)", "x": "Cembung (convex)", "f": "Datar (flat)",
                   "k": "Berbenjol (knobbed)", "s": "Cekung (sunken)"}),
    "cap-surface": ("Tudung jamur", "Permukaan tudung (cap-surface)",
                    {"f": "Berserat (fibrous)", "g": "Beralur (grooves)", "y": "Bersisik (scaly)", "s": "Halus (smooth)"}),
    "cap-color": ("Tudung jamur", "Warna tudung (cap-color)", _WARNA_TUDUNG),
    "bruises": ("Bau & memar", "Memar (bruises)", {"t": "Memar saat disentuh", "f": "Tidak memar"}),
    "odor": ("Bau & memar", "Bau (odor)",
             {"a": "Almond", "l": "Adas manis (anise)", "c": "Kreosot", "y": "Amis", "f": "Busuk",
              "m": "Apek", "n": "Tidak berbau", "p": "Menyengat", "s": "Pedas (rempah)"}),
    "gill-attachment": ("Insang", "Pelekatan insang (gill-attachment)",
                        {"a": "Menempel (attached)", "d": "Menurun (descending)", "f": "Bebas (free)", "n": "Berlekuk (notched)"}),
    "gill-spacing": ("Insang", "Jarak insang (gill-spacing)",
                     {"c": "Rapat (close)", "w": "Sangat rapat (crowded)", "d": "Renggang (distant)"}),
    "gill-size": ("Insang", "Ukuran insang (gill-size)", {"b": "Lebar (broad)", "n": "Sempit (narrow)"}),
    "gill-color": ("Insang", "Warna insang (gill-color)", _WARNA_INSANG),
    "stalk-shape": ("Batang", "Bentuk batang (stalk-shape)", {"e": "Membesar (enlarging)", "t": "Meruncing (tapering)"}),
    "stalk-root": ("Batang", "Pangkal batang (stalk-root)",
                   {"b": "Membulat (bulbous)", "c": "Gada (club)", "u": "Cawan (cup)", "e": "Rata (equal)",
                    "z": "Rhizomorf", "r": "Berakar (rooted)", "?": "Tidak diketahui"}),
    "stalk-surface-above-ring": ("Batang", "Permukaan batang atas cincin (stalk-surface-above-ring)", _PERMUKAAN_BATANG),
    "stalk-surface-below-ring": ("Batang", "Permukaan batang bawah cincin (stalk-surface-below-ring)", _PERMUKAAN_BATANG),
    "stalk-color-above-ring": ("Batang", "Warna batang atas cincin (stalk-color-above-ring)", _WARNA_BATANG),
    "stalk-color-below-ring": ("Batang", "Warna batang bawah cincin (stalk-color-below-ring)", _WARNA_BATANG),
    "veil-type": ("Selubung & cincin", "Tipe selubung (veil-type)", {"p": "Sebagian (partial)", "u": "Menyeluruh (universal)"}),
    "veil-color": ("Selubung & cincin", "Warna selubung (veil-color)",
                   {"n": "Cokelat", "o": "Oranye", "w": "Putih", "y": "Kuning"}),
    "ring-number": ("Selubung & cincin", "Jumlah cincin (ring-number)", {"n": "Tidak ada", "o": "Satu", "t": "Dua"}),
    "ring-type": ("Selubung & cincin", "Tipe cincin (ring-type)",
                  {"c": "Sarang laba-laba (cobwebby)", "e": "Cepat hilang (evanescent)", "f": "Melebar (flaring)",
                   "l": "Besar (large)", "n": "Tidak ada", "p": "Menggantung (pendant)",
                   "s": "Berselubung (sheathing)", "z": "Zona (zone)"}),
    "spore-print-color": ("Lingkungan", "Warna cetakan spora (spore-print-color)",
                          {"k": "Hitam", "n": "Cokelat", "b": "Krem (buff)", "h": "Cokelat tua", "r": "Hijau",
                           "o": "Oranye", "u": "Ungu", "w": "Putih", "y": "Kuning"}),
    "population": ("Lingkungan", "Populasi (population)",
                   {"a": "Melimpah (abundant)", "c": "Mengelompok (clustered)", "n": "Banyak (numerous)",
                    "s": "Tersebar (scattered)", "v": "Beberapa (several)", "y": "Soliter (solitary)"}),
    "habitat": ("Lingkungan", "Habitat (habitat)",
                {"g": "Rumput (grasses)", "l": "Daun (leaves)", "m": "Padang rumput (meadows)", "p": "Jalan setapak (paths)",
                 "u": "Perkotaan (urban)", "w": "Lahan terlantar (waste)", "d": "Hutan (woods)"}),
}

# veil-type hanya punya 1 nilai unik (p), jadi tidak dipakai sebagai fitur model/formulir
FITUR_MODEL = [f for f in FEATURES if f != "veil-type"]
URUTAN_KELOMPOK = ["Tudung jamur", "Bau & memar", "Insang", "Batang", "Selubung & cincin", "Lingkungan"]


def short(label):
    """'Lonceng (bell)' -> 'Lonceng'"""
    return label.split(" (")[0]


def judul_pendek(fitur):
    """'Bau (odor)' -> 'Bau'"""
    return short(FEATURES[fitur][1])


def pisah_ohe(nama_kolom):
    """'odor_n' -> ('odor', 'n'). Nama fitur dataset memakai tanda '-', bukan '_', sehingga aman."""
    fitur, kode = nama_kolom.rsplit("_", 1)
    return fitur, kode


def jelaskan_kondisi(nama_kolom, benar):
    """Terjemahkan satu pemisahan pohon pada kolom one-hot menjadi kalimat.
    benar=True  -> kolom bernilai 1 (kategori itu ada)  -> 'Bau = Tidak berbau'
    benar=False -> kolom bernilai 0                     -> 'Bau ≠ Tidak berbau'"""
    fitur, kode = pisah_ohe(nama_kolom)
    label = short(FEATURES[fitur][2][kode])
    return f"{judul_pendek(fitur)} {'=' if benar else '≠'} {label}"
