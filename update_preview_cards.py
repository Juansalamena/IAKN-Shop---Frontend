with open("preview/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Home Screen 4 Product Cards
old_home_grid = """          <div class="products-grid">
            <!-- Product 1 -->
            <div class="product-card" onclick="openProductDetail('prod_1')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #fef08a 0%, #fde047 100%);">
                <span class="material-icons" style="color: #854d0e; font-size: 42px;">auto_stories</span>
                <div class="badge-product-tag">Buku Ilmiah</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.9</span>
                  <span class="rating-count">(120)</span>
                </div>
                <div class="product-title">Antropologi Musik Maluku &amp; Nusantara</div>
                <div class="product-author">Oleh: Prodi Musik Gereja</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 85.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_1')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Product 2 -->
            <div class="product-card" onclick="openProductDetail('prod_2')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #e9d5ff 0%, #c084fc 100%);">
                <span class="material-icons" style="color: #6b21a8; font-size: 42px;">palette</span>
                <div class="badge-product-tag">Jasa Grafis</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.8</span>
                  <span class="rating-count">(85)</span>
                </div>
                <div class="product-title">Desain Banner &amp; Publikasi Acara...</div>
                <div class="product-author">Kreatif Lab Mahasiswa</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 50.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_2')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Product 3 -->
            <div class="product-card" onclick="openProductDetail('prod_3')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #fed7aa 0%, #fb923c 100%);">
                <span class="material-icons" style="color: #9a3412; font-size: 42px;">music_note</span>
                <div class="badge-product-tag">Alat Musik</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">5.0</span>
                  <span class="rating-count">(25)</span>
                </div>
                <div class="product-title">Tifa Maluku Kayu Ukir Asli</div>
                <div class="product-author">Bengkel Seni Kampus</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 350.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_3')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Product 4 -->
            <div class="product-card" onclick="openProductDetail('prod_4')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #bfdbfe 0%, #60a5fa 100%);">
                <span class="material-icons" style="color: #1e40af; font-size: 42px;">laptop_chromebook</span>
                <div class="badge-product-tag">Tek. Edukasi</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.9</span>
                  <span class="rating-count">(42)</span>
                </div>
                <div class="product-title">Media Belajar Interaktif PAUD...</div>
                <div class="product-author">Laboratorium FKIP IAKN</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 125.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_4')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>
          </div>"""

new_home_grid = """          <div class="products-grid">
            <!-- Product 1 -->
            <div class="product-card" onclick="openProductDetail('prod_1')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #fef08a 0%, #fde047 100%); position: relative;">
                <img src="assets/images/produk/prod_1_img1.jpg" alt="Antropologi Musik" style="width: 100%; height: 100%; object-fit: contain; padding: 4px;">
                <div class="badge-product-tag">Buku Ilmiah</div>
                <div class="badge-video-card"><span class="material-icons" style="font-size: 11px;">play_arrow</span>Video</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.9</span>
                  <span class="rating-count">(120)</span>
                </div>
                <div class="product-title">Antropologi Musik Maluku &amp; Nusantara</div>
                <div class="product-author">Oleh: Prodi Musik Gereja</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 85.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_1')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Product 2 -->
            <div class="product-card" onclick="openProductDetail('prod_2')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #e9d5ff 0%, #c084fc 100%); position: relative;">
                <img src="assets/images/produk/prod_2_img1.jpg" alt="Desain Banner" style="width: 100%; height: 100%; object-fit: contain; padding: 4px;">
                <div class="badge-product-tag">Jasa Grafis</div>
                <div class="badge-video-card"><span class="material-icons" style="font-size: 11px;">play_arrow</span>Video</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.8</span>
                  <span class="rating-count">(85)</span>
                </div>
                <div class="product-title">Desain Banner &amp; Publikasi Acara...</div>
                <div class="product-author">Kreatif Lab Mahasiswa</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 50.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_2')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Product 3 -->
            <div class="product-card" onclick="openProductDetail('prod_3')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #fed7aa 0%, #fb923c 100%); position: relative;">
                <img src="assets/images/produk/prod_3_img1.jpg" alt="Tifa Maluku" style="width: 100%; height: 100%; object-fit: contain; padding: 4px;">
                <div class="badge-product-tag">Alat Musik</div>
                <div class="badge-video-card"><span class="material-icons" style="font-size: 11px;">play_arrow</span>Video</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">5.0</span>
                  <span class="rating-count">(25)</span>
                </div>
                <div class="product-title">Tifa Maluku Kayu Ukir Asli</div>
                <div class="product-author">Bengkel Seni Kampus</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 350.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_3')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Product 4 -->
            <div class="product-card" onclick="openProductDetail('prod_4')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #bfdbfe 0%, #60a5fa 100%); position: relative;">
                <img src="assets/images/produk/prod_4_img1.jpg" alt="Media Belajar PAUD" style="width: 100%; height: 100%; object-fit: contain; padding: 4px;">
                <div class="badge-product-tag">Tek. Edukasi</div>
                <div class="badge-video-card"><span class="material-icons" style="font-size: 11px;">play_arrow</span>Video</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.9</span>
                  <span class="rating-count">(42)</span>
                </div>
                <div class="product-title">Media Belajar Interaktif PAUD...</div>
                <div class="product-author">Laboratorium FKIP IAKN</div>
                <div class="product-bottom">
                  <div class="product-price">Rp 125.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_4')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>
          </div>"""

assert old_home_grid in html, "Could not find old_home_grid"
html = html.replace(old_home_grid, new_home_grid, 1)

# Replace Produk Screen Products Grid
old_produk_grid_header = """          <!-- Products Grid -->
          <div class="products-grid">
            <!-- P1 -->
            <div class="product-card">
              <div class="product-img-box" style="background: linear-gradient(135deg, #dcfce7 0%, #86efac 100%);">
                <span class="material-icons" style="color: #166534; font-size: 42px;">sports_handball</span>
                <div class="badge-product-tag" style="background: #22c55e; color: white;">Handmade Kampus</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.9</span>
                  <span class="rating-count">(48)</span>
                </div>
                <div class="product-title">Tifa Maluku Tradisional Kayu...</div>
                <div class="product-author" style="display: flex; align-items: center; gap: 3px;">
                  <span class="material-icons" style="font-size: 12px; color: #3b82f6;">verified</span>
                  <span>Galeri Seni Musik IAKN</span>
                </div>
                <div class="product-bottom">
                  <div class="product-price">Rp 320.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_3')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>"""

new_produk_grid_header = """          <!-- Products Grid -->
          <div class="products-grid">
            <!-- P1 -->
            <div class="product-card" onclick="openProductDetail('prod_3')" style="cursor: pointer;">
              <div class="product-img-box" style="background: linear-gradient(135deg, #fed7aa 0%, #fb923c 100%); position: relative;">
                <img src="assets/images/produk/prod_3_img1.jpg" alt="Tifa Maluku" style="width: 100%; height: 100%; object-fit: contain; padding: 4px;">
                <div class="badge-product-tag" style="background: #22c55e; color: white;">Handmade Kampus</div>
                <div class="badge-video-card"><span class="material-icons" style="font-size: 11px;">play_arrow</span>Video</div>
              </div>
              <div class="product-card-body">
                <div class="rating-row">
                  <span class="material-icons">star</span>
                  <span class="rating-val">4.9</span>
                  <span class="rating-count">(48)</span>
                </div>
                <div class="product-title">Tifa Maluku Tradisional Kayu...</div>
                <div class="product-author" style="display: flex; align-items: center; gap: 3px;">
                  <span class="material-icons" style="font-size: 12px; color: #3b82f6;">verified</span>
                  <span>Galeri Seni Musik IAKN</span>
                </div>
                <div class="product-bottom">
                  <div class="product-price">Rp 350.000</div>
                  <button class="btn-add-cart" onclick="event.stopPropagation(); addProductToCartHome('prod_3')">
                    <span class="material-icons">shopping_cart</span>
                  </button>
                </div>
              </div>
            </div>"""

if old_produk_grid_header in html:
    html = html.replace(old_produk_grid_header, new_produk_grid_header, 1)

# Make sure all product cards on Produk screen have click triggers to openProductDetail
html = html.replace('<!-- P2 -->\n            <div class="product-card">', '<!-- P2 -->\n            <div class="product-card" onclick="openProductDetail(\'prod_5\')" style="cursor: pointer;">')
html = html.replace('<!-- P3 -->\n            <div class="product-card">', '<!-- P3 -->\n            <div class="product-card" onclick="openProductDetail(\'prod_9\')" style="cursor: pointer;">')
html = html.replace('<!-- P4 -->\n            <div class="product-card">', '<!-- P4 -->\n            <div class="product-card" onclick="openProductDetail(\'prod_11\')" style="cursor: pointer;">')
html = html.replace('<!-- P5 -->\n            <div class="product-card">', '<!-- P5 -->\n            <div class="product-card" onclick="openProductDetail(\'prod_10\')" style="cursor: pointer;">')
html = html.replace('<!-- P6 -->\n            <div class="product-card">', '<!-- P6 -->\n            <div class="product-card" onclick="openProductDetail(\'prod_12\')" style="cursor: pointer;">')

with open("preview/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("preview/index.html product cards updated!")

