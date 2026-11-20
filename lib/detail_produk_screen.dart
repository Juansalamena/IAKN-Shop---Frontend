import 'dart:async';
import 'package:flutter/material.dart';
import 'home_screen.dart';
import 'keranjang_screen.dart';
import 'fullscreen_image_viewer.dart';

enum MediaType { video, photo }

class DetailProdukScreen extends StatefulWidget {
  final ProductItem product;

  const DetailProdukScreen({super.key, required this.product});

  @override
  State<DetailProdukScreen> createState() => _DetailProdukScreenState();
}

class _DetailProdukScreenState extends State<DetailProdukScreen> {
  final Color primaryBlue = const Color(0xFF0000FF);
  final Color darkBlue = const Color(0xFF00008B);
  final Color shopeeOrange = const Color(0xFFEE4D2D);

  bool _isFavorite = false;
  int _selectedQuantity = 1;
  int _currentImageIndex = 0;
  MediaType _selectedMediaType = MediaType.video;

  // Video playback simulation states
  bool _isVideoPlaying = false;
  bool _isMuted = false;
  double _videoProgress = 0.0;
  Timer? _videoTimer;
  int _videoElapsedSeconds = 0;
  late int _videoTotalSeconds;
  final PageController _imagePageController = PageController();

  @override
  void initState() {
    super.initState();
    // Default to video if available, else photo
    if (widget.product.videoUrl != null || widget.product.videoThumbnail != null) {
      _selectedMediaType = MediaType.video;
    } else {
      _selectedMediaType = MediaType.photo;
    }

    _videoTotalSeconds = _parseDuration(widget.product.videoDuration ?? "0:30");
  }

  int _parseDuration(String durationStr) {
    try {
      final parts = durationStr.split(':');
      if (parts.length == 2) {
        return int.parse(parts[0]) * 60 + int.parse(parts[1]);
      }
    } catch (_) {}
    return 30;
  }

  String _formatTime(int seconds) {
    final m = seconds ~/ 60;
    final s = seconds % 60;
    return "$m:${s.toString().padLeft(2, '0')}";
  }

  void _togglePlayVideo() {
    setState(() {
      _isVideoPlaying = !_isVideoPlaying;
    });

    if (_isVideoPlaying) {
      _videoTimer?.cancel();
      _videoTimer = Timer.periodic(const Duration(seconds: 1), (timer) {
        if (!mounted) return;
        setState(() {
          if (_videoElapsedSeconds < _videoTotalSeconds) {
            _videoElapsedSeconds++;
            _videoProgress = _videoElapsedSeconds / _videoTotalSeconds;
          } else {
            // Loop or finish
            _videoElapsedSeconds = 0;
            _videoProgress = 0.0;
          }
        });
      });
    } else {
      _videoTimer?.cancel();
    }
  }

  void _seekVideo(double value) {
    setState(() {
      _videoProgress = value;
      _videoElapsedSeconds = (_videoProgress * _videoTotalSeconds).round();
    });
  }

