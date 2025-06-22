#Assignment operators
a=int(input())
b=int(input())
a +=b
print(a)
a -=b
print(a)
a *=b
print(a)
a /=b
print(a)
a %=b
print(a)
a //=b
print(a)
a **=b
print(a)
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SVIET - Sri Vasavi Institute</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }
    body { line-height: 1.6; background: #f4f4f4; }

    header {
      background-color: #004080;
      color: white;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 40px;
      flex-wrap: wrap;
    }

    .logo {
      font-size: 24px;
      font-weight: bold;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin-left: 20px;
      font-size: 16px;
    }

    .hero {
      background: url('https://www.sviet.edu.in/wp-content/uploads/2023/05/Untitled-design-3.png') center/cover no-repeat;
      height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      color: white;
      position: relative;
    }

    .hero::after {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.5);
    }

    .hero-text {
      position: relative;
      z-index: 1;
    }

    .hero-text h1 {
      font-size: 36px;
      margin-bottom: 10px;
    }

    .hero-text p {
      font-size: 18px;
    }

    section {
      padding: 40px 20px;
      max-width: 1000px;
      margin: auto;
      background: white;
      margin-bottom: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    section h2 {
      margin-bottom: 20px;
      color: #004080;
    }

    footer {
      background-color: #004080;
      color: white;
      text-align: center;
      padding: 15px;
    }

    @media (max-width: 768px) {
      header {
        flex-direction: column;
        text-align: center;
      }

      nav {
        margin-top: 10px;
      }

      .hero-text h1 {
        font-size: 28px;
      }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="logo">SVIET College</div>
    <nav>
      <a href="#about">About</a>
      <a href="#courses">Courses</a>
      <a href="#admission">Admissions</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <!-- Hero Banner -->
  <section class="hero">
    <div class="hero-text">
      <h1>Welcome to SVIET</h1>
      <p>Empowering Future Engineers & Leaders</p>
    </div>
  </section>

  <!-- About Section -->
  <section id="about">
    <h2>About Us</h2>
    <p>SVIET (Sri Vasavi Institute of Engineering & Technology) is a premier institution offering top-quality engineering education with a focus on innovation, research, and industry collaboration. Our mission is to shape students into global professionals and responsible citizens.</p>
  </section>

  <!-- Courses Section -->
  <section id="courses">
    <h2>Courses Offered</h2>
    <ul>
      <li>B.Tech - CSE, ECE, EEE, Mechanical, Civil</li>
      <li>M.Tech - AI, VLSI, Power Systems</li>
      <li>MBA - Business Administration</li>
    </ul>
  </section>

  <!-- Admission Section -->
  <section id="admission">
    <h2>Admissions</h2>
    <p>Admissions are open for the academic year 2025-26. Apply now through AP EAMCET or directly under management quota. Scholarships are available for eligible students. Visit our campus to learn more about facilities and programs.</p>
  </section>

  <!-- Contact Section -->
  <section id="contact">
    <h2>Contact Us</h2>
    <p><strong>Address:</strong> Sri Vasavi Institute of Engineering & Technology, Nandamuru, Krishna District, Andhra Pradesh</p>
    <p><strong>Phone:</strong> +91-8676-297000</p>
    <p><strong>Email:</strong> info@sviet.edu.in</p>
  </section>

  <!-- Footer -->
  <footer>
    <p>&copy; 2025 SVIET College. All rights reserved.</p>
  </footer>

</body>
</html>
