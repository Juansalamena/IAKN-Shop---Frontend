import re

# 1. Update ProductItem and _allProducts in lib/home_screen.dart

product_item_class = '''class ProductItem {
  final String id;
  final String tag;
  final Color tagColor;
  final String title;
  final String author;
  final String category;
  final String price;
  final int priceInt;
  final double rating;
  final int reviews;
  final IconData icon;
  final Color iconColor;
  final bool isFlashSale;
  final String? oldPrice;
  final String? discount;
  final String? description;
  final List<String> images;
  final String? videoUrl;
  final String? videoThumbnail;
  final String? videoDuration;
  final String? videoTitle;

  const ProductItem({
    required this.id,
    required this.tag,
    required this.tagColor,
    required this.title,
    required this.author,
    required this.category,
    required this.price,
    required this.priceInt,
    required this.rating,
    required this.reviews,
    required this.icon,
    required this.iconColor,
    this.isFlashSale = false,
    this.oldPrice,
    this.discount,
    this.description,
    this.images = const [],
    this.videoUrl,
    this.videoThumbnail,
    this.videoDuration,
    this.videoTitle,
  });
}'''

all_products_dart = '''  // Complete catalog of IAKN Commerce products with 7-8 images and 1 video each (Shopee style)
  final List<ProductItem> _allProducts = const [
    ProductItem(
      id: "prod_1",
      tag: "Buku Ilmiah",
      tagColor: Colors.blue,
      title: "Antropologi Musik Maluku & Nusantara",
      author: "Oleh: Prodi Musik Gereja",
      category: "Buku/Ilmiah",
      price: "Rp 85.000",
      priceInt: 85000,
      rating: 4.9,
      reviews: 120,
      icon: Icons.menu_book,
      iconColor: Colors.blue,
      description:
          "Buku referensi ilmiah karya kolaboratif dosen dan mahasiswa Program Studi Musik Gereja IAKN Ambon. Mengulas secara mendalam kekayaan etnomusikologi, ragam nyanyian liturgi kontekstual, dan instrumen tradisional khas Maluku dalam perspektif antropologi budaya Nusantara.",
      images: [
        "assets/images/produk/prod_1_img1.jpg",
        "assets/images/produk/prod_1_img2.jpg",
        "assets/images/produk/prod_1_img3.jpg",
        "assets/images/produk/prod_1_img4.jpg",
        "assets/images/produk/prod_1_img5.jpg",
        "assets/images/produk/prod_1_img6.jpg",
        "assets/images/produk/prod_1_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
      videoThumbnail: "assets/images/produk/prod_1_video_thumb.jpg",
      videoDuration: "0:35",
      videoTitle: "Video Bedah Buku Antropologi Musik Maluku",
    ),
    ProductItem(
      id: "prod_2",
      tag: "Jasa Grafis",
      tagColor: Colors.purple,
      title: "Desain Banner & Publikasi Acara Kampus",
      author: "Kreatif Lab Mahasiswa",
      category: "Desain Grafis",
      price: "Rp 50.000",
      priceInt: 50000,
      rating: 4.8,
      reviews: 85,
      icon: Icons.design_services,
      iconColor: Colors.purple,
      description:
          "Layanan pembuatan desain visual profesional oleh tim Kreatif Lab Mahasiswa IAKN. Melayani pembuatan poster seminar, spanduk dies natalis, banner kegiatan gerejawi, brosur, serta grafis media sosial dengan revisi fleksibel dan pengerjaan kilat 24 jam.",
      images: [
        "assets/images/produk/prod_2_img1.jpg",
        "assets/images/produk/prod_2_img2.jpg",
        "assets/images/produk/prod_2_img3.jpg",
        "assets/images/produk/prod_2_img4.jpg",
        "assets/images/produk/prod_2_img5.jpg",
        "assets/images/produk/prod_2_img6.jpg",
        "assets/images/produk/prod_2_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
      videoThumbnail: "assets/images/produk/prod_2_video_thumb.jpg",
      videoDuration: "0:28",
      videoTitle: "Video Portofolio Desain & Proses Kreatif",
    ),
    ProductItem(
      id: "prod_3",
      tag: "Alat Musik",
      tagColor: Colors.deepOrange,
      title: "Tifa Maluku Kayu Ukir Asli",
      author: "Bengkel Seni Kampus",
      category: "Alat Musik",
      price: "Rp 350.000",
      priceInt: 350000,
      rating: 5.0,
      reviews: 25,
      icon: Icons.music_note,
      iconColor: Colors.deepOrange,
      description:
          "Instrumen musik perkusi tifa tradisional khas Maluku yang dipahat langsung oleh mahasiswa seni kriya kampus. Dibuat menggunakan kayu lenggua pilihan berkepadatan tinggi dan membran kulit alami yang menghasilkan resonansi suara autentik dan kuat untuk ibadah dan pertunjukan seni.",
      images: [
        "assets/images/produk/prod_3_img1.jpg",
        "assets/images/produk/prod_3_img2.jpg",
        "assets/images/produk/prod_3_img3.jpg",
        "assets/images/produk/prod_3_img4.jpg",
        "assets/images/produk/prod_3_img5.jpg",
        "assets/images/produk/prod_3_img6.jpg",
        "assets/images/produk/prod_3_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
      videoThumbnail: "assets/images/produk/prod_3_video_thumb.jpg",
      videoDuration: "0:42",
      videoTitle: "Video Uji Suara & Dentuman Akustik Tifa",
    ),
    ProductItem(
      id: "prod_4",
      tag: "Tek. Edukasi",
      tagColor: Colors.teal,
      title: "Media Belajar Interaktif PAUD Kristen",
      author: "Laboratorium FKIP IAKN",
      category: "Tek. Edukasi",
      price: "Rp 125.000",
      priceInt: 125000,
      rating: 4.9,
      reviews: 42,
      icon: Icons.computer,
      iconColor: Colors.teal,
      description:
          "Paket perangkat ajar edukatif interaktif rancangan Laboratorium FKIP IAKN Ambon. Dilengkapi materi cerita Alkitab anak, lagu rohani interaktif, dan lembar aktivitas kreatif ramah anak usia dini.",
      images: [
        "assets/images/produk/prod_4_img1.jpg",
        "assets/images/produk/prod_4_img2.jpg",
        "assets/images/produk/prod_4_img3.jpg",
        "assets/images/produk/prod_4_img4.jpg",
        "assets/images/produk/prod_4_img5.jpg",
        "assets/images/produk/prod_4_img6.jpg",
        "assets/images/produk/prod_4_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyBlazes.mp4",
      videoThumbnail: "assets/images/produk/prod_4_video_thumb.jpg",
      videoDuration: "0:30",
      videoTitle: "Video Cuplikan Game & Animasi Edukatif PAUD",
    ),
    ProductItem(
      id: "prod_5",
      tag: "Karya Dosen",
      tagColor: Colors.blue,
      title: "Buku Teologi Kontekstual & Budaya Maluku",
      author: "Penulis: Dosen IAKN",
      category: "Buku/Ilmiah",
      price: "Rp 95.000",
      priceInt: 95000,
      rating: 5.0,
      reviews: 82,
      icon: Icons.menu_book,
      iconColor: Colors.blue,
      description:
          "Karya ilmiah unggulan dosen IAKN Ambon yang membahas integrasi nilai-nilai kearifan lokal 'Pela Gandong' dengan teologi kontekstual kontemporer dalam membina harmoni dan persaudaraan masyarakat kepulauan.",
      images: [
        "assets/images/produk/prod_5_img1.jpg",
        "assets/images/produk/prod_5_img2.jpg",
        "assets/images/produk/prod_5_img3.jpg",
        "assets/images/produk/prod_5_img4.jpg",
        "assets/images/produk/prod_5_img5.jpg",
        "assets/images/produk/prod_5_img6.jpg",
        "assets/images/produk/prod_5_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4",
      videoThumbnail: "assets/images/produk/prod_5_video_thumb.jpg",
      videoDuration: "0:45",
      videoTitle: "Video Ulasan Akademis bersama Dosen Penulis",
    ),
    ProductItem(
      id: "prod_6",
      tag: "Flash Sale",
      tagColor: Colors.red,
      title: "Hoodie Dies Natalis IAKN Ke-25",
      author: "Koperasi Mahasiswa IAKN",
      category: "Merchandise",
      price: "Rp 99.000",
      priceInt: 99000,
      rating: 4.9,
      reviews: 165,
      icon: Icons.checkroom,
      iconColor: Colors.indigo,
      isFlashSale: true,
      oldPrice: "165rb",
      discount: "-40%",
      description:
          "Hoodie edisi eksklusif perayaan Dies Natalis IAKN Ambon ke-25. Dibuat dari bahan premium cotton fleece 330 gsm yang lembut, hangat, dan nyaman dipakai kuliah sehari-hari dengan sablon grafis logo IAKN tahan lama.",
      images: [
        "assets/images/produk/prod_6_img1.jpg",
        "assets/images/produk/prod_6_img2.jpg",
        "assets/images/produk/prod_6_img3.jpg",
        "assets/images/produk/prod_6_img4.jpg",
        "assets/images/produk/prod_6_img5.jpg",
        "assets/images/produk/prod_6_img6.jpg",
        "assets/images/produk/prod_6_img7.jpg",
        "assets/images/produk/prod_6_img8.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
      videoThumbnail: "assets/images/produk/prod_6_video_thumb.jpg",
      videoDuration: "0:25",
      videoTitle: "Video Try-On & Uji Kualitas Bahan Hoodie",
    ),
    ProductItem(
      id: "prod_7",
      tag: "Flash Sale",
      tagColor: Colors.red,
      title: "Tumbler Grafir Logo Edisi Ambon",
      author: "Koperasi Mahasiswa",
      category: "Merchandise",
      price: "Rp 45.000",
      priceInt: 45000,
      rating: 4.8,
      reviews: 90,
      icon: Icons.local_drink,
      iconColor: Colors.cyan,
      isFlashSale: true,
      oldPrice: "90rb",
      discount: "-50%",
      description:
          "Tumbler vacuum flask ramah lingkungan edisi Dies Natalis IAKN Ambon. Menjaga suhu air dingin 24 jam dan panas 12 jam, dilengkapi ukiran grafir laser presisi logo kebanggaan IAKN.",
      images: [
        "assets/images/produk/prod_7_img1.jpg",
        "assets/images/produk/prod_7_img2.jpg",
        "assets/images/produk/prod_7_img3.jpg",
        "assets/images/produk/prod_7_img4.jpg",
        "assets/images/produk/prod_7_img5.jpg",
        "assets/images/produk/prod_7_img6.jpg",
        "assets/images/produk/prod_7_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackSeeTheWorld.mp4",
      videoThumbnail: "assets/images/produk/prod_7_video_thumb.jpg",
      videoDuration: "0:20",
      videoTitle: "Video Uji Ketahanan Suhu & Anti Bocor Tumbler",
    ),
    ProductItem(
      id: "prod_8",
      tag: "Kriya Seni",
      tagColor: Colors.deepOrange,
      title: "Miniatur Tifa Khas Maluku Orisinal",
      author: "Sanggar Seni & Kriya Kampus",
      category: "Alat Musik",
      price: "Rp 50.000",
      priceInt: 50000,
      rating: 4.9,
      reviews: 50,
      icon: Icons.music_note,
      iconColor: Colors.deepOrange,
      isFlashSale: true,
      oldPrice: "100rb",
      discount: "-50%",
      description:
          "Suvenir miniatur tifa ukuran 20cm dengan ukiran etnik khas Maluku buatan tangan Sanggar Seni & Kriya Kampus. Sangat pas untuk cenderamata wisuda dan oleh-oleh tamu kehormatan.",
      images: [
        "assets/images/produk/prod_8_img1.jpg",
        "assets/images/produk/prod_8_img2.jpg",
        "assets/images/produk/prod_8_img3.jpg",
        "assets/images/produk/prod_8_img4.jpg",
        "assets/images/produk/prod_8_img5.jpg",
        "assets/images/produk/prod_8_img6.jpg",
        "assets/images/produk/prod_8_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
      videoThumbnail: "assets/images/produk/prod_8_video_thumb.jpg",
      videoDuration: "0:22",
      videoTitle: "Video 360 Derajat Rotasi Miniatur Tifa",
    ),
    ProductItem(
      id: "prod_9",
      tag: "Layanan Kilat",
      tagColor: Colors.purple,
      title: "Jasa Translate Naskah Ilmiah & Abstrak",
      author: "Unit Bahasa Kampus",
      category: "Jasa/Layanan",
      price: "Rp 35.000",
      priceInt: 35000,
      rating: 4.9,
      reviews: 64,
      icon: Icons.translate,
      iconColor: Colors.purple,
      description:
          "Layanan penerjemahan naskah ilmiah, artikel jurnal, skripsi, dan abstrak bilingual (Indonesia - Inggris) oleh tim ahli Unit Bahasa IAKN Ambon dengan akurasi tata bahasa akademis terjamin.",
      images: [
        "assets/images/produk/prod_9_img1.jpg",
        "assets/images/produk/prod_9_img2.jpg",
        "assets/images/produk/prod_9_img3.jpg",
        "assets/images/produk/prod_9_img4.jpg",
        "assets/images/produk/prod_9_img5.jpg",
        "assets/images/produk/prod_9_img6.jpg",
        "assets/images/produk/prod_9_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4",
      videoThumbnail: "assets/images/produk/prod_9_video_thumb.jpg",
      videoDuration: "0:32",
      videoTitle: "Video Prosedur & Standar Mutu Terjemahan Naskah",
    ),
    ProductItem(
      id: "prod_10",
      tag: "Merchandise BEM",
      tagColor: Colors.pink,
      title: "Totebag Kanvas Motif Tenun Maluku",
      author: "BEM IAKN Ambon",
      category: "Merchandise",
      price: "Rp 45.000",
      priceInt: 45000,
      rating: 4.7,
      reviews: 53,
      icon: Icons.shopping_bag,
      iconColor: Colors.pink,
      description:
          "Totebag kanvas tebal ramah lingkungan berhias motif tenun khas Maluku persembahan BEM IAKN Ambon. Cocok untuk membawa buku kuliah, laptop 14 inch, dan perlengkapan harian.",
      images: [
        "assets/images/produk/prod_10_img1.jpg",
        "assets/images/produk/prod_10_img2.jpg",
        "assets/images/produk/prod_10_img3.jpg",
        "assets/images/produk/prod_10_img4.jpg",
        "assets/images/produk/prod_10_img5.jpg",
        "assets/images/produk/prod_10_img6.jpg",
        "assets/images/produk/prod_10_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4",
      videoThumbnail: "assets/images/produk/prod_10_video_thumb.jpg",
      videoDuration: "0:26",
      videoTitle: "Video Uji Kapasitas & Ketahanan Muatan Totebag",
    ),
    ProductItem(
      id: "prod_11",
      tag: "Karya Mahasiswa",
      tagColor: Colors.green,
      title: "Gitar Akustik Custom Mahasiswa",
      author: "Prodi Pendidikan Seni",
      category: "Alat Musik",
      price: "Rp 750.000",
      priceInt: 750000,
      rating: 4.8,
      reviews: 19,
      icon: Icons.music_note,
      iconColor: Colors.green,
      description:
          "Gitar akustik handmade hasil rancang bangun mahasiswa Prodi Pendidikan Seni Musik IAKN Ambon. Menggunakan kayu spruce solid pilihan dengan intonasi nada presisi dan neck ergonomis rosewood.",
      images: [
        "assets/images/produk/prod_11_img1.jpg",
        "assets/images/produk/prod_11_img2.jpg",
        "assets/images/produk/prod_11_img3.jpg",
        "assets/images/produk/prod_11_img4.jpg",
        "assets/images/produk/prod_11_img5.jpg",
        "assets/images/produk/prod_11_img6.jpg",
        "assets/images/produk/prod_11_img7.jpg",
        "assets/images/produk/prod_11_img8.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
      videoThumbnail: "assets/images/produk/prod_11_video_thumb.jpg",
      videoDuration: "0:48",
      videoTitle: "Video Soundcheck Akustik & Petikan Melodi Gitar",
    ),
    ProductItem(
      id: "prod_12",
      tag: "Lisensi Edu",
      tagColor: Colors.teal,
      title: "Software Pembelajaran Liturgi Digital",
      author: "Lab Komputer IAKN",
      category: "Tek. Edukasi",
      price: "Rp 150.000",
      priceInt: 150000,
      rating: 4.9,
      reviews: 31,
      icon: Icons.computer,
      iconColor: Colors.teal,
      description:
          "Aplikasi multimedia interaktif panduan tata ibadah dan aransemen musik liturgi digital karya Laboratorium Komputer IAKN Ambon. Dilengkapi partitur digital dan simulasi paduan suara 4 suara.",
      images: [
        "assets/images/produk/prod_12_img1.jpg",
        "assets/images/produk/prod_12_img2.jpg",
        "assets/images/produk/prod_12_img3.jpg",
        "assets/images/produk/prod_12_img4.jpg",
        "assets/images/produk/prod_12_img5.jpg",
        "assets/images/produk/prod_12_img6.jpg",
        "assets/images/produk/prod_12_img7.jpg",
      ],
      videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
      videoThumbnail: "assets/images/produk/prod_12_video_thumb.jpg",
      videoDuration: "0:40",
      videoTitle: "Video Demo Navigasi & Fitur Partitur Digital",
    ),
  ];'''

