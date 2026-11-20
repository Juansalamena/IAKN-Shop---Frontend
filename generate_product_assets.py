import os
import math
from PIL import Image, ImageDraw, ImageFont

output_dir = "assets/images/produk"
os.makedirs(output_dir, exist_ok=True)

# Try loading font
def get_font(size, bold=False):
    names = ['segoeuib.ttf', 'arialbd.ttf'] if bold else ['segoeui.ttf', 'arial.ttf']
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            pass
    try:
        return ImageFont.load_default()
    except Exception:
        return None

f_tag = get_font(18, bold=True)
f_title = get_font(28, bold=True)
f_subtitle = get_font(20, bold=False)
f_badge = get_font(16, bold=True)
f_desc = get_font(22, bold=False)
f_meta = get_font(18, bold=True)
f_huge = get_font(80, bold=True)

products_data = [
    {
        "id": "prod_1",
        "tag": "Buku Ilmiah",
        "title": "Antropologi Musik Maluku & Nusantara",
        "author": "Prodi Musik Gereja IAKN",
        "category": "Buku/Ilmiah",
        "price": "Rp 85.000",
        "rating": "4.9 (120 Ulasan)",
        "theme_color": (30, 58, 138),     # Navy blue
        "accent_color": (59, 130, 246),
        "video_duration": "0:35",
        "video_title": "Video Bedah Buku Antropologi Musik Maluku",
        "slides": [
            ("Foto 1/7: Tampak Depan", "Sampul Buku Resmi Berlatar Etnik & Logo IAKN", "Buku referensi etnomusikologi terlengkap karya civitas akademika."),
            ("Foto 2/7: Sudut & Punggung", "Ketebalan Buku (Spine) & Jilid Jahit Benang Kuat", "Kualitas penjilidan standar perpustakaan internasional tahan lama."),
            ("Foto 3/7: Daftar Isi", "Struktur Bab Etnomusikologi & Analisis Budaya", "Memuat kajian komprehensif nyanyian liturgi & instrumen tradisional."),
            ("Foto 4/7: Halaman Isi", "Transkripsi Partitur Musik & Dokumentasi Etnik", "Dilengkapi notasi angka, balok, dan arsip foto langka alat musik Maluku."),
            ("Foto 5/7: Spesifikasi Fisik", "280 Halaman • Kertas Bookpaper 72gr • Ukuran B5", "Format nyaman dibaca, ramah mata, dan ber-ISBN resmi nasional."),
            ("Foto 6/7: Pemakaian Nyata", "Buku Referensi Perpustakaan & Kuliah Kampus", "Digunakan sebagai modul inti perkuliahan Prodi Musik Gereja IAKN."),
            ("Foto 7/7: Sertifikat Resmi", "Segel Orisinalitas UPT Penerbitan IAKN Ambon", "Produk dijamin 100% asli terbitan resmi kampus IAKN Ambon.")
        ]
    },
    {
        "id": "prod_2",
        "tag": "Jasa Grafis",
        "title": "Desain Banner & Publikasi Acara Kampus",
        "author": "Kreatif Lab Mahasiswa",
        "category": "Desain Grafis",
        "price": "Rp 50.000",
        "rating": "4.8 (85 Ulasan)",
        "theme_color": (88, 28, 135),     # Deep purple
        "accent_color": (168, 85, 247),
        "video_duration": "0:28",
        "video_title": "Video Portofolio Desain & Proses Kreatif",
        "slides": [
            ("Foto 1/7: Banner Horizontal", "Desain Banner Panggung Utama 3x1 Meter", "Komposisi visual modern dengan ketajaman warna cetak tingkat tinggi."),
            ("Foto 2/7: Standing Banner", "Desain X-Banner / Roll Up Vertikal Seminar", "Format proporsional untuk dekorasi auditorium, aula, dan booth expo."),
            ("Foto 3/7: Palet & Tipografi", "Harmonisasi Warna Profesional & Grid Layout", "Tipografi terkurasi yang mudah dibaca dari kejauhan dengan estetika rapi."),
            ("Foto 4/7: Format File Lengkap", "File Master AI, PSD, PDF Print Ready, PNG & JPG", "Bebas pilih resolusi cetak tanpa khawatir pecah atau buram."),
            ("Foto 5/7: Alur Kerja Cepat", "Pengerjaan Kilat 24 Jam & Revisi Tanpa Batas", "Garansi kepuasan desain hingga siap cetak untuk acara kampus Anda."),
            ("Foto 6/7: Dokumentasi Acara", "Simulasi Banner Terpasang di Auditorium IAKN", "Telah dipercaya oleh puluhan panitia seminar & Dies Natalis kampus."),
            ("Foto 7/7: Garansi Mutu", "Sertifikasi Layanan Kreatif Lab IAKN Ambon", "Layanan jasa resmi binaan inkubator bisnis kreatif mahasiswa IAKN.")
        ]
    },
    {
        "id": "prod_3",
        "tag": "Alat Musik",
        "title": "Tifa Maluku Kayu Ukir Asli",
        "author": "Bengkel Seni Kampus",
        "category": "Alat Musik",
        "price": "Rp 350.000",
        "rating": "5.0 (25 Ulasan)",
        "theme_color": (124, 45, 18),     # Terracotta / mahogany
        "accent_color": (234, 88, 12),
        "video_duration": "0:42",
        "video_title": "Video Uji Suara & Dentuman Akustik Tifa",
        "slides": [
            ("Foto 1/7: Tampilan Utama", "Tifa Tradisional Kayu Lenggua Utuh Berdiri", "Dibuat langsung tangan pengrajin seni kriya kampus IAKN Ambon."),
            ("Foto 2/7: Detail Pahat Ukir", "Ornamen Etnik Filosofis Khas Kepulauan Maluku", "Pahatan manual mendalam bernilai artistik tinggi dengan vernis alami."),
            ("Foto 3/7: Membran Alami", "Selaput Kulit Pilihan & Tali Anyaman Rotan", "Menghasilkan dentuman bass mantap dan resonansi suara akustik merdu."),
            ("Foto 4/7: Dimensi Fisik", "Tinggi 65 cm • Diameter 22 cm • Berat 3.2 kg", "Ukuran ideal untuk pagelaran musik gerejawi dan pementasan adat."),
            ("Foto 5/7: Rongga Resonansi", "Konstruksi Bawah Kokoh & Rongga Udara Presisi", "Bagian dalam kayu dikeruk halus untuk pantulan suara maksimal."),
            ("Foto 6/7: Pertunjukan Seni", "Dipakai dalam Ansambel Musik Etnik IAKN", "Instrumen panggung andalan sanggar musik etnomusikologi IAKN Ambon."),
            ("Foto 7/7: Sertifikat Otentik", "Cap Keaslian Kriya Bengkel Seni IAKN Ambon", "Jaminan keaslian bahan kayu lenggua solid asli dari tanah Maluku.")
        ]
    },
    {
        "id": "prod_4",
        "tag": "Tek. Edukasi",
        "title": "Media Belajar Interaktif PAUD Kristen",
        "author": "Laboratorium FKIP IAKN",
        "category": "Tek. Edukasi",
        "price": "Rp 125.000",
        "rating": "4.9 (42 Ulasan)",
        "theme_color": (3, 105, 161),     # Sky blue / cyan
        "accent_color": (14, 165, 233),
        "video_duration": "0:30",
        "video_title": "Video Cuplikan Game & Animasi Edukatif PAUD",
        "slides": [
            ("Foto 1/7: Antarmuka Aplikasi", "Menu Utama Interaktif Beranimasi Ramah Anak", "Navigasi tombol besar, ramah sentuhan tablet dan suara pemandu ceria."),
            ("Foto 2/7: Modul Alkitab Bergambar", "Cerita Tokoh Alkitab Dilengkapi Audio Dubbing", "Animasi interaktif dengan ilustrasi penuh warna yang disukai balita."),
            ("Foto 3/7: Fitur Kuis & Nyanyian", "Game Edukasi Tebak Gambar & Karaoke Lagu Rohani", "Melatih kognitif, motorik, dan musikal anak sejak usia dini."),
            ("Foto 4/7: Dashboard Guru", "Modul Lembar Evaluasi & Panduan Kurikulum PAUD", "Memudahkan guru mengukur pemahaman belajar anak secara terstruktur."),
            ("Foto 5/7: Spesifikasi Sistem", "Kompatibel Tablet Android, Windows PC & Web", "Instalasi praktis, ukuran file ringan, dan bisa dimainkan offline."),
            ("Foto 6/7: Uji Coba Lapangan", "Siswa PAUD Bahagia Belajar Interaktif di Kelas", "Telah diuji klinis di sekolah laboratorium PAUD percontohan IAKN."),
            ("Foto 7/7: Lisensi Resmi", "Sertifikat Hak Cipta & Lisensi Edukasi FKIP", "Aman untuk anak, tanpa iklan dan terdaftar di UPT FKIP IAKN Ambon.")
        ]
    },
    {
        "id": "prod_5",
        "tag": "Karya Dosen",
        "title": "Buku Teologi Kontekstual & Budaya Maluku",
        "author": "Penulis: Dosen IAKN",
        "category": "Buku/Ilmiah",
        "price": "Rp 95.000",
        "rating": "5.0 (82 Ulasan)",
        "theme_color": (120, 53, 15),     # Rich amber
        "accent_color": (245, 158, 11),
        "video_duration": "0:45",
        "video_title": "Video Ulasan Akademis bersama Dosen Penulis",
        "slides": [
            ("Foto 1/7: Sampul Eksklusif", "Cover Edisi Emas Teologi Kontekstual Maluku", "Karya magnum opus dialog keimanan dan kearifan lokal nusantara."),
            ("Foto 2/7: Jilid Hardcover", "Ketebalan Hardcover Eksklusif dengan Pita Sutra", "Kualitas cetakan mewah cocok untuk koleksi akademisi dan perpustakaan."),
            ("Foto 3/7: Kata Sambutan Rektor", "Apresiasi Pimpinan Kampus & Sinopsis Lengkap", "Dilengkapi testimoni para pakar sosiologi agama dan budaya Maluku."),
            ("Foto 4/7: Pembahasan Inti", "Kajian Filosofis 'Pela Gandong' dalam Teologi", "Analisis mendalam nilai persaudaraan sejati lintas komunitas adat."),
            ("Foto 5/7: Spesifikasi Literatur", "Hardcover • 340 Halaman • Kertas Imperial", "Kertas bookpaper anti-silau berkualitas tinggi standar monograf ilmiah."),
            ("Foto 6/7: Di Meja Akademisi", "Rujukan Wajib Mahasiswa Sarjana & Magister", "Menjadi teks panduan utama pada mata kuliah Teologi Kontekstual."),
            ("Foto 7/7: Tanda Tangan Penulis", "Dilengkapi Tanda Tangan Asli Dosen & Cap Barcode", "Setiap buku diverifikasi langsung dengan cap orisinalitas kampus.")
        ]
    },
    {
        "id": "prod_6",
        "tag": "Flash Sale",
        "title": "Hoodie Dies Natalis IAKN Ke-25",
        "author": "Koperasi Mahasiswa IAKN",
        "category": "Merchandise",
        "price": "Rp 99.000",
        "rating": "4.9 (165 Ulasan)",
        "theme_color": (30, 64, 175),     # Royal Navy
        "accent_color": (96, 165, 250),
        "video_duration": "0:25",
        "video_title": "Video Try-On & Uji Kualitas Bahan Hoodie",
        "slides": [
            ("Foto 1/8: Tampilan Depan", "Hoodie Navy Edisi Khusus Dies Natalis Ke-25", "Desain elegan berhias bordir logo perak & emas resmi IAKN Ambon."),
            ("Foto 2/8: Tampilan Belakang", "Artwork Tipografi 'Excellence in Diversity'", "Sentuhan seni grafis kontemporer kebanggaan almamater kampus."),
            ("Foto 3/8: Detail Bahan Kain", "Cotton Fleece Premium 330 Gsm Super Tebal", "Sangat lembut di kulit, hangat di malam hari, dan menyerap keringat."),
            ("Foto 4/8: Tali & Resleting", "Tali Tudung Logam Metalik & Jahitan Rantai Dobel", "Aksesori logam anti-karat dengan kualitas jahitan distro kelas atas."),
            ("Foto 5/8: Panduan Ukuran", "Size Chart Lengkap (S, M, L, XL, XXL, 3XL)", "Potongan regular-fit nyaman untuk pria maupun wanita (unisex)."),
            ("Foto 6/8: Model Pemakaian", "Foto Mahasiswa Bergaya Kasual di Kampus", "Tampil percaya diri, modis, dan penuh rasa bangga terhadap almamater."),
            ("Foto 7/8: Paket Kemasan", "Ziplock Bag Tebal + Bonus 3 Stiker Dies Natalis", "Kemasan rapi dan higienis siap pakai atau dikirim ke luar daerah."),
            ("Foto 8/8: Woven Label Asli", "Label Tenun Resmi Koperasi Mahasiswa IAKN", "Jaminan produk merchandise 100% orisinal diproduksi resmi Kopma.")
        ]
    },
    {
        "id": "prod_7",
        "tag": "Flash Sale",
        "title": "Tumbler Grafir Logo Edisi Ambon",
        "author": "Koperasi Mahasiswa",
        "category": "Merchandise",
        "price": "Rp 45.000",
        "rating": "4.8 (90 Ulasan)",
        "theme_color": (14, 116, 144),    # Teal / Cyan
        "accent_color": (6, 182, 212),
        "video_duration": "0:20",
        "video_title": "Video Uji Ketahanan Suhu & Anti Bocor Tumbler",
        "slides": [
            ("Foto 1/7: Tampilan Utama", "Tumbler Vacuum Flask Stainless Steel Matte Finish", "Warna elegan hitam doff dan biru toska dengan ukiran laser presisi."),
            ("Foto 2/7: Tutup Anti Tumpah", "Karet Silikon Seal 100% Leak-Proof & Kunci Klik", "Aman dimasukkan ke dalam ransel tanpa khawatir bocor atau tumpah."),
            ("Foto 3/7: Ketajaman Grafir", "Ukiran Laser Logo IAKN & Motif Teluk Ambon", "Grafir permanen anti gores, tidak akan luntur meski dicuci berkali-kali."),
            ("Foto 4/7: Uji Isolasi Panas/Dingin", "Tahan Dingin 24 Jam & Panas 12 Jam (SUS 304)", "Teknologi insulasi vakum ganda menjaga suhu minuman tetap segar."),
            ("Foto 5/7: Dimensi Ergonomis", "Kapasitas 500 ml • Tinggi 22.5 cm • Bobot Ringan", "Pas di cup holder mobil dan nyaman digenggam sepanjang hari."),
            ("Foto 6/7: Teman Aktivitas", "Bawa Kopi Hangat ke Kelas atau Air Dingin Olahraga", "Mendukung gerakan kampus hijau ramah lingkungan bebas sampah plastik."),
            ("Foto 7/7: Kemasan Gift Box", "Kotak Silinder Karton Daur Ulang Elegan", "Sangat cantik untuk hadiah wisuda, suvenir seminar atau kado sahabat.")
        ]
    },
    {
        "id": "prod_8",
        "tag": "Kriya Seni",
        "title": "Miniatur Tifa Khas Maluku Orisinal",
        "author": "Sanggar Seni & Kriya Kampus",
        "category": "Alat Musik",
        "price": "Rp 50.000",
        "rating": "4.9 (50 Ulasan)",
        "theme_color": (109, 40, 217),    # Purple / bronze
        "accent_color": (147, 51, 234),
        "video_duration": "0:22",
        "video_title": "Video 360 Derajat Rotasi Miniatur Tifa",
        "slides": [
            ("Foto 1/7: Tampilan Miniatur", "Miniatur Tifa Kayu Ukir 20 cm Finishing Mengkilap", "Karya miniatur presisi tinggi buatan mahasiswa kriya seni IAKN."),
            ("Foto 2/7: Sudut Ukiran Khas", "Detail Pahat Ornamen Tradisional Maluku Manual", "Tiap lekukan diukir dengan ketelitian tinggi mencerminkan seni etnik."),
            ("Foto 3/7: Detail Atas Membran", "Kulit Sintetis Rapi & Anyaman Benang Tifa", "Menyerupai tifa ukuran asli dengan perbandingan skala yang presisi."),
            ("Foto 4/7: Perbandingan Ukuran", "Pas di Telapak Tangan & Indah di Meja Kerja", "Ukuran kompak yang manis untuk dekorasi meja resepsionis atau lemari kaca."),
            ("Foto 5/7: Bahan Kayu Alami", "Kayu Mahoni Solid • Berat 250gr • Tahan Rayap", "Dilapisi pelindung vernis bening agar kilap kayu awet bertahun-tahun."),
            ("Foto 6/7: Suvenir Wisuda", "Cenderamata Eksklusif Tamu & Wisudawan Kampus", "Paling diminati pengunjung sebagai oleh-oleh khas kampus IAKN Ambon."),
            ("Foto 7/7: Kemasan Mika Mewah", "Box Mika Beralas Beludru Merah & Pita Emas", "Siap langsung dipajang atau diberikan sebagai bingkisan kenang-kenangan.")
        ]
    },
    {
        "id": "prod_9",
        "tag": "Layanan Kilat",
        "title": "Jasa Translate Naskah Ilmiah & Abstrak",
        "author": "Unit Bahasa Kampus",
        "category": "Jasa/Layanan",
        "price": "Rp 35.000",
        "rating": "4.9 (64 Ulasan)",
        "theme_color": (112, 26, 117),    # Fuchsia / purple
        "accent_color": (192, 38, 211),
        "video_duration": "0:32",
        "video_title": "Video Prosedur & Standar Mutu Terjemahan Naskah",
        "slides": [
            ("Foto 1/7: Layanan Resmi", "Penerjemahan Dokumen Akademik Indonesia - Inggris", "Dikelola langsung oleh tim dosen bahasa & sworn translator bersertifikat."),
            ("Foto 2/7: Perbandingan Teks", "Before - After: Kalimat Natural Berstandar Jurnal", "Mengubah naskah kaku menjadi bahasa Inggris akademis yang luwes & tepat."),
            ("Foto 3/7: Sertifikat Penerjemah", "Tim Ahli Bahasa Bersertifikat Kompetensi Resmi", "Menjamin kualitas terminologi keilmuan sesuai bidang studi naskah."),
            ("Foto 4/7: Alur Proses Mudah", "Kirim Dokumen -> Penerjemahan -> Proofreading -> Selesai", "Layanan ramah dan konsultasi langsung dengan penerjemah terkait materi."),
            ("Foto 5/7: Standar Kualitas Tinggi", "Skor Grammar 98+ • Turnitin Aman • Format APA/IEEE", "Bebas dari kesalahan tata bahasa dan typo sebelum naskah diserahkan."),
            ("Foto 6/7: Testimoni Sukses", "Ratusan Abstrak Skripsi & Paper Tembus Jurnal Scopus", "Banyak mahasiswa dan dosen terbantu meraih kelulusan & publikasi."),
            ("Foto 7/7: Surat Keterangan Resmi", "Lembar Pengesahan Terjemahan Berstempel Basah", "Dapat dilampirkan resmi pada dokumen ujian skripsi, tesis atau jurnal.")
        ]
    },
    {
        "id": "prod_10",
        "tag": "Merchandise BEM",
        "title": "Totebag Kanvas Motif Tenun Maluku",
        "author": "BEM IAKN Ambon",
        "category": "Merchandise",
        "price": "Rp 45.000",
        "rating": "4.7 (53 Ulasan)",
        "theme_color": (159, 18, 57),     # Crimson / ruby
        "accent_color": (244, 63, 94),
        "video_duration": "0:26",
        "video_title": "Video Uji Kapasitas & Ketahanan Muatan Totebag",
        "slides": [
            ("Foto 1/7: Tampilan Utama", "Totebag Kanvas Broken White Motif Tenun Tradisional", "Perpaduan anggun nuansa etnik khas Maluku dengan tren gaya urban."),
            ("Foto 2/7: Kapasitas Kompartemen", "Muat Laptop 14 Inch, Buku Tebal, Binder & Botol", "Ruang utama luas dengan alas lebar 8 cm menampung perlengkapan kuliah."),
            ("Foto 3/7: Kualitas Bahan Kanvas", "Kanvas Tebal 12 Oz & Jahitan Rantai Dobel", "Kain kuat anti robek dengan tekstur kanvas alami yang tebal dan kokoh."),
            ("Foto 4/7: Ritsleting & Saku Dalam", "Zipper Utama Besi + Kantong Rahasia Berresleting", "Aman menyimpan handphone, kunci motor, kartu identitas, dan dompet."),
            ("Foto 5/7: Dimensi Produk", "Panjang 38 cm • Tinggi 40 cm • Tali Bahu 60 cm", "Panjang tali pas disampirkan di bahu, tidak mudah melorot saat berjalan."),
            ("Foto 6/7: Gaya Mahasiswa", "Foto Mahasiswi Beraktivitas Santai di Kampus", "Aksesori harian stylish yang serasi dipadukan dengan berbagai outfit kuliah."),
            ("Foto 7/7: Hangtag Resmi BEM", "Kemasan Cassava Bag Ramah Lingkungan & Hangtag", "Setiap pembelian mendukung dana kegiatan kemahasiswaan BEM IAKN.")
        ]
    },
    {
        "id": "prod_11",
        "tag": "Karya Mahasiswa",
        "title": "Gitar Akustik Custom Mahasiswa",
        "author": "Prodi Pendidikan Seni",
        "category": "Alat Musik",
        "price": "Rp 750.000",
        "rating": "4.8 (19 Ulasan)",
        "theme_color": (21, 128, 61),     # Emerald green
        "accent_color": (34, 197, 94),
        "video_duration": "0:48",
        "video_title": "Video Soundcheck Akustik & Petikan Melodi Gitar",
        "slides": [
            ("Foto 1/8: Tampak Depan", "Gitar Akustik Solid Top Spruce Finishing Doff Satin", "Desain bodi Dreadnought 41 inch menghasilkan volume akustik bertenaga."),
            ("Foto 2/8: Tampak Belakang", "Kayu Mahogany Eksotis Berpola Serat Alami Indah", "Resonansi nada bass warm dan artikulasi treble kristal yang seimbang."),
            ("Foto 3/8: Headstock & Dryers", "Headstock Ukir Logo IAKN & Dryer Chrome Presisi", "Tuning stabil, putaran mulus dan tidak mudah fals saat dimainkan lama."),
            ("Foto 4/8: Fretboard & Inlay", "Kayu Rosewood Halus dengan Inlay Kerang Mutiara", "Fret baja dipoles rata tanpa sudut tajam, nyaman untuk fingerstyle."),
            ("Foto 5/8: Rosette Etnik", "Ornamen Pahat Nusantara Mengelilingi Soundhole", "Sentuhan seni etnik nusantara yang membedakannya dari gitar pabrikan umum."),
            ("Foto 6/8: Spesifikasi Akustik", "Dual Action Truss Rod • Senar D'Addario Bronze 0.11", "Ketinggian senar (action) disetel rendah dan empuk, tanpa buzzing."),
            ("Foto 7/8: Pentas Musik", "Dimainkan Mahasiswa pada Konser Musik Kampus", "Instrumen andalan pertunjukan musik gerejawi dan akustik kampus IAKN."),
            ("Foto 8/8: Paket Bonus Lengkap", "Softcase Tebal, Capo Alloy, 3 Pick & Strap Tenun", "Paket lengkap siap pentas langsung dari bengkel instrumen IAKN.")
        ]
    },
    {
        "id": "prod_12",
        "tag": "Lisensi Edu",
        "title": "Software Pembelajaran Liturgi Digital",
        "author": "Lab Komputer IAKN",
        "category": "Tek. Edukasi",
        "price": "Rp 150.000",
        "rating": "4.9 (31 Ulasan)",
        "theme_color": (15, 118, 110),    # Teal
        "accent_color": (20, 184, 166),
        "video_duration": "0:40",
        "video_title": "Video Demo Navigasi & Fitur Partitur Digital",
        "slides": [
            ("Foto 1/7: Tampilan Utama", "Dashboard Modern & Tata Letak Intuitif", "Aplikasi media ajar liturgi digital terlengkap berbasis teknologi kampus."),
            ("Foto 2/7: Modul Tata Ibadah", "Penyusun Urutan Liturgi Mingguan & Kalender Gereja", "Praktis menyusun tata ibadah hari minggu, natal, paskah dan perjamuan."),
            ("Foto 3/7: Bank Partitur Rohani", "Koleksi Ratusan Partitur Not Angka & Not Balok", "Dilengkapi pemutar instrumen piano/organ virtual untuk latihan jemaat."),
            ("Foto 4/7: Paduan Suara 4 Suara", "Fitur Split Audio Sopran, Alto, Tenor & Bass", "Memudahkan pelatih paduan suara melatih tiap kelompok suara secara mandiri."),
            ("Foto 5/7: Kompatibilitas Sistem", "Kompatibel Windows 10/11, macOS, Android & Web", "Aplikasi sangat ringan (RAM 2GB lancar), bebas lag dan hemat daya."),
            ("Foto 6/7: Praktik Laboratorium", "Mahasiswa Liturgi Berlatih di Lab Komputer IAKN", "Digunakan rutin dalam praktikum teknologi tata ibadah mahasiswa."),
            ("Foto 7/7: Sertifikat Lisensi", "Kartu Lisensi Permanen (Lifetime Key) & Panduan", "Lisensi resmi seumur hidup dengan update database lagu berkala.")
        ]
    }
]

