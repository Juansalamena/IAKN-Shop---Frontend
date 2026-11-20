import json
import re

with open("preview/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Shopee CSS
shopee_css = """
    /* SHOPEE-STYLE PRODUCT MEDIA GALLERY CSS */
    .shopee-hero-media {
      height: 310px;
      width: 100%;
      background: #000;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .shopee-video-layer, .shopee-photo-layer {
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000;
    }
    #shopee-video-el {
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #000;
    }
    .shopee-video-thumb-cover {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
    }
    .shopee-video-thumb-cover img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .shopee-play-btn-pulse {
      position: absolute;
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: rgba(238, 77, 45, 0.92);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 0 0 0 rgba(238, 77, 45, 0.7);
      animation: shopeePulse 1.8s infinite;
      transition: transform 0.2s;
    }
    .shopee-play-btn-pulse:hover {
      transform: scale(1.1);
    }
    .shopee-play-btn-pulse span {
      font-size: 34px;
      margin-left: 3px;
    }
    @keyframes shopeePulse {
      0% {
        box-shadow: 0 0 0 0 rgba(238, 77, 45, 0.7);
      }
      70% {
        box-shadow: 0 0 0 16px rgba(238, 77, 45, 0);
      }
      100% {
        box-shadow: 0 0 0 0 rgba(238, 77, 45, 0);
      }
    }
    .shopee-media-top-bar {
      position: absolute;
      top: 12px;
      left: 12px;
      right: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 5;
    }
    .shopee-video-badge-pill {
      background: #ee4d2d;
      color: #fff;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 3px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .shopee-duration-pill {
      background: rgba(0, 0, 0, 0.75);
      color: #fff;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      backdrop-filter: blur(4px);
    }
    .shopee-video-controls {
      position: absolute;
      bottom: 44px;
      left: 10px;
      right: 10px;
      background: rgba(0, 0, 0, 0.75);
      border-radius: 8px;
      padding: 5px 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 5;
      backdrop-filter: blur(6px);
      box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }
    .shopee-ctrl-btn {
      background: none;
      border: none;
      color: #fff;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2px;
      transition: color 0.2s;
    }
    .shopee-ctrl-btn:hover {
      color: #ee4d2d;
    }
    .shopee-ctrl-btn .material-icons {
      font-size: 20px;
    }
    .shopee-time-text {
      color: #e2e8f0;
      font-size: 10px;
      font-weight: 600;
      min-width: 26px;
    }
    .shopee-seek-slider {
      flex: 1;
      height: 4px;
      -webkit-appearance: none;
      appearance: none;
      background: rgba(255, 255, 255, 0.3);
      border-radius: 2px;
      outline: none;
      cursor: pointer;
      accent-color: #ee4d2d;
    }
    .shopee-photo-layer img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      cursor: zoom-in;
    }
    .shopee-arrow-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.5);
      color: #fff;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 4;
      transition: background 0.2s;
    }
    .shopee-arrow-btn:hover {
      background: rgba(0, 0, 0, 0.85);
    }
    .shopee-arrow-btn.left {
      left: 8px;
    }
    .shopee-arrow-btn.right {
      right: 8px;
    }
    .shopee-photo-counter-badge {
      position: absolute;
      bottom: 46px;
      right: 12px;
      background: rgba(0, 0, 0, 0.75);
      color: #fff;
      padding: 4px 9px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      z-index: 5;
    }
    .shopee-media-switcher {
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(0, 0, 0, 0.85);
      border-radius: 20px;
      padding: 3px;
      display: flex;
      gap: 3px;
      z-index: 6;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    .shopee-switcher-pill {
      background: transparent;
      border: none;
      color: #cbd5e1;
      padding: 4px 12px;
      border-radius: 16px;
      font-size: 11px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .shopee-switcher-pill.active-video {
      background: #ee4d2d;
      color: #fff;
      font-weight: 700;
    }
    .shopee-switcher-pill.active-photo {
      background: var(--primary-blue);
      color: #fff;
      font-weight: 700;
    }
    .shopee-thumb-container {
      background: #fff;
      padding: 10px 14px;
      border-bottom: 1px solid #e2e8f0;
      margin-bottom: 8px;
    }
    .shopee-thumb-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .shopee-thumb-strip {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: thin;
      padding-bottom: 4px;
    }
    .shopee-thumb-item {
      flex: 0 0 58px;
      height: 58px;
      border-radius: 8px;
      border: 1.5px solid #e2e8f0;
      overflow: hidden;
      position: relative;
      cursor: pointer;
      background: #f1f5f9;
      transition: all 0.2s;
    }
    .shopee-thumb-item:hover {
      border-color: #94a3b8;
    }
    .shopee-thumb-item.active-video {
      border: 2.5px solid #ee4d2d;
      transform: scale(1.05);
      box-shadow: 0 2px 6px rgba(238, 77, 45, 0.3);
    }
    .shopee-thumb-item.active-photo {
      border: 2.5px solid var(--primary-blue);
      transform: scale(1.05);
      box-shadow: 0 2px 6px rgba(0, 0, 255, 0.25);
    }
    .shopee-thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .shopee-thumb-video-overlay {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.45);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .shopee-thumb-video-icon {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: #ef4444;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
    }
    .shopee-thumb-index-tag {
      position: absolute;
      bottom: 2px;
      right: 2px;
      background: rgba(0, 0, 0, 0.65);
      color: #fff;
      font-size: 8px;
      font-weight: 700;
      padding: 1px 4px;
      border-radius: 3px;
    }
    .badge-video-card {
      position: absolute;
      bottom: 6px;
      right: 6px;
      background: rgba(238, 77, 45, 0.95);
      color: #fff;
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 9px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 2px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.25);
      z-index: 2;
    }
    /* Fullscreen Modal */
    .shopee-fullscreen-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.95);
      z-index: 9999;
      display: flex;
      flex-direction: column;
    }
    .shopee-modal-header {
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(0, 0, 0, 0.6);
    }
    .shopee-modal-close {
      background: none;
      border: none;
      color: #fff;
      cursor: pointer;
      font-size: 24px;
    }
    .shopee-modal-body {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }
    .shopee-modal-body img {
      max-width: 95%;
      max-height: 90vh;
      object-fit: contain;
    }
    .shopee-modal-body video {
      max-width: 95%;
      max-height: 85vh;
      outline: none;
    }
    .shopee-modal-footer {
      padding: 12px;
      text-align: center;
      background: rgba(0, 0, 0, 0.6);
    }
"""

if "/* SHOPEE-STYLE PRODUCT MEDIA GALLERY CSS */" not in html:
    html = html.replace("</style>", shopee_css + "\n  </style>")

# 2. Update Detail Produk Screen HTML inside screen-detail-produk
old_detail_hero_markup = """          <!-- Hero Image Box -->
          <div class="detail-hero-box" id="detail-hero-box" style="background: linear-gradient(135deg, #fef08a 0%, #fde047 100%);">
            <span class="material-icons" id="detail-hero-icon" style="font-size: 100px; color: #854d0e;">auto_stories</span>
            <div class="detail-tag-badge" id="detail-tag-badge">Buku Ilmiah</div>
            <div class="detail-discount-badge" id="detail-discount-badge" style="display: none;">-40%</div>
          </div>"""

new_shopee_hero_markup = """          <!-- SHOPEE-STYLE HERO MEDIA CAROUSEL & VIDEO PLAYER -->
          <div class="shopee-hero-media" id="detail-hero-media">
            <!-- Video Layer -->
            <div class="shopee-video-layer" id="shopee-video-layer">
              <video id="shopee-video-el" playsinline preload="metadata" ontimeupdate="onShopeeVideoTimeUpdate()" onended="onShopeeVideoEnded()">
                <source id="shopee-video-src" src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" type="video/mp4">
              </video>
              <div class="shopee-video-thumb-cover" id="shopee-video-thumb-cover" onclick="toggleShopeeVideo()">
                <img id="shopee-video-thumb-img" src="assets/images/produk/prod_1_video_thumb.jpg" alt="Thumbnail Video">
                <div class="shopee-play-btn-pulse">
                  <span class="material-icons" id="shopee-center-play-icon">play_arrow</span>
                </div>
              </div>
              <!-- Top Badges -->
              <div class="shopee-media-top-bar">
                <div class="shopee-video-badge-pill">
                  <span class="material-icons" style="font-size: 13px;">videocam</span>
                  <span>VIDEO RESMI</span>
                </div>
                <div class="shopee-duration-pill" id="shopee-duration-pill">0:35</div>
              </div>
              <!-- Bottom Custom Shopee Video Controls -->
              <div class="shopee-video-controls" id="shopee-video-controls">
                <button class="shopee-ctrl-btn" onclick="toggleShopeeVideo()" title="Putar/Jeda">
                  <span class="material-icons" id="shopee-play-pause-icon">play_arrow</span>
                </button>
                <span class="shopee-time-text" id="shopee-time-current">0:00</span>
                <input type="range" class="shopee-seek-slider" id="shopee-seek-slider" min="0" max="100" value="0" oninput="seekShopeeVideo(this.value)">
                <span class="shopee-time-text" id="shopee-time-total">0:35</span>
                <button class="shopee-ctrl-btn" onclick="toggleShopeeMute()" title="Suara">
                  <span class="material-icons" id="shopee-volume-icon">volume_up</span>
                </button>
                <button class="shopee-ctrl-btn" onclick="openShopeeVideoFullscreen()" title="Layar Penuh">
                  <span class="material-icons">fullscreen</span>
                </button>
              </div>
            </div>

            <!-- Photo Layer -->
            <div class="shopee-photo-layer" id="shopee-photo-layer" style="display: none;">
              <img id="shopee-photo-img" src="assets/images/produk/prod_1_img1.jpg" alt="Foto Produk" onclick="openShopeePhotoFullscreen()">
              <button class="shopee-arrow-btn left" onclick="prevShopeePhoto()">
                <span class="material-icons">chevron_left</span>
              </button>
              <button class="shopee-arrow-btn right" onclick="nextShopeePhoto()">
                <span class="material-icons">chevron_right</span>
              </button>
              <div class="detail-tag-badge" id="detail-tag-badge">Buku Ilmiah</div>
              <div class="detail-discount-badge" id="detail-discount-badge" style="display: none;">-40%</div>
              <div class="shopee-photo-counter-badge" id="shopee-photo-counter" onclick="openShopeePhotoFullscreen()">
                <span class="material-icons" style="font-size: 13px;">photo_camera</span>
                <span id="shopee-photo-counter-text">1/7</span>
              </div>
            </div>

            <!-- Shopee Segmented Switcher Pill: [ ▶ Video ] / [ 📷 Foto ] -->
            <div class="shopee-media-switcher">
              <button class="shopee-switcher-pill active-video" id="pill-media-video" onclick="setShopeeMediaType('video')">
                <span class="material-icons" style="font-size: 13px;">play_circle</span>
                <span id="pill-video-label">Video (0:35)</span>
              </button>
              <button class="shopee-switcher-pill" id="pill-media-photo" onclick="setShopeeMediaType('photo')">
                <span class="material-icons" style="font-size: 13px;">photo_library</span>
                <span id="pill-photo-label">Foto (7)</span>
              </button>
            </div>
          </div>

          <!-- SHOPEE THUMBNAIL STRIP -->
          <div class="shopee-thumb-container">
            <div class="shopee-thumb-header">
              <span style="font-size: 11px; font-weight: 700; color: #1e293b;" id="shopee-thumb-title">Galeri Media (8 Media)</span>
              <span style="font-size: 10px; color: #64748b;" id="shopee-thumb-status">Sedang memutar video</span>
            </div>
            <div class="shopee-thumb-strip" id="shopee-thumb-strip">
              <!-- Dynamically rendered thumbnails -->
            </div>
          </div>"""

assert old_detail_hero_markup in html, "Could not find old_detail_hero_markup"
html = html.replace(old_detail_hero_markup, new_shopee_hero_markup, 1)

# 3. Add Fullscreen Modal before </body>
modal_html = """  <!-- Shopee Fullscreen Media Lightbox Modal -->
  <div id="shopee-fullscreen-modal" class="shopee-fullscreen-modal" style="display: none;">
    <div class="shopee-modal-header">
      <span id="shopee-modal-title" style="color: #fff; font-size: 13px; font-weight: 700;">Galeri Produk</span>
      <button class="shopee-modal-close" onclick="closeShopeeFullscreen()"><span class="material-icons">close</span></button>
    </div>
    <div class="shopee-modal-body" id="shopee-modal-body">
      <img id="shopee-modal-img" src="" alt="Zoom Foto">
      <video id="shopee-modal-video" controls playsinline style="display: none; width: 90%; max-height: 80vh;">
        <source id="shopee-modal-video-src" src="" type="video/mp4">
      </video>
      <button class="shopee-arrow-btn left" id="shopee-modal-prev" onclick="prevShopeePhotoModal()" style="display: none;">
        <span class="material-icons">chevron_left</span>
      </button>
      <button class="shopee-arrow-btn right" id="shopee-modal-next" onclick="nextShopeePhotoModal()" style="display: none;">
        <span class="material-icons">chevron_right</span>
      </button>
    </div>
    <div class="shopee-modal-footer">
      <span id="shopee-modal-counter" style="color: rgba(255,255,255,0.8); font-size: 12px;">Foto 1 dari 7</span>
    </div>
  </div>
"""

if "id=\"shopee-fullscreen-modal\"" not in html:
    html = html.replace("</body>", modal_html + "\n</body>")

# 4. Update allHomeProducts in preview/index.html with 7-8 images + 1 video for all 12 products
new_all_home_products_js = """    // Home Products Catalog Data with 7-8 images and 1 video each (Shopee style)
    const allHomeProducts = [
      {
        id: "prod_1",
        tag: "Buku Ilmiah",
        title: "Antropologi Musik Maluku & Nusantara",
        author: "Oleh: Prodi Musik Gereja",
        category: "Buku/Ilmiah",
        price: 85000,
        priceStr: "Rp 85.000",
        rating: 4.9,
        reviews: 120,
        icon: "auto_stories",
        bg: "linear-gradient(135deg, #fef08a 0%, #fde047 100%)",
        iconColor: "#854d0e",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
        videoThumbnail: "assets/images/produk/prod_1_video_thumb.jpg",
        videoDuration: "0:35",
        videoTitle: "Video Bedah Buku Antropologi Musik Maluku",
        images: [
          "assets/images/produk/prod_1_img1.jpg",
          "assets/images/produk/prod_1_img2.jpg",
          "assets/images/produk/prod_1_img3.jpg",
          "assets/images/produk/prod_1_img4.jpg",
          "assets/images/produk/prod_1_img5.jpg",
          "assets/images/produk/prod_1_img6.jpg",
          "assets/images/produk/prod_1_img7.jpg"
        ]
      },
      {
        id: "prod_2",
        tag: "Jasa Grafis",
        title: "Desain Banner & Publikasi Acara Kampus",
        author: "Kreatif Lab Mahasiswa",
        category: "Desain Grafis",
        price: 50000,
        priceStr: "Rp 50.000",
        rating: 4.8,
        reviews: 85,
        icon: "palette",
        bg: "linear-gradient(135deg, #e9d5ff 0%, #c084fc 100%)",
        iconColor: "#6b21a8",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
        videoThumbnail: "assets/images/produk/prod_2_video_thumb.jpg",
        videoDuration: "0:28",
        videoTitle: "Video Portofolio Desain & Proses Kreatif",
        images: [
          "assets/images/produk/prod_2_img1.jpg",
          "assets/images/produk/prod_2_img2.jpg",
          "assets/images/produk/prod_2_img3.jpg",
          "assets/images/produk/prod_2_img4.jpg",
          "assets/images/produk/prod_2_img5.jpg",
          "assets/images/produk/prod_2_img6.jpg",
          "assets/images/produk/prod_2_img7.jpg"
        ]
      },
      {
        id: "prod_3",
        tag: "Alat Musik",
        title: "Tifa Maluku Kayu Ukir Asli",
        author: "Bengkel Seni Kampus",
        category: "Alat Musik",
        price: 350000,
        priceStr: "Rp 350.000",
        rating: 5.0,
        reviews: 25,
        icon: "music_note",
        bg: "linear-gradient(135deg, #fed7aa 0%, #fb923c 100%)",
        iconColor: "#9a3412",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
        videoThumbnail: "assets/images/produk/prod_3_video_thumb.jpg",
        videoDuration: "0:42",
        videoTitle: "Video Uji Suara & Dentuman Akustik Tifa",
        images: [
          "assets/images/produk/prod_3_img1.jpg",
          "assets/images/produk/prod_3_img2.jpg",
          "assets/images/produk/prod_3_img3.jpg",
          "assets/images/produk/prod_3_img4.jpg",
          "assets/images/produk/prod_3_img5.jpg",
          "assets/images/produk/prod_3_img6.jpg",
          "assets/images/produk/prod_3_img7.jpg"
        ]
      },
      {
        id: "prod_4",
        tag: "Tek. Edukasi",
        title: "Media Belajar Interaktif PAUD Kristen",
        author: "Laboratorium FKIP IAKN",
        category: "Tek. Edukasi",
        price: 125000,
        priceStr: "Rp 125.000",
        rating: 4.9,
        reviews: 42,
        icon: "laptop_chromebook",
        bg: "linear-gradient(135deg, #bfdbfe 0%, #60a5fa 100%)",
        iconColor: "#1e40af",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyBlazes.mp4",
        videoThumbnail: "assets/images/produk/prod_4_video_thumb.jpg",
        videoDuration: "0:30",
        videoTitle: "Video Cuplikan Game & Animasi Edukatif PAUD",
        images: [
          "assets/images/produk/prod_4_img1.jpg",
          "assets/images/produk/prod_4_img2.jpg",
          "assets/images/produk/prod_4_img3.jpg",
          "assets/images/produk/prod_4_img4.jpg",
          "assets/images/produk/prod_4_img5.jpg",
          "assets/images/produk/prod_4_img6.jpg",
          "assets/images/produk/prod_4_img7.jpg"
        ]
      },
      {
        id: "prod_5",
        tag: "Karya Dosen",
        title: "Buku Teologi Kontekstual & Budaya Maluku",
        author: "Penulis: Dosen IAKN",
        category: "Buku/Ilmiah",
        price: 95000,
        priceStr: "Rp 95.000",
        rating: 5.0,
        reviews: 82,
        icon: "menu_book",
        bg: "linear-gradient(135deg, #fef08a 0%, #facc15 100%)",
        iconColor: "#854d0e",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4",
        videoThumbnail: "assets/images/produk/prod_5_video_thumb.jpg",
        videoDuration: "0:45",
        videoTitle: "Video Ulasan Akademis bersama Dosen Penulis",
        images: [
          "assets/images/produk/prod_5_img1.jpg",
          "assets/images/produk/prod_5_img2.jpg",
          "assets/images/produk/prod_5_img3.jpg",
          "assets/images/produk/prod_5_img4.jpg",
          "assets/images/produk/prod_5_img5.jpg",
          "assets/images/produk/prod_5_img6.jpg",
          "assets/images/produk/prod_5_img7.jpg"
        ]
      },
      {
        id: "prod_6",
        tag: "Merchandise",
        title: "Hoodie Dies Natalis IAKN Ke-25",
        author: "Koperasi Mahasiswa IAKN",
        category: "Merchandise",
        price: 99000,
        priceStr: "Rp 99.000",
        rating: 4.9,
        reviews: 165,
        icon: "checkroom",
        bg: "linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)",
        iconColor: "#ffffff",
        oldPrice: "165rb",
        discount: "-40%",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
        videoThumbnail: "assets/images/produk/prod_6_video_thumb.jpg",
        videoDuration: "0:25",
        videoTitle: "Video Try-On & Uji Kualitas Bahan Hoodie",
        images: [
          "assets/images/produk/prod_6_img1.jpg",
          "assets/images/produk/prod_6_img2.jpg",
          "assets/images/produk/prod_6_img3.jpg",
          "assets/images/produk/prod_6_img4.jpg",
          "assets/images/produk/prod_6_img5.jpg",
          "assets/images/produk/prod_6_img6.jpg",
          "assets/images/produk/prod_6_img7.jpg",
          "assets/images/produk/prod_6_img8.jpg"
        ]
      },
      {
        id: "prod_7",
        tag: "Merchandise",
        title: "Tumbler Grafir Logo Edisi Ambon",
        author: "Koperasi Mahasiswa",
        category: "Merchandise",
        price: 45000,
        priceStr: "Rp 45.000",
        rating: 4.8,
        reviews: 90,
        icon: "local_cafe",
        bg: "linear-gradient(135deg, #06b6d4 0%, #0891b2 100%)",
        iconColor: "#ffffff",
        oldPrice: "90rb",
        discount: "-50%",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackSeeTheWorld.mp4",
        videoThumbnail: "assets/images/produk/prod_7_video_thumb.jpg",
        videoDuration: "0:20",
        videoTitle: "Video Uji Ketahanan Suhu & Anti Bocor Tumbler",
        images: [
          "assets/images/produk/prod_7_img1.jpg",
          "assets/images/produk/prod_7_img2.jpg",
          "assets/images/produk/prod_7_img3.jpg",
          "assets/images/produk/prod_7_img4.jpg",
          "assets/images/produk/prod_7_img5.jpg",
          "assets/images/produk/prod_7_img6.jpg",
          "assets/images/produk/prod_7_img7.jpg"
        ]
      },
      {
        id: "prod_8",
        tag: "Kriya Seni",
        title: "Miniatur Tifa Khas Maluku Orisinal",
        author: "Sanggar Seni & Kriya Kampus",
        category: "Alat Musik",
        price: 50000,
        priceStr: "Rp 50.000",
        rating: 4.9,
        reviews: 50,
        icon: "apartment",
        bg: "linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%)",
        iconColor: "#ffffff",
        oldPrice: "100rb",
        discount: "-50%",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
        videoThumbnail: "assets/images/produk/prod_8_video_thumb.jpg",
        videoDuration: "0:22",
        videoTitle: "Video 360 Derajat Rotasi Miniatur Tifa",
        images: [
          "assets/images/produk/prod_8_img1.jpg",
          "assets/images/produk/prod_8_img2.jpg",
          "assets/images/produk/prod_8_img3.jpg",
          "assets/images/produk/prod_8_img4.jpg",
          "assets/images/produk/prod_8_img5.jpg",
          "assets/images/produk/prod_8_img6.jpg",
          "assets/images/produk/prod_8_img7.jpg"
        ]
      },
      {
        id: "prod_9",
        tag: "Layanan Kilat",
        title: "Jasa Translate Naskah Ilmiah & Abstrak",
        author: "Unit Bahasa Kampus",
        category: "Jasa/Layanan",
        price: 35000,
        priceStr: "Rp 35.000",
        rating: 4.9,
        reviews: 64,
        icon: "translate",
        bg: "linear-gradient(135deg, #e9d5ff 0%, #c084fc 100%)",
        iconColor: "#6b21a8",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4",
        videoThumbnail: "assets/images/produk/prod_9_video_thumb.jpg",
        videoDuration: "0:32",
        videoTitle: "Video Prosedur & Standar Mutu Terjemahan Naskah",
        images: [
          "assets/images/produk/prod_9_img1.jpg",
          "assets/images/produk/prod_9_img2.jpg",
          "assets/images/produk/prod_9_img3.jpg",
          "assets/images/produk/prod_9_img4.jpg",
          "assets/images/produk/prod_9_img5.jpg",
          "assets/images/produk/prod_9_img6.jpg",
          "assets/images/produk/prod_9_img7.jpg"
        ]
      },
      {
        id: "prod_10",
        tag: "Merchandise BEM",
        title: "Totebag Kanvas Motif Tenun Maluku",
        author: "BEM IAKN Ambon",
        category: "Merchandise",
        price: 45000,
        priceStr: "Rp 45.000",
        rating: 4.7,
        reviews: 53,
        icon: "shopping_bag",
        bg: "linear-gradient(135deg, #fbcfe8 0%, #f472b6 100%)",
        iconColor: "#9d174d",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4",
        videoThumbnail: "assets/images/produk/prod_10_video_thumb.jpg",
        videoDuration: "0:26",
        videoTitle: "Video Uji Kapasitas & Ketahanan Muatan Totebag",
        images: [
          "assets/images/produk/prod_10_img1.jpg",
          "assets/images/produk/prod_10_img2.jpg",
          "assets/images/produk/prod_10_img3.jpg",
          "assets/images/produk/prod_10_img4.jpg",
          "assets/images/produk/prod_10_img5.jpg",
          "assets/images/produk/prod_10_img6.jpg",
          "assets/images/produk/prod_10_img7.jpg"
        ]
      },
      {
        id: "prod_11",
        tag: "Karya Mahasiswa",
        title: "Gitar Akustik Custom Mahasiswa",
        author: "Prodi Pendidikan Seni",
        category: "Alat Musik",
        price: 750000,
        priceStr: "Rp 750.000",
        rating: 4.8,
        reviews: 19,
        icon: "music_note",
        bg: "linear-gradient(135deg, #bbf7d0 0%, #4ade80 100%)",
        iconColor: "#166534",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
        videoThumbnail: "assets/images/produk/prod_11_video_thumb.jpg",
        videoDuration: "0:48",
        videoTitle: "Video Soundcheck Akustik & Petikan Melodi Gitar",
        images: [
          "assets/images/produk/prod_11_img1.jpg",
          "assets/images/produk/prod_11_img2.jpg",
          "assets/images/produk/prod_11_img3.jpg",
          "assets/images/produk/prod_11_img4.jpg",
          "assets/images/produk/prod_11_img5.jpg",
          "assets/images/produk/prod_11_img6.jpg",
          "assets/images/produk/prod_11_img7.jpg",
          "assets/images/produk/prod_11_img8.jpg"
        ]
      },
      {
        id: "prod_12",
        tag: "Lisensi Edu",
        title: "Software Pembelajaran Liturgi Digital",
        author: "Lab Komputer IAKN",
        category: "Tek. Edukasi",
        price: 150000,
        priceStr: "Rp 150.000",
        rating: 4.9,
        reviews: 31,
        icon: "computer",
        bg: "linear-gradient(135deg, #ccfbf1 0%, #2dd4bf 100%)",
        iconColor: "#115e59",
        videoUrl: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
        videoThumbnail: "assets/images/produk/prod_12_video_thumb.jpg",
        videoDuration: "0:40",
        videoTitle: "Video Demo Navigasi & Fitur Partitur Digital",
        images: [
          "assets/images/produk/prod_12_img1.jpg",
          "assets/images/produk/prod_12_img2.jpg",
          "assets/images/produk/prod_12_img3.jpg",
          "assets/images/produk/prod_12_img4.jpg",
          "assets/images/produk/prod_12_img5.jpg",
          "assets/images/produk/prod_12_img6.jpg",
          "assets/images/produk/prod_12_img7.jpg"
        ]
      }
    ];"""

all_home_products_pattern = re.compile(r"    // Home Products Catalog Data for Search\s+const allHomeProducts = \[.+?\n    \];", re.DOTALL)
assert all_home_products_pattern.search(html), "Could not find allHomeProducts array in preview/index.html"
html = all_home_products_pattern.sub(new_all_home_products_js, html, count=1)

# 5. Add JavaScript functions for Shopee media gallery
shopee_js = """
    // SHOPEE MEDIA GALLERY LOGIC
    let shopeeMediaType = 'video'; // 'video' or 'photo'
    let currentShopeePhotoIndex = 0;
    let isShopeeVideoPlaying = false;
    let isShopeeVideoMuted = false;

    function formatShopeeTime(seconds) {
      if (isNaN(seconds)) return "0:00";
      const m = Math.floor(seconds / 60);
      const s = Math.floor(seconds % 60);
      return m + ":" + (s < 10 ? "0" : "") + s;
    }

    function setShopeeMediaType(type, photoIdx = 0) {
      shopeeMediaType = type;
      currentShopeePhotoIndex = photoIdx;

      const videoLayer = document.getElementById('shopee-video-layer');
      const photoLayer = document.getElementById('shopee-photo-layer');
      const pillVideo = document.getElementById('pill-media-video');
      const pillPhoto = document.getElementById('pill-media-photo');
      const statusEl = document.getElementById('shopee-thumb-status');
      const videoEl = document.getElementById('shopee-video-el');

      if (type === 'video') {
        if (videoLayer) videoLayer.style.display = 'flex';
        if (photoLayer) photoLayer.style.display = 'none';
        if (pillVideo) {
          pillVideo.classList.add('active-video');
        }
        if (pillPhoto) {
          pillPhoto.classList.remove('active-photo');
        }
        if (statusEl) statusEl.textContent = 'Sedang memutar video demo produk';
      } else {
        if (videoEl && !videoEl.paused) {
          videoEl.pause();
          isShopeeVideoPlaying = false;
          updateShopeePlayPauseIcons();
        }
        if (videoLayer) videoLayer.style.display = 'none';
        if (photoLayer) photoLayer.style.display = 'flex';
        if (pillVideo) {
          pillVideo.classList.remove('active-video');
        }
        if (pillPhoto) {
          pillPhoto.classList.add('active-photo');
        }
        updateShopeePhotoDisplay();
      }

      updateShopeeThumbActive();
    }

    function updateShopeePhotoDisplay() {
      if (!currentDetailProduct || !currentDetailProduct.images) return;
      const total = currentDetailProduct.images.length;
      if (total === 0) return;

      currentShopeePhotoIndex = (currentShopeePhotoIndex + total) % total;
      const imgEl = document.getElementById('shopee-photo-img');
      const counterText = document.getElementById('shopee-photo-counter-text');
      const statusEl = document.getElementById('shopee-thumb-status');

      if (imgEl) {
        imgEl.src = currentDetailProduct.images[currentShopeePhotoIndex];
      }
      if (counterText) {
        counterText.textContent = `${currentShopeePhotoIndex + 1}/${total}`;
      }
      if (statusEl) {
        statusEl.textContent = `Foto ${currentShopeePhotoIndex + 1} dari ${total}`;
      }
      updateShopeeThumbActive();
    }

    function prevShopeePhoto() {
      currentShopeePhotoIndex--;
      updateShopeePhotoDisplay();
    }

    function nextShopeePhoto() {
      currentShopeePhotoIndex++;
      updateShopeePhotoDisplay();
    }

    function toggleShopeeVideo() {
      const videoEl = document.getElementById('shopee-video-el');
      const thumbCover = document.getElementById('shopee-video-thumb-cover');
      if (!videoEl) return;

      if (videoEl.paused) {
        videoEl.play().then(() => {
          isShopeeVideoPlaying = true;
          if (thumbCover) thumbCover.style.display = 'none';
          updateShopeePlayPauseIcons();
        }).catch(err => {
          console.log('Autoplay prevented or network blocked:', err);
          // Still simulate play state
          isShopeeVideoPlaying = true;
          if (thumbCover) thumbCover.style.display = 'none';
          updateShopeePlayPauseIcons();
        });
      } else {
        videoEl.pause();
        isShopeeVideoPlaying = false;
        updateShopeePlayPauseIcons();
      }
    }

    function updateShopeePlayPauseIcons() {
      const icon = document.getElementById('shopee-play-pause-icon');
      if (icon) {
        icon.textContent = isShopeeVideoPlaying ? 'pause' : 'play_arrow';
      }
    }

    function toggleShopeeMute() {
      const videoEl = document.getElementById('shopee-video-el');
      const icon = document.getElementById('shopee-volume-icon');
      if (!videoEl) return;
      isShopeeVideoMuted = !isShopeeVideoMuted;
      videoEl.muted = isShopeeVideoMuted;
      if (icon) {
        icon.textContent = isShopeeVideoMuted ? 'volume_off' : 'volume_up';
      }
    }

    function onShopeeVideoTimeUpdate() {
      const videoEl = document.getElementById('shopee-video-el');
      const slider = document.getElementById('shopee-seek-slider');
      const curEl = document.getElementById('shopee-time-current');
      const totEl = document.getElementById('shopee-time-total');
      if (!videoEl || !videoEl.duration) return;

      const cur = videoEl.currentTime;
      const tot = videoEl.duration;
      if (curEl) curEl.textContent = formatShopeeTime(cur);
      if (totEl) totEl.textContent = formatShopeeTime(tot);
      if (slider) slider.value = (cur / tot) * 100;
    }

    function onShopeeVideoEnded() {
      isShopeeVideoPlaying = false;
      updateShopeePlayPauseIcons();
      const thumbCover = document.getElementById('shopee-video-thumb-cover');
      if (thumbCover) thumbCover.style.display = 'flex';
    }

    function seekShopeeVideo(percent) {
      const videoEl = document.getElementById('shopee-video-el');
      if (!videoEl || !videoEl.duration) return;
      videoEl.currentTime = (percent / 100) * videoEl.duration;
    }

    function updateShopeeThumbActive() {
      const strip = document.getElementById('shopee-thumb-strip');
      if (!strip) return;
      const items = strip.querySelectorAll('.shopee-thumb-item');
      items.forEach(el => {
        el.classList.remove('active-video', 'active-photo');
        const mediaType = el.getAttribute('data-type');
        const idx = parseInt(el.getAttribute('data-index') || '0');

        if (shopeeMediaType === 'video' && mediaType === 'video') {
          el.classList.add('active-video');
        } else if (shopeeMediaType === 'photo' && mediaType === 'photo' && idx === currentShopeePhotoIndex) {
          el.classList.add('active-photo');
        }
      });
    }

    function renderShopeeThumbStrip(prod) {
      const strip = document.getElementById('shopee-thumb-strip');
      const titleEl = document.getElementById('shopee-thumb-title');
      if (!strip) return;

      const totalMedia = (prod.videoUrl ? 1 : 0) + (prod.images ? prod.images.length : 0);
      if (titleEl) {
        titleEl.textContent = `Galeri Media (${totalMedia} Media: 1 Video + ${prod.images ? prod.images.length : 0} Foto)`;
      }

      let html = '';
      // 1. Video Thumbnail
      if (prod.videoUrl || prod.videoThumbnail) {
        const thumbSrc = prod.videoThumbnail || (prod.images && prod.images.length ? prod.images[0] : '');
        html += `
          <div class="shopee-thumb-item active-video" data-type="video" onclick="setShopeeMediaType('video')">
            <img src="${thumbSrc}" alt="Video Thumb" onerror="this.src='assets/images/produk/prod_1_video_thumb.jpg'">
            <div class="shopee-thumb-video-overlay">
              <div class="shopee-thumb-video-icon">▶</div>
            </div>
            <div class="shopee-thumb-index-tag" style="background: #ef4444;">${prod.videoDuration || '0:30'}</div>
          </div>
        `;
      }

      // 2. Photo Thumbnails
      if (prod.images && prod.images.length) {
        prod.images.forEach((imgUrl, idx) => {
          html += `
            <div class="shopee-thumb-item" data-type="photo" data-index="${idx}" onclick="setShopeeMediaType('photo', ${idx})">
              <img src="${imgUrl}" alt="Foto ${idx + 1}" onerror="this.src='assets/images/produk/prod_1_img1.jpg'">
              <div class="shopee-thumb-index-tag">${idx + 1}</div>
            </div>
          `;
        });
      }

      strip.innerHTML = html;
    }

    // Fullscreen Modal Logic
    function openShopeePhotoFullscreen() {
      if (!currentDetailProduct || !currentDetailProduct.images) return;
      const modal = document.getElementById('shopee-fullscreen-modal');
      const modalImg = document.getElementById('shopee-modal-img');
      const modalVideo = document.getElementById('shopee-modal-video');
      const prevBtn = document.getElementById('shopee-modal-prev');
      const nextBtn = document.getElementById('shopee-modal-next');
      const titleEl = document.getElementById('shopee-modal-title');
      const counterEl = document.getElementById('shopee-modal-counter');

      if (!modal) return;
      modal.style.display = 'flex';
      if (modalVideo) modalVideo.style.display = 'none';
      if (modalImg) {
        modalImg.style.display = 'block';
        modalImg.src = currentDetailProduct.images[currentShopeePhotoIndex];
      }
      if (prevBtn) prevBtn.style.display = 'flex';
      if (nextBtn) nextBtn.style.display = 'flex';
      if (titleEl) titleEl.textContent = currentDetailProduct.title;
      if (counterEl) counterEl.textContent = `Foto ${currentShopeePhotoIndex + 1} dari ${currentDetailProduct.images.length}`;
    }

    function prevShopeePhotoModal() {
      prevShopeePhoto();
      openShopeePhotoFullscreen();
    }

    function nextShopeePhotoModal() {
      nextShopeePhoto();
      openShopeePhotoFullscreen();
    }

    function openShopeeVideoFullscreen() {
      if (!currentDetailProduct) return;
      const modal = document.getElementById('shopee-fullscreen-modal');
      const modalImg = document.getElementById('shopee-modal-img');
      const modalVideo = document.getElementById('shopee-modal-video');
      const modalVideoSrc = document.getElementById('shopee-modal-video-src');
      const prevBtn = document.getElementById('shopee-modal-prev');
      const nextBtn = document.getElementById('shopee-modal-next');
      const titleEl = document.getElementById('shopee-modal-title');
      const counterEl = document.getElementById('shopee-modal-counter');

      if (!modal) return;
      modal.style.display = 'flex';
      if (modalImg) modalImg.style.display = 'none';
      if (prevBtn) prevBtn.style.display = 'none';
      if (nextBtn) nextBtn.style.display = 'none';
      if (modalVideo && modalVideoSrc) {
        modalVideo.style.display = 'block';
        modalVideoSrc.src = currentDetailProduct.videoUrl || 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4';
        modalVideo.load();
        modalVideo.play().catch(e => console.log('Video play error:', e));
      }
      if (titleEl) titleEl.textContent = currentDetailProduct.videoTitle || (currentDetailProduct.title + " (Video)");
      if (counterEl) counterEl.textContent = `Video Resmi • Durasi ${currentDetailProduct.videoDuration || '0:30'}`;
    }

    function closeShopeeFullscreen() {
      const modal = document.getElementById('shopee-fullscreen-modal');
      const modalVideo = document.getElementById('shopee-modal-video');
      if (modalVideo) {
        modalVideo.pause();
      }
      if (modal) modal.style.display = 'none';
    }
"""

if "function setShopeeMediaType" not in html:
    html = html.replace("    function openProductDetail(prodId) {", shopee_js + "\n    function openProductDetail(prodId) {")

# 6. Update openProductDetail(prodId) to initialize Shopee Media
old_open_detail = """      // Update UI elements
      const heroBox = document.getElementById('detail-hero-box');
      const heroIcon = document.getElementById('detail-hero-icon');
      const tagBadge = document.getElementById('detail-tag-badge');
      const discBadge = document.getElementById('detail-discount-badge');"""

new_open_detail = """      // Update Shopee Media Gallery
      const videoSrcEl = document.getElementById('shopee-video-src');
      const videoEl = document.getElementById('shopee-video-el');
      const videoThumbImg = document.getElementById('shopee-video-thumb-img');
      const thumbCover = document.getElementById('shopee-video-thumb-cover');
      const durationPill = document.getElementById('shopee-duration-pill');
      const timeTotal = document.getElementById('shopee-time-total');
      const pillVideoLabel = document.getElementById('pill-video-label');
      const pillPhotoLabel = document.getElementById('pill-photo-label');

      if (prod.videoUrl && videoSrcEl && videoEl) {
        videoSrcEl.src = prod.videoUrl;
        videoEl.load();
      }
      if (videoThumbImg) {
        videoThumbImg.src = prod.videoThumbnail || (prod.images && prod.images.length ? prod.images[0] : 'assets/images/produk/prod_1_video_thumb.jpg');
      }
      if (thumbCover) {
        thumbCover.style.display = 'flex';
      }
      if (durationPill) durationPill.textContent = prod.videoDuration || '0:30';
      if (timeTotal) timeTotal.textContent = prod.videoDuration || '0:30';
      if (pillVideoLabel) pillVideoLabel.textContent = `Video (${prod.videoDuration || '0:30'})`;
      if (pillPhotoLabel) pillPhotoLabel.textContent = `Foto (${prod.images ? prod.images.length : 0})`;

      renderShopeeThumbStrip(prod);
      setShopeeMediaType(prod.videoUrl ? 'video' : 'photo', 0);

      // Update UI elements
      const tagBadge = document.getElementById('detail-tag-badge');
      const discBadge = document.getElementById('detail-discount-badge');"""

assert old_open_detail in html, "Could not find old_open_detail in preview/index.html"
html = html.replace(old_open_detail, new_open_detail, 1)

# 7. Add Video badge to product cards in search results
old_card_tag = """                <div class="product-img-box" style="background: ${p.bg};">
                  <span class="material-icons" style="color: ${p.iconColor}; font-size: 40px;">${p.icon}</span>
                  <div class="badge-product-tag">${p.tag}</div>
                </div>"""

new_card_tag = """                <div class="product-img-box" style="background: ${p.bg}; position: relative;">
                  ${p.images && p.images.length ? `<img src="${p.images[0]}" alt="${p.title}" style="width: 100%; height: 100%; object-fit: contain; padding: 4px;" onerror="this.style.display='none';">` : `<span class="material-icons" style="color: ${p.iconColor}; font-size: 40px;">${p.icon}</span>`}
                  <div class="badge-product-tag">${p.tag}</div>
                  ${p.videoUrl ? `<div class="badge-video-card"><span class="material-icons" style="font-size: 11px;">play_arrow</span>Video</div>` : ''}
                </div>"""

if old_card_tag in html:
    html = html.replace(old_card_tag, new_card_tag)

with open("preview/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("preview/index.html updated successfully with Shopee-style media gallery!")