with open("lib/home_screen.dart", "r", encoding="utf-8") as f:
    home_content = f.read()

# Replace ProductItem class
class_pattern = re.compile(r"class ProductItem \{.+?\n\}", re.DOTALL)
assert class_pattern.search(home_content), "Could not find ProductItem class in home_screen.dart"
home_content = class_pattern.sub(product_item_class, home_content, count=1)

# Replace _allProducts list
prod_list_pattern = re.compile(r"  // Complete catalog of IAKN Commerce products\s+final List<ProductItem> _allProducts = const \[.+?\n  \];", re.DOTALL)
assert prod_list_pattern.search(home_content), "Could not find _allProducts in home_screen.dart"
home_content = prod_list_pattern.sub(all_products_dart, home_content, count=1)

# Add video badge to _buildProductCard in home_screen.dart
tag_badge_str = '''              Positioned(
                top: 6,
                left: 6,
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.95),
                    borderRadius: BorderRadius.circular(4),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withValues(alpha: 0.05),
                        blurRadius: 2,
                      ),
                    ],
                  ),
                  child: Text(
                    product.tag,
                    style: TextStyle(
                      fontSize: 9,
                      fontWeight: FontWeight.bold,
                      color: product.tagColor,
                    ),
                  ),
                ),
              ),'''