print("Starting asset generation for 12 products...")

for prod in products_data:
    pid = prod["id"]
    theme = prod["theme_color"]
    accent = prod["accent_color"]
    
    # 1. Generate 7-8 images for this product
    for idx, (step_label, main_caption, desc_caption) in enumerate(prod["slides"]):
        img_num = idx + 1
        img_path = f"{output_dir}/{pid}_img{img_num}.jpg"
        
        img = Image.new("RGB", (800, 800), color=(248, 250, 252))
        draw = ImageDraw.Draw(img)
        
        # Soft gradient header band
        for y in range(130):
            factor = y / 130.0
            r = int(theme[0] * (1 - factor * 0.15))
            g = int(theme[1] * (1 - factor * 0.15))
            b = int(theme[2] * (1 - factor * 0.15))
            draw.line([(0, y), (800, y)], fill=(r, g, b))
            
        # Header Badge
        draw.rounded_rectangle([(30, 25), (200, 60)], radius=8, fill=(255, 255, 255, 230))
        draw.text((45, 32), "IAKN MALL", fill=theme, font=f_badge)
        
        draw.text((220, 32), f"•  {prod['category']}", fill=(220, 235, 255), font=f_badge)
        draw.text((30, 75), prod["title"], fill=(255, 255, 255), font=f_title)
        
        # Central Product Showcase Card
        draw.rounded_rectangle([(40, 150), (760, 620)], radius=20, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
        
        # Card Inner Header / View Tag
        draw.rounded_rectangle([(60, 170), (320, 215)], radius=12, fill=(accent[0], accent[1], accent[2]))
        draw.text((75, 178), step_label, fill=(255, 255, 255), font=f_badge)
        
        # Shopee-style camera photo icon & counter
        draw.text((630, 178), f"📷 {img_num}/{len(prod['slides'])}", fill=(100, 116, 139), font=f_meta)
        
        # Visual Center Graphics Box
        draw.rounded_rectangle([(80, 235), (720, 500)], radius=16, fill=(241, 245, 249), outline=(203, 213, 225), width=1)
        
        # Visual Accents inside showcase
        # Decorative circular watermark
        draw.ellipse([(260, 260), (540, 475)], outline=(accent[0], accent[1], accent[2]), width=3)
        draw.ellipse([(280, 280), (520, 455)], outline=(theme[0], theme[1], theme[2]), width=1)
        
        # Product Category Icon Text or Emblem
        cat_initials = prod["tag"][:2].upper()
        draw.text((360, 320), cat_initials, fill=(theme[0], theme[1], theme[2]), font=f_huge)
        
        # Seal banner
        draw.rounded_rectangle([(230, 450), (570, 485)], radius=8, fill=theme)
        draw.text((250, 458), "IAKN AMBON • OFFICIAL PRODUCT", fill=(255, 255, 255), font=f_badge)
        
        # Step Title inside card
        draw.text((80, 520), main_caption, fill=(15, 23, 42), font=f_title)
        draw.text((80, 565), desc_caption, fill=(71, 85, 105), font=f_desc)
        
        # Bottom Footer Bar (Shopee Info Bar)
        draw.rounded_rectangle([(40, 640), (760, 760)], radius=16, fill=theme)
        
        # Left Price & Rating
        draw.text((65, 660), prod["price"], fill=(254, 240, 138), font=f_title)
        draw.text((65, 710), f"★ {prod['rating']}  |  {prod['author']}", fill=(241, 245, 249), font=f_meta)
        
        # Right Guarantee Badges
        draw.rounded_rectangle([(550, 660), (735, 740)], radius=10, fill=(255, 255, 255, 40), outline=(255, 255, 255), width=1)
        draw.text((565, 675), "100% ORIGINAL", fill=(255, 255, 255), font=f_badge)
        draw.text((565, 705), "GARANSI KAMPUS", fill=(254, 240, 138), font=f_badge)
        
        # Save image
        img.save(img_path, "JPEG", quality=92)
        
    # 2. Generate 1 Video Thumbnail for this product
    v_thumb_path = f"{output_dir}/{pid}_video_thumb.jpg"
    v_img = Image.new("RGB", (800, 800), color=(15, 23, 42))
    v_draw = ImageDraw.Draw(v_img)
    
    # Outer gradient
    for y in range(800):
        factor = y / 800.0
        r = int(15 + (theme[0] - 15) * 0.4 * factor)
        g = int(23 + (theme[1] - 23) * 0.4 * factor)
        b = int(42 + (theme[2] - 42) * 0.4 * factor)
        v_draw.line([(0, y), (800, y)], fill=(r, g, b))
        
    # Video border card
    v_draw.rounded_rectangle([(30, 30), (770, 770)], radius=24, outline=(239, 68, 68), width=3)
    
    # Shopee Video Top Header
    v_draw.rounded_rectangle([(50, 50), (220, 95)], radius=10, fill=(239, 68, 68))
    v_draw.text((68, 60), "▶ VIDEO PRODUK", fill=(255, 255, 255), font=f_badge)
    
    # Duration badge top right
    v_draw.rounded_rectangle([(630, 50), (750, 95)], radius=10, fill=(0, 0, 0, 180), outline=(255, 255, 255), width=1)
    v_draw.text((650, 60), prod["video_duration"], fill=(255, 255, 255), font=f_badge)
    
    # Large Center Play Button
    center_x, center_y = 400, 370
    v_draw.ellipse([(center_x - 75, center_y - 75), (center_x + 75, center_y + 75)], fill=(239, 68, 68, 220), outline=(255, 255, 255), width=4)
    # Triangle Play
    triangle = [
        (center_x - 20, center_y - 35),
        (center_x + 40, center_y),
        (center_x - 20, center_y + 35)
    ]
    v_draw.polygon(triangle, fill=(255, 255, 255))
    
    # Text below play button
    v_draw.text((240, 480), "SENTUH UNTUK MEMUTAR VIDEO", fill=(255, 255, 255), font=f_meta)
    
    # Bottom Video Info Card
    v_draw.rounded_rectangle([(50, 550), (750, 740)], radius=16, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
    v_draw.text((75, 570), prod["video_title"], fill=(255, 255, 255), font=f_title)
    v_draw.text((75, 620), f"Produk: {prod['title']}", fill=(203, 213, 225), font=f_subtitle)
    v_draw.text((75, 665), f"Kualitas HD 1080p • Suara Jernih • Durasi {prod['video_duration']} • Ulasan {prod['author']}", fill=(148, 163, 184), font=f_desc)
    
    # Save video thumbnail
    v_img.save(v_thumb_path, "JPEG", quality=92)
    print(f"Generated {len(prod['slides'])} images + 1 video thumbnail for {pid}")

# Also ensure tifa_1..tifa_3 remain intact, and tifa_4..7 are also available for tifa
for i in range(1, 8):
    source = f"{output_dir}/prod_3_img{i}.jpg"
    target = f"{output_dir}/tifa_{i}.jpg"
    if not os.path.exists(target) and os.path.exists(source):
        import shutil
        shutil.copyfile(source, target)

print("All product assets generated successfully!")

