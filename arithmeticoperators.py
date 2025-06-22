#Arithmetic operators
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>AJIO Clone</title>
  <style>
    * {
      margin: 0; padding: 0; box-sizing: border-box;
      font-family: 'Segoe UI', sans-serif;
    }

    body { background-color: #fff; color: #333; }

    /* Header */
    header {
      background-color: #1c1c1c;
      color: white;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 30px;
      flex-wrap: wrap;
    }

    .logo {
      font-size: 28px;
      font-weight: bold;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin-left: 20px;
      font-size: 16px;
    }

    .search-bar {
      margin-top: 10px;
      flex: 1;
      text-align: center;
    }

    .search-bar input {
      padding: 8px 12px;
      width: 60%;
      max-width: 400px;
      border-radius: 20px;
      border: none;
      outline: none;
    }

    /* Carousel */
    .carousel {
      position: relative;
      width: 100%;
      height: 400px;
      overflow: hidden;
    }

    .slides {
      display: flex;
      width: 300%;
      height: 100%;
      animation: slide 12s infinite;
    }

    .slide {
      width: 100%;
      flex-shrink: 0;
      height: 100%;
    }

    .slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    @keyframes slide {
      0% { transform: translateX(0%); }
      33% { transform: translateX(-100%); }
      66% { transform: translateX(-200%); }
      100% { transform: translateX(0%); }
    }

    /* Categories */
    .categories {
      padding: 40px 20px;
      text-align: center;
    }

    .categories h2 {
      margin-bottom: 20px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 20px;
    }

    .grid img {
      width: 100%;
      border-radius: 10px;
      transition: transform 0.3s ease;
    }

    .grid img:hover {
      transform: scale(1.05);
    }

    /* Products */
    .products {
      padding: 40px 20px;
    }

    .products h2 {
      text-align: center;
      margin-bottom: 30px;
    }

    .product-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
    }

    .product {
      border: 1px solid #eee;
      width: 200px;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 2px 5px rgba(0,0,0,0.05);
      transition: 0.3s;
    }

    .product img {
      width: 100%;
      height: 220px;
      object-fit: cover;
    }

    .product h4 {
      padding: 10px;
      font-size: 16px;
    }

    .product p {
      padding: 0 10px 10px;
      color: #ff5e00;
      font-weight: bold;
    }

    /* Footer */
    footer {
      background-color: #1c1c1c;
      color: white;
      text-align: center;
      padding: 20px;
      margin-top: 40px;
    }

    @media(max-width: 768px) {
      header {
        flex-direction: column;
        text-align: center;
      }

      nav {
        margin-top: 10px;
      }

      .search-bar {
        margin-top: 10px;
      }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="logo">AJIO</div>
    <nav>
      <a href="#">Men</a>
      <a href="#">Women</a>
      <a href="#">Kids</a>
      <a href="#">Sale</a>
    </nav>
    <div class="search-bar">
      <input type="text" placeholder="Search for brands, products..." />
    </div>
  </header>

  <!-- Hero Carousel -->
  <div class="carousel">
    <div class="slides">
      <div class="slide">
        <img src="https://assets.ajio.com/cms/AJIO/WEB/23062024-D-unisex-topbanner-dnmxflat65.jpg" alt="Banner 1">
      </div>
      <div class="slide">
        <img src="https://assets.ajio.com/cms/AJIO/WEB/23062024-D-unisex-topbanner-superdry-upto50.jpg" alt="Banner 2">
      </div>
      <div class="slide">
        <img src="https://assets.ajio.com/cms/AJIO/WEB/23062024-D-unisex-topbanner-lee-upto50.jpg" alt="Banner 3">
      </div>
    </div>
  </div>

  <!-- Categories -->
  <section class="categories">
    <h2>Shop by Category</h2>
    <div class="grid">
      <img src="https://assets.ajio.com/cms/AJIO/WEB/23062024-D-unisex-brands-uspolo.jpg" alt="Category 1" />
      <img src="https://assets.ajio.com/cms/AJIO/WEB/23062024-D-unisex-brands-leecooper.jpg" alt="Category 2" />
      <img src="https://assets.ajio.com/cms/AJIO/WEB/23062024-D-unisex-brands-redtape.jpg" alt="Category 3" />
    </div>
  </section>

  <!-- Products -->
  <section class="products">
    <h2>Trending Products</h2>
    <div class="product-grid">
      <div class="product">
        <img src="https://assets.ajio.com/medias/sys_master/root/20240321/SyaB/65fb9ea505ac7d77bbfcfd34/-473Wx593H-466925131-grey-MODEL.jpg" alt="Product 1">
        <h4>Men's Sneakers</h4>
        <p>₹1,299</p>
      </div>
      <div class="product">
        <img src="https://assets.ajio.com/medias/sys_master/root/20240321/B02Y/65fb9b9305ac7d77bbfcf24d/-473Wx593H-466925093-black-MODEL.jpg" alt="Product 2">
        <h4>Casual Shoes</h4>
        <p>₹1,999</p>
      </div>
      <div class="product">
        <img src="https://assets.ajio.com/medias/sys_master/root/20240314/G5lK/65f2fcad05ac7d77bbf16ef4/-473Wx593H-466861039-black-MODEL.jpg" alt="Product 3">
        <h4>Women Handbag</h4>
        <p>₹899</p>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <p>&copy; 2025 AJIO Clone | Designed for Educational Purpose</p>
  </footer>

</body>
</html>