  void _openFullscreenVideo() {
    showDialog(
      context: context,
      barrierColor: Colors.black.withValues(alpha: 0.95),
      builder: (ctx) {
        bool localPlaying = _isVideoPlaying;
        int localElapsed = _videoElapsedSeconds;
        double localProgress = _videoProgress;
        bool localMuted = _isMuted;

        return StatefulBuilder(
          builder: (context, setDialogState) {
            return Scaffold(
              backgroundColor: Colors.transparent,
              appBar: AppBar(
                backgroundColor: Colors.black54,
                elevation: 0,
                iconTheme: const IconThemeData(color: Colors.white),
                title: Text(
                  widget.product.videoTitle ?? "Video Produk",
                  style: const TextStyle(color: Colors.white, fontSize: 14),
                ),
                actions: [
                  IconButton(
                    icon: Icon(localMuted ? Icons.volume_off : Icons.volume_up, color: Colors.white),
                    onPressed: () {
                      setDialogState(() {
                        localMuted = !localMuted;
                        _isMuted = localMuted;
                      });
                      setState(() {});
                    },
                  ),
                ],
              ),
              body: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Expanded(
                      child: Stack(
                        alignment: Alignment.center,
                        children: [
                          _buildImageWidget(
                            widget.product.videoThumbnail ?? (widget.product.images.isNotEmpty ? widget.product.images[0] : ""),
                            fit: BoxFit.contain,
                          ),
                          GestureDetector(
                            onTap: () {
                              setDialogState(() {
                                localPlaying = !localPlaying;
                              });
                              _togglePlayVideo();
                            },
                            child: Container(
                              padding: const EdgeInsets.all(16),
                              decoration: BoxDecoration(
                                color: Colors.black.withValues(alpha: 0.6),
                                shape: BoxShape.circle,
                              ),
                              child: Icon(
                                localPlaying ? Icons.pause : Icons.play_arrow,
                                size: 54,
                                color: Colors.white,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    Container(
                      color: Colors.black87,
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          SliderTheme(
                            data: SliderTheme.of(context).copyWith(
                              activeTrackColor: shopeeOrange,
                              inactiveTrackColor: Colors.white24,
                              thumbColor: shopeeOrange,
                              trackHeight: 3,
                            ),
                            child: Slider(
                              value: localProgress.clamp(0.0, 1.0),
                              onChanged: (val) {
                                setDialogState(() {
                                  localProgress = val;
                                  localElapsed = (val * _videoTotalSeconds).round();
                                });
                                _seekVideo(val);
                              },
                            ),
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                _formatTime(localElapsed),
                                style: const TextStyle(color: Colors.white70, fontSize: 12),
                              ),
                              Text(
                                _formatTime(_videoTotalSeconds),
                                style: const TextStyle(color: Colors.white70, fontSize: 12),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }

  @override
  void dispose() {
    _videoTimer?.cancel();
    _imagePageController.dispose();
    super.dispose();
  }

  Widget _buildImageWidget(String path, {BoxFit fit = BoxFit.cover, double? width, double? height}) {
    if (path.isEmpty) {
      return Center(child: Icon(widget.product.icon, size: 80, color: widget.product.iconColor));
    }
    if (path.startsWith('http://') || path.startsWith('https://')) {
      return Image.network(
        path,
        fit: fit,
        width: width,
        height: height,
        loadingBuilder: (context, child, progress) {
          if (progress == null) return child;
          return const Center(child: CircularProgressIndicator(strokeWidth: 2));
        },
        errorBuilder: (context, error, stackTrace) =>
            Center(child: Icon(widget.product.icon, size: 80, color: widget.product.iconColor)),
      );
    } else {
      return Image.asset(
        path,
        fit: fit,
        width: width,
        height: height,
        errorBuilder: (context, error, stackTrace) =>
            Center(child: Icon(widget.product.icon, size: 80, color: widget.product.iconColor)),
      );
    }
  }

  void _addToCart() {
    for (int i = 0; i < _selectedQuantity; i++) {
      CartManager.addItem(
        title: widget.product.title,
        seller: widget.product.author,
        category: widget.product.category,
        price: widget.product.priceInt,
        icon: widget.product.icon,
        iconColor: widget.product.iconColor,
      );
    }
    setState(() {});

    ScaffoldMessenger.of(context).clearSnackBars();
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.check_circle, color: Colors.greenAccent, size: 20),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                "$_selectedQuantity x '${widget.product.title}' ditambahkan ke keranjang!",
                overflow: TextOverflow.ellipsis,
              ),
            ),
          ],
        ),
        action: SnackBarAction(
          label: "Lihat",
          textColor: Colors.yellowAccent,
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const KeranjangScreen()),
            ).then((_) {
              if (mounted) setState(() {});
            });
          },
        ),
        behavior: SnackBarBehavior.floating,
        duration: const Duration(seconds: 3),
      ),
    );
  }

  void _buyNow() {
    for (int i = 0; i < _selectedQuantity; i++) {
      CartManager.addItem(
        title: widget.product.title,
        seller: widget.product.author,
        category: widget.product.category,
        price: widget.product.priceInt,
        icon: widget.product.icon,
        iconColor: widget.product.iconColor,
      );
    }
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const KeranjangScreen()),
    ).then((_) {
      if (mounted) setState(() {});
    });
  }

  @override
  Widget build(BuildContext context) {
    final prod = widget.product;
    final hasVideo = prod.videoUrl != null || prod.videoThumbnail != null;
    final totalPhotos = prod.images.length;

    return Scaffold(
      backgroundColor: Colors.grey[100],
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(60),
        child: Container(
          color: darkBlue,
          padding: EdgeInsets.only(
            top: MediaQuery.of(context).padding.top + 4,
            left: 8,
            right: 12,
            bottom: 8,
          ),
          child: Row(
            children: [
              IconButton(
                icon: const Icon(Icons.arrow_back, color: Colors.white),
                onPressed: () => Navigator.pop(context),
              ),
              const Expanded(
                child: Text(
                  "Detail Produk",
                  style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                  ),
                ),
              ),
              IconButton(
                icon: Icon(
                  _isFavorite ? Icons.favorite : Icons.favorite_border,
                  color: _isFavorite ? Colors.redAccent : Colors.white,
                ),
                tooltip: "Simpan Produk",
                onPressed: () {
                  setState(() {
                    _isFavorite = !_isFavorite;
                  });
                  ScaffoldMessenger.of(context).clearSnackBars();
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text(
                        _isFavorite
                            ? "Produk ditambahkan ke daftar favorit."
                            : "Produk dihapus dari daftar favorit.",
                      ),
                      duration: const Duration(seconds: 2),
                      behavior: SnackBarBehavior.floating,
                    ),
                  );
                },
              ),
              InkWell(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const KeranjangScreen()),
                  ).then((_) {
                    if (mounted) setState(() {});
                  });
                },
                borderRadius: BorderRadius.circular(20),
                child: Padding(
                  padding: const EdgeInsets.all(4.0),
                  child: Stack(
                    children: [
                      const Icon(Icons.shopping_cart, color: Colors.white, size: 26),
                      Positioned(
                        right: 0,
                        top: 0,
                        child: Container(
                          padding: const EdgeInsets.all(2),
                          decoration: const BoxDecoration(
                            color: Colors.red,
                            shape: BoxShape.circle,
                          ),
                          constraints: const BoxConstraints(
                            minWidth: 15,
                            minHeight: 15,
                          ),
                          child: Text(
                            "${CartManager.itemCount}",
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 9,
                              fontWeight: FontWeight.bold,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
      body: ListView(
        physics: const BouncingScrollPhysics(),
        children: [
          // 1. SHOPEE-STYLE HERO MEDIA CONTAINER
          Container(
            height: 330,
            width: double.infinity,
            color: Colors.black,
            child: Stack(
              children: [
                // Media Content (Video or Image Slider)
                if (_selectedMediaType == MediaType.video && hasVideo)
                  // Video View
                  Stack(
                    alignment: Alignment.center,
                    children: [
                      // Video Thumbnail / Canvas
                      SizedBox(
                        width: double.infinity,
                        height: 330,
                        child: _buildImageWidget(
                          prod.videoThumbnail ?? (prod.images.isNotEmpty ? prod.images[0] : ""),
                          fit: BoxFit.contain,
                        ),
                      ),
                      // Overlay Dark Tint
                      Container(
                        color: Colors.black.withValues(alpha: _isVideoPlaying ? 0.15 : 0.4),
                      ),
                      // Center Play / Pause Icon Button
                      GestureDetector(
                        onTap: _togglePlayVideo,
                        child: Container(
                          padding: const EdgeInsets.all(16),
                          decoration: BoxDecoration(
                            color: shopeeOrange.withValues(alpha: 0.9),
                            shape: BoxShape.circle,
                            boxShadow: [
                              BoxShadow(
                                color: shopeeOrange.withValues(alpha: 0.4),
                                blurRadius: 16,
                                spreadRadius: 2,
                              ),
                            ],
                          ),
                          child: Icon(
                            _isVideoPlaying ? Icons.pause : Icons.play_arrow,
                            size: 46,
                            color: Colors.white,
                          ),
                        ),
                      ),
                      // Top Video Info Bar
                      Positioned(
                        top: 14,
                        left: 14,
                        right: 14,
                        child: Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                              decoration: BoxDecoration(
                                color: shopeeOrange,
                                borderRadius: BorderRadius.circular(4),
                              ),
                              child: const Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Icon(Icons.videocam, color: Colors.white, size: 14),
                                  SizedBox(width: 4),
                                  Text(
                                    "VIDEO RESMI",
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 10,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const Spacer(),
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                              decoration: BoxDecoration(
                                color: Colors.black.withValues(alpha: 0.7),
                                borderRadius: BorderRadius.circular(4),
                              ),
                              child: Text(
                                prod.videoDuration ?? "0:30",
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                      // Bottom Video Controls
                      Positioned(
                        bottom: 45,
                        left: 10,
                        right: 10,
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: Colors.black.withValues(alpha: 0.75),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            children: [
                              GestureDetector(
                                onTap: _togglePlayVideo,
                                child: Icon(
                                  _isVideoPlaying ? Icons.pause : Icons.play_arrow,
                                  color: Colors.white,
                                  size: 20,
                                ),
                              ),
                              const SizedBox(width: 8),
                              Text(
                                _formatTime(_videoElapsedSeconds),
                                style: const TextStyle(color: Colors.white, fontSize: 11),
                              ),
                              Expanded(
                                child: SliderTheme(
                                  data: SliderTheme.of(context).copyWith(
                                    activeTrackColor: shopeeOrange,
                                    inactiveTrackColor: Colors.white24,
                                    thumbColor: shopeeOrange,
                                    thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 6),
                                    trackHeight: 2.5,
                                  ),
                                  child: Slider(
                                    value: _videoProgress.clamp(0.0, 1.0),
                                    onChanged: _seekVideo,
                                  ),
                                ),
                              ),
                              Text(
                                _formatTime(_videoTotalSeconds),
                                style: const TextStyle(color: Colors.white70, fontSize: 11),
                              ),
                              const SizedBox(width: 8),
                              GestureDetector(
                                onTap: () {
                                  setState(() {
                                    _isMuted = !_isMuted;
                                  });
                                },
                                child: Icon(
                                  _isMuted ? Icons.volume_off : Icons.volume_up,
                                  color: Colors.white,
                                  size: 18,
                                ),
                              ),
                              const SizedBox(width: 8),
                              GestureDetector(
                                onTap: _openFullscreenVideo,
                                child: const Icon(
                                  Icons.fullscreen,
                                  color: Colors.white,
                                  size: 20,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ],
                  )
                else
                  // Photo Slider
                  Stack(
                    children: [
                      PageView.builder(
                        controller: _imagePageController,
                        itemCount: totalPhotos,
                        onPageChanged: (idx) {
                          setState(() {
                            _currentImageIndex = idx;
                          });
                        },
                        itemBuilder: (context, idx) {
                          return GestureDetector(
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(
                                  builder: (context) => FullscreenImageViewer(
                                    images: prod.images,
                                    initialIndex: idx,
                                    title: prod.title,
                                  ),
                                ),
                              );
                            },
                            child: Container(
                              color: Colors.grey.shade900,
                              child: Center(
                                child: _buildImageWidget(
                                  prod.images[idx],
                                  fit: BoxFit.contain,
                                  width: double.infinity,
                                  height: 330,
                                ),
                              ),
                            ),
                          );
                        },
                      ),
                      // Top badges for photos
                      Positioned(
                        top: 14,
                        left: 14,
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: Colors.white.withValues(alpha: 0.95),
                            borderRadius: BorderRadius.circular(6),
                            boxShadow: [
                              BoxShadow(color: Colors.black.withValues(alpha: 0.1), blurRadius: 4),
                            ],
                          ),
                          child: Text(
                            prod.tag,
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.bold,
                              color: prod.tagColor,
                            ),
                          ),
                        ),
                      ),
                      if (prod.isFlashSale && prod.discount != null)
                        Positioned(
                          top: 14,
                          right: 14,
                          child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                            decoration: BoxDecoration(
                              color: Colors.red,
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Text(
                              "FLASH SALE ${prod.discount}",
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ),
                      // Bottom right photo counter
                      Positioned(
                        bottom: 45,
                        right: 14,
                        child: GestureDetector(
                          onTap: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => FullscreenImageViewer(
                                  images: prod.images,
                                  initialIndex: _currentImageIndex,
                                  title: prod.title,
                                ),
                              ),
                            );
                          },
                          child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                            decoration: BoxDecoration(
                              color: Colors.black.withValues(alpha: 0.75),
                              borderRadius: BorderRadius.circular(16),
                            ),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                const Icon(Icons.fullscreen, color: Colors.white, size: 14),
                                const SizedBox(width: 4),
                                Text(
                                  "${_currentImageIndex + 1}/$totalPhotos • Buka Penuh",
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 11,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),

                // Shopee-Style Switcher Pill: [ ▶ Video ] / [ 📷 Foto ]
                Positioned(
                  bottom: 8,
                  left: 0,
                  right: 0,
                  child: Center(
                    child: Container(
                      padding: const EdgeInsets.all(3),
                      decoration: BoxDecoration(
                        color: Colors.black.withValues(alpha: 0.8),
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withValues(alpha: 0.3),
                            blurRadius: 6,
                          ),
                        ],
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          if (hasVideo)
                            GestureDetector(
                              onTap: () {
                                setState(() {
                                  _selectedMediaType = MediaType.video;
                                });
                              },
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 5),
                                decoration: BoxDecoration(
                                  color: _selectedMediaType == MediaType.video
                                      ? shopeeOrange
                                      : Colors.transparent,
                                  borderRadius: BorderRadius.circular(16),
                                ),
                                child: Row(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    const Icon(Icons.play_circle_fill, color: Colors.white, size: 14),
                                    const SizedBox(width: 4),
                                    Text(
                                      "Video (${prod.videoDuration ?? '0:30'})",
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontSize: 11,
                                        fontWeight: _selectedMediaType == MediaType.video
                                            ? FontWeight.bold
                                            : FontWeight.normal,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          GestureDetector(
                            onTap: () {
                              setState(() {
                                _selectedMediaType = MediaType.photo;
                              });
                            },
                            child: Container(
                              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 5),
                              decoration: BoxDecoration(
                                color: _selectedMediaType == MediaType.photo
                                    ? primaryBlue
                                    : Colors.transparent,
                                borderRadius: BorderRadius.circular(16),
                              ),
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  const Icon(Icons.photo_library, color: Colors.white, size: 14),
                                  const SizedBox(width: 4),
                                  Text(
                                    "Foto ($totalPhotos)",
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 11,
                                      fontWeight: _selectedMediaType == MediaType.photo
                                          ? FontWeight.bold
                                          : FontWeight.normal,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),

          // 2. SHOPEE HORIZONTAL THUMBNAIL STRIP
          Container(
            color: Colors.white,
            padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      "Galeri Media (${(hasVideo ? 1 : 0) + totalPhotos} Media)",
                      style: const TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                        color: Colors.black87,
                      ),
                    ),
                    Text(
                      _selectedMediaType == MediaType.video
                          ? "Sedang memutar video"
                          : "Foto ${_currentImageIndex + 1} dari $totalPhotos",
                      style: TextStyle(fontSize: 11, color: Colors.grey.shade600),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                SizedBox(
                  height: 64,
                  child: ListView(
                    scrollDirection: Axis.horizontal,
                    physics: const BouncingScrollPhysics(),
                    children: [
                      // Video Thumbnail
                      if (hasVideo)
                        GestureDetector(
                          onTap: () {
                            setState(() {
                              _selectedMediaType = MediaType.video;
                            });
                          },
                          child: Container(
                            width: 64,
                            height: 64,
                            margin: const EdgeInsets.only(right: 8),
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(
                                color: _selectedMediaType == MediaType.video
                                    ? shopeeOrange
                                    : Colors.grey.shade300,
                                width: _selectedMediaType == MediaType.video ? 2.5 : 1.0,
                              ),
                            ),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(6),
                              child: Stack(
                                fit: StackFit.expand,
                                children: [
                                  _buildImageWidget(
                                    prod.videoThumbnail ?? (prod.images.isNotEmpty ? prod.images[0] : ""),
                                  ),
                                  Container(color: Colors.black45),
                                  Center(
                                    child: Container(
                                      padding: const EdgeInsets.all(4),
                                      decoration: const BoxDecoration(
                                        color: Colors.red,
                                        shape: BoxShape.circle,
                                      ),
                                      child: const Icon(Icons.play_arrow, color: Colors.white, size: 16),
                                    ),
                                  ),
                                  Positioned(
                                    bottom: 2,
                                    left: 2,
                                    right: 2,
                                    child: Container(
                                      padding: const EdgeInsets.symmetric(vertical: 1),
                                      color: Colors.black87,
                                      child: Text(
                                        prod.videoDuration ?? "0:30",
                                        textAlign: TextAlign.center,
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontSize: 8,
                                          fontWeight: FontWeight.bold,
                                        ),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),

                      // Image Thumbnails (5-8 images)
                      ...List.generate(totalPhotos, (idx) {
                        final isSelected =
                            _selectedMediaType == MediaType.photo && _currentImageIndex == idx;
                        return GestureDetector(
                          onTap: () {
                            setState(() {
                              _selectedMediaType = MediaType.photo;
                              _currentImageIndex = idx;
                            });
                            if (_imagePageController.hasClients) {
                              _imagePageController.animateToPage(
                                idx,
                                duration: const Duration(milliseconds: 300),
                                curve: Curves.easeInOut,
                              );
                            }
                          },
                          child: Container(
                            width: 64,
                            height: 64,
                            margin: const EdgeInsets.only(right: 8),
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(
                                color: isSelected ? primaryBlue : Colors.grey.shade300,
                                width: isSelected ? 2.5 : 1.0,
                              ),
                            ),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(6),
                              child: Stack(
                                fit: StackFit.expand,
                                children: [
                                  _buildImageWidget(prod.images[idx]),
                                  Positioned(
                                    bottom: 2,
                                    right: 2,
                                    child: Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 1),
                                      decoration: BoxDecoration(
                                        color: Colors.black.withValues(alpha: 0.6),
                                        borderRadius: BorderRadius.circular(4),
                                      ),
                                      child: Text(
                                        "${idx + 1}",
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontSize: 9,
                                          fontWeight: FontWeight.bold,
                                        ),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        );
                      }),
                    ],
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // 3. Price and Title Card
          Container(
            color: Colors.white,
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  crossAxisAlignment: CrossAxisAlignment.baseline,
                  textBaseline: TextBaseline.alphabetic,
                  children: [
                    Text(
                      prod.price,
                      style: TextStyle(
                        color: primaryBlue,
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    if (prod.oldPrice != null) ...[
                      const SizedBox(width: 8),
                      Text(
                        prod.oldPrice!,
                        style: const TextStyle(
                          color: Colors.grey,
                          fontSize: 13,
                          decoration: TextDecoration.lineThrough,
                        ),
                      ),
                    ],
                    if (prod.discount != null) ...[
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: Colors.red.shade50,
                          borderRadius: BorderRadius.circular(4),
                          border: Border.all(color: Colors.red.shade200),
                        ),
                        child: Text(
                          prod.discount!,
                          style: TextStyle(
                            color: Colors.red.shade700,
                            fontSize: 11,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  prod.title,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                    height: 1.3,
                  ),
                ),
                const SizedBox(height: 8),
                Row(
                  children: [
                    const Icon(Icons.star, color: Colors.amber, size: 16),
                    const SizedBox(width: 4),
                    Text(
                      "${prod.rating}",
                      style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                    ),
                    Text(
                      " (${prod.reviews} ulasan)",
                      style: const TextStyle(fontSize: 12, color: Colors.grey),
                    ),
                    const SizedBox(width: 12),
                    const Text("•", style: TextStyle(color: Colors.grey)),
                    const SizedBox(width: 12),
                    Text(
                      "${prod.reviews * 2}+ Terjual",
                      style: const TextStyle(fontSize: 12, color: Colors.grey),
                    ),
                    const SizedBox(width: 12),
                    const Text("•", style: TextStyle(color: Colors.grey)),
                    const SizedBox(width: 12),
                    const Text(
                      "Stok Tersedia",
                      style: TextStyle(fontSize: 12, color: Colors.green, fontWeight: FontWeight.w600),
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // 4. Campus Seller Info Card
          Container(
            color: Colors.white,
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            child: Row(
              children: [
                CircleAvatar(
                  radius: 22,
                  backgroundColor: darkBlue.withValues(alpha: 0.1),
                  child: Icon(Icons.school, color: darkBlue, size: 24),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Flexible(
                            child: Text(
                              prod.author,
                              style: const TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.bold,
                              ),
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                          const SizedBox(width: 4),
                          const Icon(Icons.verified, color: Colors.blue, size: 14),
                        ],
                      ),
                      const SizedBox(height: 2),
                      const Text(
                        "Civitas Akademika IAKN Ambon",
                        style: TextStyle(fontSize: 11, color: Colors.grey),
                      ),
                    ],
                  ),
                ),
                OutlinedButton(
                  onPressed: () {
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text("Membuka profil civitas: ${prod.author}"),
                        duration: const Duration(seconds: 2),
                      ),
                    );
                  },
                  style: OutlinedButton.styleFrom(
                    foregroundColor: primaryBlue,
                    side: BorderSide(color: primaryBlue),
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    minimumSize: Size.zero,
                    tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6)),
                  ),
                  child: const Text("Kunjungi", style: TextStyle(fontSize: 11)),
                ),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // 5. Specifications & Details Table
          Container(
            color: Colors.white,
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "Spesifikasi & Informasi",
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 12),
                _buildSpecRow("Kategori", prod.category),
                _buildSpecRow("Jumlah Media", "${(hasVideo ? 1 : 0) + totalPhotos} (1 Video + $totalPhotos Foto)"),
                _buildSpecRow("Kondisi", "Baru (Orisinal 100%)"),
                _buildSpecRow("Penjamin Mutu", "Lembaga Akademik IAKN Ambon"),
                _buildSpecRow("Pengambilan", "Gratis di Auditorium / Koperasi Kampus"),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // 6. Product Description
          Container(
            color: Colors.white,
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "Deskripsi Produk",
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 8),
                Text(
                  prod.description ??
                      "Produk resmi civitas akademika Institut Agama Kristen Negeri (IAKN) Ambon. Dikerjakan dengan dedikasi tinggi, mengedepankan kualitas, nilai etika kristiani, dan pelestarian seni budaya nusantara.",
                  style: const TextStyle(fontSize: 12, height: 1.6, color: Colors.black87),
                ),
                const SizedBox(height: 12),
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: primaryBlue.withValues(alpha: 0.05),
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: primaryBlue.withValues(alpha: 0.15)),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.volunteer_activism, color: primaryBlue, size: 22),
                      const SizedBox(width: 10),
                      const Expanded(
                        child: Text(
                          "Setiap transaksi mendukung langsung dana beasiswa dan riset kreatif mahasiswa IAKN Ambon.",
                          style: TextStyle(fontSize: 11, color: Colors.black87),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // 7. Quantity Selector Section
          Container(
            color: Colors.white,
            padding: const EdgeInsets.all(16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  "Jumlah Pesanan",
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                Row(
                  children: [
                    InkWell(
                      onTap: () {
                        if (_selectedQuantity > 1) {
                          setState(() {
                            _selectedQuantity--;
                          });
                        }
                      },
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          border: Border.all(color: Colors.grey.shade300),
                          borderRadius: BorderRadius.circular(4),
                        ),
                        child: const Icon(Icons.remove, size: 14),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 14),
                      child: Text(
                        "$_selectedQuantity",
                        style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                      ),
                    ),
                    InkWell(
                      onTap: () {
                        setState(() {
                          _selectedQuantity++;
                        });
                      },
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          border: Border.all(color: Colors.grey.shade300),
                          borderRadius: BorderRadius.circular(4),
                        ),
                        child: const Icon(Icons.add, size: 14),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 100), // padding for bottom bar
        ],
      ),
      bottomSheet: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
        decoration: BoxDecoration(
          color: Colors.white,
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.08),
              blurRadius: 10,
              offset: const Offset(0, -3),
            ),
          ],
        ),
        child: SafeArea(
          child: Row(
            children: [
              // Chat Button
              InkWell(
                onTap: () {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text("Membuka chat interaktif dengan ${prod.author}"),
                      duration: const Duration(seconds: 2),
                    ),
                  );
                },
                child: Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.grey.shade100,
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: Colors.grey.shade300),
                  ),
                  child: Icon(Icons.chat_bubble_outline, color: primaryBlue, size: 20),
                ),
              ),
              const SizedBox(width: 8),

              // Add to Cart Button
              Expanded(
                flex: 1,
                child: OutlinedButton.icon(
                  onPressed: _addToCart,
                  icon: const Icon(Icons.add_shopping_cart, size: 16),
                  label: const Text(
                    "+ Keranjang",
                    style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                  ),
                  style: OutlinedButton.styleFrom(
                    foregroundColor: primaryBlue,
                    side: BorderSide(color: primaryBlue),
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                  ),
                ),
              ),
              const SizedBox(width: 8),

              // Buy Now Button
              Expanded(
                flex: 1,
                child: ElevatedButton(
                  onPressed: _buyNow,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: shopeeOrange,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                  ),
                  child: const Text(
                    "Beli Sekarang",
                    style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildSpecRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 120,
            child: Text(
              label,
              style: const TextStyle(fontSize: 11, color: Colors.grey),
            ),
          ),
          Expanded(
            child: Text(
              value,
              style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w600),
            ),
          ),
        ],
      ),
    );
  }
}