video_badge_str = tag_badge_str + '''
              if (product.videoUrl != null || product.videoThumbnail != null)
                Positioned(
                  bottom: 6,
                  right: 6,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 2),
                    decoration: BoxDecoration(
                      color: const Color(0xFFEE4D2D).withValues(alpha: 0.9),
                      borderRadius: BorderRadius.circular(4),
                    ),
                    child: const Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.play_arrow, color: Colors.white, size: 10),
                        SizedBox(width: 2),
                        Text(
                          "Video",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 9,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),'''

assert tag_badge_str in home_content, "tag_badge_str not found in home_screen.dart"
home_content = home_content.replace(tag_badge_str, video_badge_str, 1)

with open("lib/home_screen.dart", "w", encoding="utf-8") as f:
    f.write(home_content)

print("lib/home_screen.dart updated successfully!")


# 2. Update lib/produk_screen.dart
with open("lib/produk_screen.dart", "r", encoding="utf-8") as f:
    prod_content = f.read()

# Replace _allProducts list in produk_screen.dart
prod_screen_list_pattern = re.compile(r"  // Daftar katalog produk IAKN Commerce\s+final List<ProductItem> _allProducts = const \[.+?\n  \];", re.DOTALL)
assert prod_screen_list_pattern.search(prod_content), "Could not find _allProducts in produk_screen.dart"
prod_content = prod_screen_list_pattern.sub(all_products_dart.replace("  // Complete catalog of IAKN Commerce products with 7-8 images and 1 video each (Shopee style)", "  // Daftar katalog produk IAKN Commerce"), prod_content, count=1)

