import streamlit as st

st.set_page_config(
    page_title="Diego Kurilo | Architect",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Global CSS ──────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0d0d0d;
    color: #e8e8e8;
}

/* Remove default Streamlit padding */
.block-container { padding: 0 !important; max-width: 100% !important; }
header { visibility: hidden; }
footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Navbar ──────────────────────────────────────────────────── */
.navbar {
    position: fixed; top: 0; left: 0; width: 100%; z-index: 9999;
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 60px;
    background: rgba(13,13,13,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.navbar-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem; font-weight: 700;
    letter-spacing: 2px; color: #fff; text-transform: uppercase;
}
.navbar-links { display: flex; gap: 40px; }
.navbar-links a {
    color: #aaa; text-decoration: none; font-size: 0.78rem;
    letter-spacing: 2px; text-transform: uppercase; font-weight: 500;
    transition: color 0.3s;
}
.navbar-links a:hover { color: #fff; }

/* ── Hero ────────────────────────────────────────────────────── */
.hero {
    height: 100vh;
    background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 50%, #0d0d0d 100%);
    display: flex; flex-direction: column;
    justify-content: center; align-items: flex-start;
    padding: 0 10vw;
    position: relative; overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: 0; right: 0;
    width: 45%; height: 100%;
    background: linear-gradient(135deg, transparent 0%, rgba(180,160,120,0.04) 100%);
    border-left: 1px solid rgba(255,255,255,0.04);
}
.hero-tag {
    font-size: 0.72rem; letter-spacing: 4px; text-transform: uppercase;
    color: #b4a078; margin-bottom: 24px; font-weight: 500;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 7vw, 6.5rem);
    font-weight: 700; line-height: 1.05;
    color: #ffffff; margin: 0 0 8px 0;
}
.hero-title-italic {
    font-family: 'Playfair Display', serif;
    font-style: italic; color: #b4a078;
}
.hero-subtitle {
    font-size: 0.9rem; color: #666; letter-spacing: 1px;
    max-width: 480px; line-height: 1.8; margin-top: 28px;
}
.hero-line {
    width: 60px; height: 1px; background: #b4a078;
    margin: 32px 0;
}
.hero-scroll {
    font-size: 0.68rem; letter-spacing: 3px; text-transform: uppercase;
    color: #555; position: absolute; bottom: 40px; left: 10vw;
}
.hero-year {
    position: absolute; right: 10vw; bottom: 40px;
    font-family: 'Playfair Display', serif; font-size: 6rem;
    color: rgba(255,255,255,0.03); font-weight: 700; line-height: 1;
    user-select: none;
}

/* ── Section shared ──────────────────────────────────────────── */
.section {
    padding: 100px 10vw;
}
.section-alt { background: #111; }
.section-tag {
    font-size: 0.68rem; letter-spacing: 4px; text-transform: uppercase;
    color: #b4a078; margin-bottom: 16px; font-weight: 500;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-weight: 700; color: #fff; margin: 0 0 20px 0; line-height: 1.2;
}
.section-divider {
    width: 50px; height: 1px; background: #b4a078; margin-bottom: 48px;
}
.section-body {
    font-size: 0.9rem; color: #888; line-height: 1.9; max-width: 600px;
}

/* ── Project grid ────────────────────────────────────────────── */
.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2px;
    margin-top: 60px;
}
.project-card {
    position: relative; overflow: hidden; aspect-ratio: 4/3;
    background: #1a1a1a; cursor: pointer;
}
.project-card-render {
    width: 100%; height: 100%; object-fit: cover;
    transition: transform 0.6s ease;
}
.project-card:hover .project-card-render { transform: scale(1.05); }
.project-card-overlay {
    position: absolute; bottom: 0; left: 0; width: 100%;
    padding: 30px 24px 24px;
    background: linear-gradient(transparent, rgba(0,0,0,0.88));
    transform: translateY(10px); transition: transform 0.4s ease;
}
.project-card:hover .project-card-overlay { transform: translateY(0); }
.project-card-label {
    font-size: 0.6rem; letter-spacing: 3px; text-transform: uppercase;
    color: #b4a078; margin-bottom: 6px;
}
.project-card-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem; color: #fff; margin: 0;
}
.project-card-loc {
    font-size: 0.75rem; color: #888; margin-top: 4px; letter-spacing: 1px;
}

/* ── Floor plan section ──────────────────────────────────────── */
.plan-tabs {
    display: flex; gap: 0; margin-bottom: 48px; border-bottom: 1px solid #222;
}
.plan-tab {
    padding: 14px 28px; font-size: 0.75rem; letter-spacing: 2px;
    text-transform: uppercase; color: #555; cursor: pointer;
    border-bottom: 2px solid transparent; transition: all 0.3s;
}
.plan-tab.active { color: #b4a078; border-bottom-color: #b4a078; }
.plan-container {
    background: #f5f0e8; border-radius: 2px;
    padding: 40px; display: flex; justify-content: center;
}

/* ── Services ────────────────────────────────────────────────── */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 40px; margin-top: 60px;
}
.service-card {
    border-top: 1px solid #222; padding-top: 28px;
}
.service-number {
    font-family: 'Playfair Display', serif;
    font-size: 2rem; color: rgba(180,160,120,0.25);
    line-height: 1; margin-bottom: 16px;
}
.service-name {
    font-size: 0.85rem; font-weight: 600; color: #ddd;
    letter-spacing: 1px; margin-bottom: 12px;
    text-transform: uppercase;
}
.service-desc { font-size: 0.8rem; color: #666; line-height: 1.8; }

/* ── Stats bar ───────────────────────────────────────────────── */
.stats-bar {
    display: flex; flex-wrap: wrap; gap: 0;
    border-top: 1px solid #222; border-bottom: 1px solid #222;
    margin: 80px 0;
}
.stat-item {
    flex: 1; min-width: 160px;
    padding: 40px 32px; border-right: 1px solid #222;
    text-align: center;
}
.stat-item:last-child { border-right: none; }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 3rem; color: #fff; line-height: 1;
}
.stat-label {
    font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase;
    color: #555; margin-top: 8px;
}

/* ── About ───────────────────────────────────────────────────── */
.about-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 80px;
    align-items: center;
}
.about-image-placeholder {
    background: linear-gradient(135deg, #1a1a1a, #252525);
    aspect-ratio: 3/4; border: 1px solid #222;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.7rem; color: #333; letter-spacing: 2px; text-transform: uppercase;
}
.about-text p { font-size: 0.88rem; color: #777; line-height: 1.9; margin-bottom: 20px; }
.about-credentials { margin-top: 40px; }
.credential-item {
    display: flex; gap: 20px; align-items: flex-start;
    padding: 16px 0; border-bottom: 1px solid #1a1a1a;
}
.credential-year {
    font-size: 0.7rem; color: #b4a078; letter-spacing: 1px;
    min-width: 50px; padding-top: 2px;
}
.credential-text { font-size: 0.82rem; color: #aaa; line-height: 1.6; }

/* ── Contact ─────────────────────────────────────────────────── */
.contact-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 80px;
    margin-top: 60px;
}
.contact-info-item { margin-bottom: 40px; }
.contact-info-label {
    font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase;
    color: #b4a078; margin-bottom: 8px;
}
.contact-info-value { font-size: 1rem; color: #ccc; }
.contact-form input, .contact-form textarea {
    width: 100%; background: transparent;
    border: none; border-bottom: 1px solid #222;
    padding: 14px 0; color: #ccc; font-family: 'Inter', sans-serif;
    font-size: 0.85rem; outline: none; transition: border-color 0.3s;
    margin-bottom: 28px;
}
.contact-form input:focus,
.contact-form textarea:focus { border-bottom-color: #b4a078; }
.contact-form textarea { min-height: 100px; resize: vertical; }
.btn-send {
    background: transparent; border: 1px solid #b4a078;
    color: #b4a078; padding: 14px 40px; font-size: 0.72rem;
    letter-spacing: 3px; text-transform: uppercase; cursor: pointer;
    transition: all 0.3s;
}
.btn-send:hover { background: #b4a078; color: #0d0d0d; }

/* ── Footer ──────────────────────────────────────────────────── */
.footer {
    padding: 40px 10vw;
    display: flex; justify-content: space-between; align-items: center;
    border-top: 1px solid #1a1a1a;
}
.footer-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1rem; color: #444; letter-spacing: 2px;
}
.footer-copy { font-size: 0.72rem; color: #333; }
</style>
""",
    unsafe_allow_html=True,
)

# ─── Navigation ──────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="navbar">
  <div class="navbar-brand">Diego Kurilo</div>
  <div class="navbar-links">
    <a href="#work">Work</a>
    <a href="#plans">Plans</a>
    <a href="#services">Services</a>
    <a href="#about">About</a>
    <a href="#contact">Contact</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Hero ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="hero" id="home">
  <div class="hero-tag">Architecture &amp; Design Studio</div>
  <h1 class="hero-title">
    Building<br>
    <span class="hero-title-italic">timeless</span><br>
    spaces.
  </h1>
  <div class="hero-line"></div>
  <p class="hero-subtitle">
    Diego Kurilo Architecture crafts environments that balance
    structural precision with human experience — where every line,
    material, and proportion serves a purpose.
  </p>
  <div class="hero-scroll">Scroll to explore</div>
  <div class="hero-year">DK</div>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Stats bar ────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="section" id="stats" style="padding-top:40px;padding-bottom:40px;">
  <div class="stats-bar">
    <div class="stat-item">
      <div class="stat-num">18+</div>
      <div class="stat-label">Years of Practice</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">64</div>
      <div class="stat-label">Projects Completed</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">12</div>
      <div class="stat-label">Awards &amp; Honours</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">9</div>
      <div class="stat-label">Countries</div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Work / Portfolio ─────────────────────────────────────────────────────────
st.markdown('<div class="section" id="work">', unsafe_allow_html=True)
st.markdown(
    """
  <div class="section-tag">Selected Work</div>
  <h2 class="section-title">Projects &amp; Renders</h2>
  <div class="section-divider"></div>
  <p class="section-body">
    A curated selection of residential, cultural, and commercial projects
    that define the studio's approach to contemporary architecture.
  </p>
""",
    unsafe_allow_html=True,
)

# Project renders using SVG placeholders
projects = [
    {
        "label": "Residential · 2023",
        "name": "Casa Ventana",
        "location": "Buenos Aires, Argentina",
        "svg_gradient": "linear-gradient(135deg,#1c2b1e,#2a3d2c)",
        "svg_lines": [
            '<rect x="20" y="120" width="260" height="120" fill="rgba(255,255,255,0.06)" rx="1"/>',
            '<rect x="60" y="100" width="80" height="140" fill="rgba(255,255,255,0.04)" rx="1"/>',
            '<rect x="160" y="108" width="100" height="132" fill="rgba(255,255,255,0.05)" rx="1"/>',
            '<rect x="80" y="80" width="40" height="44" fill="rgba(255,255,255,0.08)" rx="1"/>',
            '<line x1="0" y1="240" x2="300" y2="240" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>',
        ],
    },
    {
        "label": "Cultural · 2022",
        "name": "Palacio de la Luz",
        "location": "Montevideo, Uruguay",
        "svg_gradient": "linear-gradient(135deg,#1a1e2b,#252d40)",
        "svg_lines": [
            '<rect x="30" y="60" width="240" height="180" fill="rgba(255,255,255,0.04)" rx="1"/>',
            '<rect x="30" y="60" width="240" height="40" fill="rgba(255,255,255,0.06)" rx="1"/>',
            '<line x1="80" y1="60" x2="80" y2="240" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>',
            '<line x1="150" y1="60" x2="150" y2="240" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>',
            '<line x1="220" y1="60" x2="220" y2="240" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>',
            '<rect x="100" y="180" width="100" height="60" fill="rgba(255,255,255,0.07)" rx="1"/>',
        ],
    },
    {
        "label": "Commercial · 2024",
        "name": "Torre Blanca",
        "location": "São Paulo, Brazil",
        "svg_gradient": "linear-gradient(135deg,#201818,#2d2020)",
        "svg_lines": [
            '<rect x="110" y="20" width="80" height="220" fill="rgba(255,255,255,0.05)" rx="1"/>',
            '<rect x="110" y="20" width="80" height="220" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1" rx="1"/>',
            '<line x1="110" y1="60" x2="190" y2="60" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>',
            '<line x1="110" y1="100" x2="190" y2="100" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>',
            '<line x1="110" y1="140" x2="190" y2="140" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>',
            '<line x1="110" y1="180" x2="190" y2="180" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>',
            '<rect x="70" y="200" width="160" height="40" fill="rgba(255,255,255,0.07)" rx="1"/>',
        ],
    },
    {
        "label": "Residential · 2021",
        "name": "Villa Serra",
        "location": "Bariloche, Argentina",
        "svg_gradient": "linear-gradient(135deg,#1f2018,#2c2d1a)",
        "svg_lines": [
            '<polygon points="20,220 150,80 280,220" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>',
            '<rect x="60" y="160" width="180" height="60" fill="rgba(255,255,255,0.06)" rx="1"/>',
            '<rect x="110" y="175" width="40" height="45" fill="rgba(255,255,255,0.08)" rx="1"/>',
            '<line x1="0" y1="220" x2="300" y2="220" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>',
        ],
    },
    {
        "label": "Public · 2023",
        "name": "Centro Cívico Norte",
        "location": "Córdoba, Argentina",
        "svg_gradient": "linear-gradient(135deg,#18202b,#1e2a38)",
        "svg_lines": [
            '<rect x="20" y="80" width="120" height="160" fill="rgba(255,255,255,0.05)" rx="1"/>',
            '<rect x="160" y="100" width="120" height="140" fill="rgba(255,255,255,0.04)" rx="1"/>',
            '<rect x="80" y="60" width="140" height="30" fill="rgba(255,255,255,0.07)" rx="1"/>',
            '<line x1="0" y1="240" x2="300" y2="240" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>',
            '<rect x="130" y="170" width="40" height="70" fill="rgba(255,255,255,0.09)" rx="1"/>',
        ],
    },
    {
        "label": "Interior · 2024",
        "name": "Atelier Kurilo",
        "location": "Rosario, Argentina",
        "svg_gradient": "linear-gradient(135deg,#201a18,#2d2520)",
        "svg_lines": [
            '<rect x="20" y="40" width="260" height="200" fill="rgba(255,255,255,0.03)" rx="1"/>',
            '<line x1="20" y1="120" x2="280" y2="120" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>',
            '<rect x="40" y="130" width="80" height="80" fill="rgba(255,255,255,0.07)" rx="1"/>',
            '<rect x="180" y="50" width="80" height="60" fill="rgba(255,255,255,0.06)" rx="1"/>',
            '<line x1="180" y1="40" x2="180" y2="240" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>',
        ],
    },
]

cards_html = '<div class="project-grid" style="margin-top:60px;">'
for p in projects:
    inner = "".join(p["svg_lines"])
    cards_html += f"""
<div class="project-card">
  <svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg"
       style="width:100%;height:100%;background:{p['svg_gradient']};">
    {inner}
    <text x="150" y="136" text-anchor="middle" font-family="Georgia,serif"
          font-size="11" fill="rgba(180,160,120,0.3)" letter-spacing="4">RENDER</text>
  </svg>
  <div class="project-card-overlay">
    <div class="project-card-label">{p['label']}</div>
    <h3 class="project-card-name">{p['name']}</h3>
    <div class="project-card-loc">{p['location']}</div>
  </div>
</div>"""
cards_html += "</div>"

st.markdown(cards_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ─── Floor Plans ──────────────────────────────────────────────────────────────
st.markdown('<div class="section section-alt" id="plans">', unsafe_allow_html=True)
st.markdown(
    """
  <div class="section-tag">Technical Drawings</div>
  <h2 class="section-title">Architectural Floor Plans</h2>
  <div class="section-divider"></div>
  <p class="section-body">
    Precision-drafted plans documenting spatial organisation, structural
    layout, and material strategy across residential and commercial typologies.
  </p>
""",
    unsafe_allow_html=True,
)

plan_choice = st.selectbox(
    "Select project",
    ["Casa Ventana — Ground Floor", "Casa Ventana — First Floor", "Villa Serra — Ground Floor", "Torre Blanca — Typical Floor"],
    label_visibility="collapsed",
)

# ── Floor plan SVG definitions ─────────────────────────────────────────────
plans = {
    "Casa Ventana — Ground Floor": """
<svg viewBox="0 0 720 520" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;max-width:720px;background:#f5f0e8;font-family:Inter,sans-serif;">

  <!-- North arrow -->
  <g transform="translate(666,40)">
    <circle cx="0" cy="0" r="16" fill="none" stroke="#333" stroke-width="1"/>
    <polygon points="0,-12 -5,8 0,4 5,8" fill="#333"/>
    <text x="0" y="28" text-anchor="middle" font-size="9" fill="#333">N</text>
  </g>

  <!-- Scale bar -->
  <g transform="translate(40,480)">
    <line x1="0" y1="0" x2="120" y2="0" stroke="#333" stroke-width="1"/>
    <line x1="0" y1="-4" x2="0" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="60" y1="-4" x2="60" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="120" y1="-4" x2="120" y2="4" stroke="#333" stroke-width="1"/>
    <text x="0" y="-8" font-size="7" fill="#555">0</text>
    <text x="56" y="-8" font-size="7" fill="#555">3m</text>
    <text x="112" y="-8" font-size="7" fill="#555">6m</text>
  </g>

  <!-- Outer walls -->
  <rect x="80" y="60" width="560" height="380" fill="#e8e2d6" stroke="#222" stroke-width="3"/>

  <!-- Interior walls -->
  <!-- Vertical divider -->
  <rect x="310" y="60" width="8" height="220" fill="#222"/>
  <!-- Horizontal mid divider -->
  <rect x="80" y="200" width="238" height="6" fill="#222"/>
  <!-- Right wing vertical -->
  <rect x="480" y="60" width="6" height="180" fill="#222"/>
  <!-- Lower horizontal -->
  <rect x="80" y="340" width="398" height="6" fill="#222"/>
  <!-- Bathroom partition -->
  <rect x="310" y="300" width="6" height="140" fill="#222"/>
  <!-- Bathroom horizontal -->
  <rect x="310" y="300" width="170" height="6" fill="#222"/>

  <!-- Rooms labels -->
  <text x="185" y="140" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">LIVING ROOM</text>
  <text x="185" y="155" text-anchor="middle" font-size="8" fill="#777">42 m²</text>

  <text x="185" y="270" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">KITCHEN</text>
  <text x="185" y="285" text-anchor="middle" font-size="8" fill="#777">18 m²</text>

  <text x="415" y="130" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">MASTER BED</text>
  <text x="415" y="145" text-anchor="middle" font-size="8" fill="#777">28 m²</text>

  <text x="575" y="130" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">BEDROOM 2</text>
  <text x="575" y="145" text-anchor="middle" font-size="8" fill="#777">22 m²</text>

  <text x="415" y="365" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">DINING ROOM</text>
  <text x="415" y="380" text-anchor="middle" font-size="8" fill="#777">24 m²</text>

  <text x="393" y="345" text-anchor="middle" font-size="9" fill="#444" letter-spacing="1">BATHROOM</text>
  <text x="393" y="358" text-anchor="middle" font-size="8" fill="#777">8 m²</text>

  <!-- Doors (arcs) -->
  <g stroke="#333" stroke-width="1" fill="none">
    <!-- Entry door -->
    <line x1="170" y1="440" x2="230" y2="440" stroke="#222" stroke-width="3"/>
    <path d="M 170 440 Q 200 410 230 440" stroke="#555" stroke-width="0.8" stroke-dasharray="3,2"/>
    <!-- Living to kitchen -->
    <line x1="80" y1="200" x2="80" y2="240" stroke="#f5f0e8" stroke-width="4"/>
    <path d="M 80 200 Q 120 200 120 240" stroke="#555" stroke-width="0.8" stroke-dasharray="3,2"/>
    <!-- Master bed door -->
    <line x1="310" y1="160" x2="310" y2="200" stroke="#f5f0e8" stroke-width="4"/>
    <path d="M 310 160 Q 350 160 350 200" stroke="#555" stroke-width="0.8" stroke-dasharray="3,2"/>
    <!-- Bathroom door -->
    <line x1="310" y1="340" x2="350" y2="340" stroke="#f5f0e8" stroke-width="4"/>
    <path d="M 310 340 Q 310 370 350 370" stroke="#555" stroke-width="0.8" stroke-dasharray="3,2"/>
  </g>

  <!-- Windows -->
  <g fill="#b4c8d0" stroke="#333" stroke-width="0.8">
    <!-- South facade windows -->
    <rect x="100" y="438" width="60" height="4"/>
    <rect x="260" y="438" width="80" height="4"/>
    <rect x="440" y="438" width="60" height="4"/>
    <!-- North facade windows -->
    <rect x="110" y="58" width="60" height="4"/>
    <rect x="340" y="58" width="80" height="4"/>
    <rect x="500" y="58" width="60" height="4"/>
    <!-- West facade windows -->
    <rect x="78" y="90" width="4" height="50"/>
    <rect x="78" y="260" width="4" height="50"/>
    <!-- East facade windows -->
    <rect x="638" y="90" width="4" height="50"/>
    <rect x="638" y="260" width="4" height="50"/>
  </g>

  <!-- Furniture — living -->
  <g opacity="0.45" stroke="#666" stroke-width="0.8" fill="#ccc8bc">
    <!-- Sofa -->
    <rect x="100" y="85" width="120" height="40" rx="3"/>
    <rect x="100" y="85" width="120" height="10" rx="2" fill="#bbb8ac"/>
    <!-- Coffee table -->
    <rect x="130" y="140" width="60" height="40" rx="2" fill="#ddd8cc"/>
    <!-- Armchair -->
    <rect x="240" y="100" width="40" height="40" rx="3"/>
  </g>

  <!-- Furniture — kitchen -->
  <g opacity="0.45" stroke="#666" stroke-width="0.8" fill="#ccc8bc">
    <rect x="90" y="215" width="130" height="22" rx="2"/>
    <rect x="90" y="215" width="22" height="22" rx="2" fill="#bbb"/>
    <!-- Island -->
    <rect x="110" y="260" width="80" height="40" rx="2" fill="#ddd"/>
  </g>

  <!-- Furniture — master bed -->
  <g opacity="0.45" stroke="#666" stroke-width="0.8" fill="#ccc8bc">
    <rect x="330" y="80" width="130" height="90" rx="3"/>
    <rect x="330" y="80" width="130" height="10" rx="2" fill="#bbb"/>
  </g>

  <!-- Title block -->
  <rect x="480" y="420" width="200" height="60" fill="none" stroke="#333" stroke-width="0.8"/>
  <line x1="480" y1="440" x2="680" y2="440" stroke="#333" stroke-width="0.5"/>
  <text x="580" y="435" text-anchor="middle" font-size="7" fill="#333" letter-spacing="2">DIEGO KURILO ARCHITECTURE</text>
  <text x="580" y="455" text-anchor="middle" font-size="8" fill="#333" font-weight="bold">CASA VENTANA</text>
  <text x="580" y="468" text-anchor="middle" font-size="7" fill="#555">GROUND FLOOR PLAN  |  SCALE 1:100</text>
  <text x="580" y="478" text-anchor="middle" font-size="7" fill="#888">BUENOS AIRES, ARGENTINA  ·  2023</text>
</svg>
""",
    "Casa Ventana — First Floor": """
<svg viewBox="0 0 720 520" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;max-width:720px;background:#f5f0e8;font-family:Inter,sans-serif;">

  <g transform="translate(666,40)">
    <circle cx="0" cy="0" r="16" fill="none" stroke="#333" stroke-width="1"/>
    <polygon points="0,-12 -5,8 0,4 5,8" fill="#333"/>
    <text x="0" y="28" text-anchor="middle" font-size="9" fill="#333">N</text>
  </g>

  <g transform="translate(40,480)">
    <line x1="0" y1="0" x2="120" y2="0" stroke="#333" stroke-width="1"/>
    <line x1="0" y1="-4" x2="0" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="60" y1="-4" x2="60" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="120" y1="-4" x2="120" y2="4" stroke="#333" stroke-width="1"/>
    <text x="0" y="-8" font-size="7" fill="#555">0</text>
    <text x="56" y="-8" font-size="7" fill="#555">3m</text>
    <text x="112" y="-8" font-size="7" fill="#555">6m</text>
  </g>

  <rect x="80" y="60" width="560" height="380" fill="#e8e2d6" stroke="#222" stroke-width="3"/>

  <!-- Stairwell void -->
  <rect x="290" y="280" width="80" height="60" fill="#d5cfc0" stroke="#333" stroke-width="1" stroke-dasharray="4,2"/>
  <line x1="290" y1="280" x2="370" y2="340" stroke="#888" stroke-width="0.6"/>
  <line x1="370" y1="280" x2="290" y2="340" stroke="#888" stroke-width="0.6"/>
  <text x="330" y="315" text-anchor="middle" font-size="7" fill="#777">VOID</text>

  <!-- Walls -->
  <rect x="310" y="60" width="6" height="360" fill="#222"/>
  <rect x="80" y="220" width="236" height="6" fill="#222"/>
  <rect x="80" y="340" width="396" height="6" fill="#222"/>
  <rect x="490" y="60" width="6" height="360" fill="#222"/>

  <!-- Room labels -->
  <text x="185" y="145" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">STUDIO</text>
  <text x="185" y="160" text-anchor="middle" font-size="8" fill="#777">30 m²</text>

  <text x="185" y="290" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">BEDROOM 3</text>
  <text x="185" y="305" text-anchor="middle" font-size="8" fill="#777">20 m²</text>

  <text x="415" y="145" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">TERRACE</text>
  <text x="415" y="160" text-anchor="middle" font-size="8" fill="#777">35 m²</text>

  <text x="580" y="290" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">LIBRARY</text>
  <text x="580" y="305" text-anchor="middle" font-size="8" fill="#777">26 m²</text>

  <!-- Windows -->
  <g fill="#b4c8d0" stroke="#333" stroke-width="0.8">
    <rect x="100" y="438" width="60" height="4"/>
    <rect x="440" y="438" width="60" height="4"/>
    <rect x="110" y="58" width="60" height="4"/>
    <rect x="360" y="58" width="80" height="4"/>
    <rect x="78" y="90" width="4" height="50"/>
    <rect x="638" y="90" width="4" height="50"/>
  </g>

  <!-- Terrace pattern -->
  <g opacity="0.25">
    <line x1="316" y1="60" x2="316" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="340" y1="60" x2="340" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="364" y1="60" x2="364" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="388" y1="60" x2="388" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="412" y1="60" x2="412" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="436" y1="60" x2="436" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="460" y1="60" x2="460" y2="220" stroke="#888" stroke-width="0.5"/>
    <line x1="316" y1="80" x2="490" y2="80" stroke="#888" stroke-width="0.5"/>
    <line x1="316" y1="104" x2="490" y2="104" stroke="#888" stroke-width="0.5"/>
    <line x1="316" y1="128" x2="490" y2="128" stroke="#888" stroke-width="0.5"/>
    <line x1="316" y1="152" x2="490" y2="152" stroke="#888" stroke-width="0.5"/>
    <line x1="316" y1="176" x2="490" y2="176" stroke="#888" stroke-width="0.5"/>
    <line x1="316" y1="200" x2="490" y2="200" stroke="#888" stroke-width="0.5"/>
  </g>

  <!-- Title block -->
  <rect x="480" y="420" width="200" height="60" fill="none" stroke="#333" stroke-width="0.8"/>
  <line x1="480" y1="440" x2="680" y2="440" stroke="#333" stroke-width="0.5"/>
  <text x="580" y="435" text-anchor="middle" font-size="7" fill="#333" letter-spacing="2">DIEGO KURILO ARCHITECTURE</text>
  <text x="580" y="455" text-anchor="middle" font-size="8" fill="#333" font-weight="bold">CASA VENTANA</text>
  <text x="580" y="468" text-anchor="middle" font-size="7" fill="#555">FIRST FLOOR PLAN  |  SCALE 1:100</text>
  <text x="580" y="478" text-anchor="middle" font-size="7" fill="#888">BUENOS AIRES, ARGENTINA  ·  2023</text>
</svg>
""",
    "Villa Serra — Ground Floor": """
<svg viewBox="0 0 720 520" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;max-width:720px;background:#f5f0e8;font-family:Inter,sans-serif;">

  <g transform="translate(666,40)">
    <circle cx="0" cy="0" r="16" fill="none" stroke="#333" stroke-width="1"/>
    <polygon points="0,-12 -5,8 0,4 5,8" fill="#333"/>
    <text x="0" y="28" text-anchor="middle" font-size="9" fill="#333">N</text>
  </g>

  <g transform="translate(40,480)">
    <line x1="0" y1="0" x2="120" y2="0" stroke="#333" stroke-width="1"/>
    <line x1="0" y1="-4" x2="0" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="60" y1="-4" x2="60" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="120" y1="-4" x2="120" y2="4" stroke="#333" stroke-width="1"/>
    <text x="0" y="-8" font-size="7" fill="#555">0</text>
    <text x="56" y="-8" font-size="7" fill="#555">3m</text>
    <text x="112" y="-8" font-size="7" fill="#555">6m</text>
  </g>

  <!-- L-shaped footprint -->
  <polygon points="80,60 500,60 500,260 640,260 640,440 80,440"
           fill="#e8e2d6" stroke="#222" stroke-width="3"/>

  <!-- Interior walls -->
  <rect x="80" y="200" width="420" height="6" fill="#222"/>
  <rect x="280" y="60" width="6" height="146" fill="#222"/>
  <rect x="500" y="260" width="6" height="180" fill="#222"/>
  <rect x="80" y="330" width="426" height="6" fill="#222"/>
  <rect x="360" y="200" width="6" height="136" fill="#222"/>

  <!-- Room labels -->
  <text x="178" y="135" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">LIVING</text>
  <text x="178" y="150" text-anchor="middle" font-size="8" fill="#777">38 m²</text>

  <text x="393" y="135" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">KITCHEN</text>
  <text x="393" y="150" text-anchor="middle" font-size="8" fill="#777">22 m²</text>

  <text x="215" y="270" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">MASTER BED</text>
  <text x="215" y="285" text-anchor="middle" font-size="8" fill="#777">32 m²</text>

  <text x="430" y="270" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">BATH</text>
  <text x="430" y="285" text-anchor="middle" font-size="8" fill="#777">9 m²</text>

  <text x="290" y="390" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">DINING</text>
  <text x="290" y="405" text-anchor="middle" font-size="8" fill="#777">26 m²</text>

  <text x="580" y="360" text-anchor="middle" font-size="10" fill="#444" letter-spacing="2">GARAGE</text>
  <text x="580" y="375" text-anchor="middle" font-size="8" fill="#777">28 m²</text>

  <!-- Windows -->
  <g fill="#b4c8d0" stroke="#333" stroke-width="0.8">
    <rect x="100" y="58" width="60" height="4"/>
    <rect x="320" y="58" width="60" height="4"/>
    <rect x="78" y="100" width="4" height="60"/>
    <rect x="78" y="260" width="4" height="50"/>
    <rect x="140" y="438" width="80" height="4"/>
    <rect x="380" y="438" width="80" height="4"/>
    <rect x="638" y="280" width="4" height="60"/>
    <rect x="500" y="258" width="80" height="4"/>
  </g>

  <!-- Title block -->
  <rect x="480" y="420" width="200" height="60" fill="none" stroke="#333" stroke-width="0.8"/>
  <line x1="480" y1="440" x2="680" y2="440" stroke="#333" stroke-width="0.5"/>
  <text x="580" y="435" text-anchor="middle" font-size="7" fill="#333" letter-spacing="2">DIEGO KURILO ARCHITECTURE</text>
  <text x="580" y="455" text-anchor="middle" font-size="8" fill="#333" font-weight="bold">VILLA SERRA</text>
  <text x="580" y="468" text-anchor="middle" font-size="7" fill="#555">GROUND FLOOR PLAN  |  SCALE 1:100</text>
  <text x="580" y="478" text-anchor="middle" font-size="7" fill="#888">BARILOCHE, ARGENTINA  ·  2021</text>
</svg>
""",
    "Torre Blanca — Typical Floor": """
<svg viewBox="0 0 720 520" xmlns="http://www.w3.org/2000/svg"
     style="width:100%;max-width:720px;background:#f5f0e8;font-family:Inter,sans-serif;">

  <g transform="translate(666,40)">
    <circle cx="0" cy="0" r="16" fill="none" stroke="#333" stroke-width="1"/>
    <polygon points="0,-12 -5,8 0,4 5,8" fill="#333"/>
    <text x="0" y="28" text-anchor="middle" font-size="9" fill="#333">N</text>
  </g>

  <g transform="translate(40,480)">
    <line x1="0" y1="0" x2="120" y2="0" stroke="#333" stroke-width="1"/>
    <line x1="0" y1="-4" x2="0" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="60" y1="-4" x2="60" y2="4" stroke="#333" stroke-width="1"/>
    <line x1="120" y1="-4" x2="120" y2="4" stroke="#333" stroke-width="1"/>
    <text x="0" y="-8" font-size="7" fill="#555">0</text>
    <text x="56" y="-8" font-size="7" fill="#555">3m</text>
    <text x="112" y="-8" font-size="7" fill="#555">6m</text>
  </g>

  <!-- Core (elevator + stairs) -->
  <rect x="300" y="200" width="120" height="120" fill="#d5cfc0" stroke="#333" stroke-width="1.5"/>
  <text x="360" y="258" text-anchor="middle" font-size="8" fill="#555" letter-spacing="2">CORE</text>
  <line x1="300" y1="200" x2="420" y2="320" stroke="#888" stroke-width="0.5"/>
  <line x1="420" y1="200" x2="300" y2="320" stroke="#888" stroke-width="0.5"/>

  <!-- Outer shell -->
  <rect x="80" y="60" width="560" height="400" fill="none" stroke="#222" stroke-width="3"/>

  <!-- Units -->
  <!-- Unit A NW -->
  <rect x="80" y="60" width="220" height="140" fill="#e8e2d6" stroke="#333" stroke-width="1"/>
  <text x="190" y="132" text-anchor="middle" font-size="9" fill="#444" letter-spacing="2">UNIT A</text>
  <text x="190" y="147" text-anchor="middle" font-size="7" fill="#777">72 m²  ·  2 bed</text>
  <!-- Unit B NE -->
  <rect x="420" y="60" width="220" height="140" fill="#e8e2d6" stroke="#333" stroke-width="1"/>
  <text x="530" y="132" text-anchor="middle" font-size="9" fill="#444" letter-spacing="2">UNIT B</text>
  <text x="530" y="147" text-anchor="middle" font-size="7" fill="#777">72 m²  ·  2 bed</text>
  <!-- Unit C SW -->
  <rect x="80" y="320" width="220" height="140" fill="#e8e2d6" stroke="#333" stroke-width="1"/>
  <text x="190" y="392" text-anchor="middle" font-size="9" fill="#444" letter-spacing="2">UNIT C</text>
  <text x="190" y="407" text-anchor="middle" font-size="7" fill="#777">65 m²  ·  1 bed</text>
  <!-- Unit D SE -->
  <rect x="420" y="320" width="220" height="140" fill="#e8e2d6" stroke="#333" stroke-width="1"/>
  <text x="530" y="392" text-anchor="middle" font-size="9" fill="#444" letter-spacing="2">UNIT D</text>
  <text x="530" y="407" text-anchor="middle" font-size="7" fill="#777">65 m²  ·  1 bed</text>
  <!-- Corridors -->
  <rect x="300" y="60" width="120" height="140" fill="#ddd8cc" stroke="#333" stroke-width="1"/>
  <text x="360" y="132" text-anchor="middle" font-size="8" fill="#777">CORRIDOR</text>
  <rect x="300" y="320" width="120" height="140" fill="#ddd8cc" stroke="#333" stroke-width="1"/>
  <text x="360" y="392" text-anchor="middle" font-size="8" fill="#777">CORRIDOR</text>
  <rect x="80" y="200" width="220" height="120" fill="#ddd8cc" stroke="#333" stroke-width="1"/>
  <text x="190" y="262" text-anchor="middle" font-size="8" fill="#777">CORRIDOR</text>
  <rect x="420" y="200" width="220" height="120" fill="#ddd8cc" stroke="#333" stroke-width="1"/>
  <text x="530" y="262" text-anchor="middle" font-size="8" fill="#777">CORRIDOR</text>

  <!-- Windows -->
  <g fill="#b4c8d0" stroke="#333" stroke-width="0.8">
    <!-- North -->
    <rect x="100" y="58" width="60" height="4"/>
    <rect x="440" y="58" width="60" height="4"/>
    <!-- South -->
    <rect x="100" y="458" width="60" height="4"/>
    <rect x="440" y="458" width="60" height="4"/>
    <!-- West -->
    <rect x="78" y="90" width="4" height="50"/>
    <rect x="78" y="330" width="4" height="50"/>
    <!-- East -->
    <rect x="638" y="90" width="4" height="50"/>
    <rect x="638" y="330" width="4" height="50"/>
  </g>

  <!-- Title block -->
  <rect x="480" y="420" width="200" height="60" fill="none" stroke="#333" stroke-width="0.8"/>
  <line x1="480" y1="440" x2="680" y2="440" stroke="#333" stroke-width="0.5"/>
  <text x="580" y="435" text-anchor="middle" font-size="7" fill="#333" letter-spacing="2">DIEGO KURILO ARCHITECTURE</text>
  <text x="580" y="455" text-anchor="middle" font-size="8" fill="#333" font-weight="bold">TORRE BLANCA</text>
  <text x="580" y="468" text-anchor="middle" font-size="7" fill="#555">TYPICAL FLOOR PLAN  |  SCALE 1:200</text>
  <text x="580" y="478" text-anchor="middle" font-size="7" fill="#888">SÃO PAULO, BRAZIL  ·  2024</text>
</svg>
""",
}

st.markdown('<div class="plan-container">', unsafe_allow_html=True)
st.markdown(plans[plan_choice], unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ─── Services ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section" id="services">', unsafe_allow_html=True)
st.markdown(
    """
  <div class="section-tag">What We Do</div>
  <h2 class="section-title">Services</h2>
  <div class="section-divider"></div>
  <div class="services-grid">
    <div class="service-card">
      <div class="service-number">01</div>
      <div class="service-name">Architectural Design</div>
      <div class="service-desc">Full-cycle design from concept sketches and schematic development through to construction documentation and site supervision.</div>
    </div>
    <div class="service-card">
      <div class="service-number">02</div>
      <div class="service-name">Interior Architecture</div>
      <div class="service-desc">Spatial planning, material selection, custom furniture design, and lighting strategy for residential and commercial environments.</div>
    </div>
    <div class="service-card">
      <div class="service-number">03</div>
      <div class="service-name">Urban Design</div>
      <div class="service-desc">Master planning, public space activation, and mixed-use development strategies at neighbourhood and city scale.</div>
    </div>
    <div class="service-card">
      <div class="service-number">04</div>
      <div class="service-name">Visualisation</div>
      <div class="service-desc">Photorealistic renders, animated walkthroughs, and immersive VR experiences to communicate design intent at every project stage.</div>
    </div>
    <div class="service-card">
      <div class="service-number">05</div>
      <div class="service-name">Technical Drawings</div>
      <div class="service-desc">Permit-ready construction documents, detailed sections, floor plans, and structural coordination drawings.</div>
    </div>
    <div class="service-card">
      <div class="service-number">06</div>
      <div class="service-name">Project Management</div>
      <div class="service-desc">On-site coordination, contractor liaison, budget tracking, and programme management from groundbreaking to handover.</div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─── About ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section section-alt" id="about">', unsafe_allow_html=True)
st.markdown(
    """
  <div class="about-grid">
    <div class="about-image-placeholder">
      <svg viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg"
           style="width:100%;height:100%;background:linear-gradient(160deg,#1a1a1a,#252525);">
        <!-- Abstract portrait placeholder -->
        <circle cx="150" cy="140" r="60" fill="none" stroke="rgba(180,160,120,0.15)" stroke-width="1"/>
        <rect x="90" y="220" width="120" height="140" rx="2" fill="none" stroke="rgba(180,160,120,0.1)" stroke-width="1"/>
        <line x1="0" y1="380" x2="300" y2="380" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
        <text x="150" y="395" text-anchor="middle" font-family="Georgia,serif"
              font-size="8" fill="rgba(180,160,120,0.3)" letter-spacing="3">DIEGO KURILO</text>
      </svg>
    </div>
    <div class="about-text">
      <div class="section-tag">The Architect</div>
      <h2 class="section-title">Diego Kurilo</h2>
      <div class="section-divider"></div>
      <p>
        Diego Kurilo is a Buenos Aires–based architect whose practice operates at the intersection of
        tectonic precision and atmospheric sensitivity. Over eighteen years he has built a body of work
        spanning private residences, cultural institutions, and large-scale urban interventions across
        South America and Europe.
      </p>
      <p>
        His approach treats every project as a unique negotiation between site, programme, and material —
        resisting generic solutions in favour of architecture that grows from its context while speaking
        a clear contemporary language.
      </p>
      <p>
        Kurilo studied at the Universidad de Buenos Aires and completed postgraduate research at the
        Architectural Association in London. He has taught at both institutions and lectured widely on
        the relationship between structure and inhabitation.
      </p>
      <div class="about-credentials">
        <div class="credential-item">
          <div class="credential-year">2007</div>
          <div class="credential-text">Architectural Association — Postgraduate Research, London</div>
        </div>
        <div class="credential-item">
          <div class="credential-year">2004</div>
          <div class="credential-text">Universidad de Buenos Aires — Master of Architecture</div>
        </div>
        <div class="credential-item">
          <div class="credential-year">2016</div>
          <div class="credential-text">Mies Crown Hall Americas Prize — Regional Finalist</div>
        </div>
        <div class="credential-item">
          <div class="credential-year">2019</div>
          <div class="credential-text">SCA Argentine Architecture Award — Built Works</div>
        </div>
        <div class="credential-item">
          <div class="credential-year">2022</div>
          <div class="credential-text">ArchDaily Building of the Year — Residential Category</div>
        </div>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Contact ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
st.markdown(
    """
  <div class="section-tag">Get in Touch</div>
  <h2 class="section-title">Start a Project</h2>
  <div class="section-divider"></div>
  <p class="section-body">
    Available for residential commissions, commercial developments, and collaborations.
    New project enquiries are welcome — every conversation starts with listening.
  </p>
  <div class="contact-grid">
    <div>
      <div class="contact-info-item">
        <div class="contact-info-label">Studio Location</div>
        <div class="contact-info-value">Palermo Soho, Buenos Aires<br>Argentina</div>
      </div>
      <div class="contact-info-item">
        <div class="contact-info-label">Email</div>
        <div class="contact-info-value">studio@diegokurilo.com</div>
      </div>
      <div class="contact-info-item">
        <div class="contact-info-label">Phone</div>
        <div class="contact-info-value">+54 11 4832 7700</div>
      </div>
      <div class="contact-info-item">
        <div class="contact-info-label">Office Hours</div>
        <div class="contact-info-value">Mon – Fri, 9:00 – 18:00 ART</div>
      </div>
    </div>
    <div>
""",
    unsafe_allow_html=True,
)

with st.form("contact_form", clear_on_submit=True):
    st.markdown(
        '<style>.stTextInput input, .stTextArea textarea { background:transparent !important; border:none !important; border-bottom:1px solid #333 !important; border-radius:0 !important; color:#ccc !important; padding:12px 0 !important; font-size:0.85rem !important; } .stFormSubmitButton button { background:transparent !important; border:1px solid #b4a078 !important; color:#b4a078 !important; padding:14px 40px !important; letter-spacing:3px !important; text-transform:uppercase !important; font-size:0.72rem !important; border-radius:0 !important; } .stFormSubmitButton button:hover { background:#b4a078 !important; color:#0d0d0d !important; }</style>',
        unsafe_allow_html=True,
    )
    name = st.text_input("", placeholder="Your Name")
    email = st.text_input("", placeholder="Email Address")
    project_type = st.text_input("", placeholder="Project Type")
    message = st.text_area("", placeholder="Tell us about your project", height=100)
    submitted = st.form_submit_button("Send Message")
    if submitted and name and email and message:
        st.markdown(
            '<p style="color:#b4a078;font-size:0.8rem;letter-spacing:1px;margin-top:16px;">Message received — we\'ll be in touch shortly.</p>',
            unsafe_allow_html=True,
        )

st.markdown("</div></div></div>", unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="footer">
  <div class="footer-brand">Diego Kurilo Architecture</div>
  <div class="footer-copy">© 2025 — All Rights Reserved — Buenos Aires</div>
</div>
""",
    unsafe_allow_html=True,
)