# Add video badge to _buildProductCard in produk_screen.dart
tag_badge_prod_str = '''              Positioned(
                top: 8,
                left: 8,
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.95),
                    borderRadius: BorderRadius.circular(6),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withValues(alpha: 0.08),
                        blurRadius: 3,
                      ),
                    ],
                  ),
                  child: Text(
                    product.tag,
                    style: TextStyle(
                      fontSize: 10,
                      fontWeight: FontWeight.bold,
                      color: product.tagColor,
                    ),
                  ),
                ),
              ),'''

video_badge_prod_str = tag_badge_prod_str + '''
              if (product.videoUrl != null || product.videoThumbnail != null)
                Positioned(
                  bottom: 8,
                  right: 8,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2.5),
                    decoration: BoxDecoration(
                      color: const Color(0xFFEE4D2D).withValues(alpha: 0.92),
                      borderRadius: BorderRadius.circular(4),
                    ),
                    child: const Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.play_arrow, color: Colors.white, size: 11),
                        SizedBox(width: 2),
                        Text(
                          "Video",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 9,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),'''

if tag_badge_prod_str in prod_content:
    prod_content = prod_content.replace(tag_badge_prod_str, video_badge_prod_str, 1)

with open("lib/produk_screen.dart", "w", encoding="utf-8") as f:
    f.write(prod_content)

print("lib/produk_screen.dart updated successfully!")

