import streamlit as st
import streamlit.components.v1 as components
import os

# ==========================================
# 1. PAGE SETUP
# ==========================================
st.set_page_config(page_title="Happy 18th, Trishu 🤍", page_icon="🌸", layout="wide")

# ==========================================
# 2. EDITORIAL / CLAUDE ARTIFACT CSS
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Sacramento&family=Jost:wght@300;400&display=swap');

    /* Variables from your HTML */
    :root {
        --rose: #e8a0b0;
        --blush: #f5d6de;
        --deep: #3a1a24;
        --gold: #c9a96e;
        --cream: #fdf6f0;
    }

    /* Background and Global Font */
    .stApp {
        background: #fdf6f0;
        font-family: 'Jost', sans-serif;
        color: #5a3a42; 
    }

    /* Beautiful Falling Petals */
    .petal {
        position: fixed;
        width: 8px;
        height: 8px;
        border-radius: 50% 0 50% 0;
        opacity: 0;
        animation: fall linear infinite;
        z-index: 0;
        pointer-events: none;
    }
    @keyframes fall {
        0%   { transform: translateY(-5vh) rotate(0deg); opacity: 0; }
        10%  { opacity: 0.6; }
        90%  { opacity: 0.3; }
        100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
    }

    /* Top Badges & Headers */
    .title-container {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
        position: relative;
        z-index: 1;
    }
    .age-badge {
        display: inline-block;
        font-family: 'Cormorant Garamond', serif;
        font-size: 13px;
        font-weight: 400;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        color: #c9a96e;
        border: 1px solid #c9a96e;
        padding: 8px 24px;
        margin-bottom: 24px;
        opacity: 0.85;
    }
    .name-title {
        font-family: 'Sacramento', cursive !important;
        font-size: 110px !important; 
        color: #3a1a24 !important; 
        margin: 0px !important;
        padding: 0px !important;
        line-height: 1 !important;
    }
    .happy-bday {
        font-family: 'Cormorant Garamond', serif;
        font-size: 15px;
        font-weight: 300;
        letter-spacing: 0.4em;
        text-transform: uppercase;
        color: #e8a0b0;
        margin-top: 10px;
    }

    /* Elegant Dividers */
    .elegant-divider {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        margin: 40px 0;
    }
    .elegant-divider-line { 
        width: 150px; 
        height: 1px; 
        background: linear-gradient(to right, transparent, #e8a0b0, transparent); 
    }
    .elegant-divider-icon { font-size: 18px; color: #e8a0b0; }

    /* The Main Letter Styling */
    .message-box {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 20px;
        text-align: center;
    }
    .opening {
        font-family: 'Cormorant Garamond', serif;
        font-style: italic;
        font-size: 24px;
        color: #3a1a24;
        line-height: 1.55;
        margin-bottom: 30px;
    }
    .body-text {
        font-family: 'Jost', sans-serif;
        font-weight: 300;
        font-size: 16px;
        color: #5a3a42;
        line-height: 1.95;
        margin-bottom: 20px;
    }

    /* Soft Cards with Gold Corners */
    .soft-card {
        background: #ffffff;
        border-radius: 4px;
        padding: 40px 30px;
        margin-bottom: 20px;
        box-shadow: 0 0 0 1px rgba(201,169,110,0.2), 0 20px 40px rgba(232,160,176,0.1);
        position: relative;
    }
    .soft-card::before, .soft-card::after {
        content: '';
        position: absolute;
        width: 40px;
        height: 40px;
        border-color: #c9a96e;
        border-style: solid;
        opacity: 0.5;
    }
    .soft-card::before { top: 15px; left: 15px; border-width: 1px 0 0 1px; }
    .soft-card::after  { bottom: 15px; right: 15px; border-width: 0 1px 1px 0; }

    /* Pinterest Audio Widget */
    .music-widget {
        background: transparent;
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 15px;
    }
    .spinning-record { font-size: 50px; animation: spin 4s linear infinite; }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    .music-info h4 { margin: 0; font-family: 'Cormorant Garamond'; color: #3a1a24; font-size: 22px; font-weight: 600; font-style: italic;}
    .music-info p { margin: 0; font-family: 'Jost'; font-size: 14px; color: #c9a96e; letter-spacing: 1px; text-transform: uppercase; }

    /* Elegant Gallery Styling */
    div.gallery-block [data-testid="stImage"] img {
        background: white !important;
        padding: 10px !important;
        border-radius: 4px !important;
        border: 1px solid rgba(201,169,110,0.3) !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05) !important;
        transition: all 0.4s ease-in-out !important;
    }
    div.gallery-block [data-testid="stImage"] img:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 15px 30px rgba(201,169,110,0.2) !important;
    }

    [data-testid="stVideo"] {
        border-radius: 4px;
        border: 1px solid rgba(201,169,110,0.3);
        padding: 10px;
        background: white;
    }

    /* Section Headers */
    .cute-header {
        font-family: 'Sacramento', cursive;
        color: #3a1a24;
        font-size: 65px;
        text-align: center;
        margin-top: 60px;
        margin-bottom: 20px;
    }

    /* Sticker Decor Layout Rules */
    div.sticker-layout [data-testid="stImage"] img {
        background: transparent !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
        animation: subtleFloat 3.5s ease-in-out infinite alternate !important;
    }
    @keyframes subtleFloat {
        0% { transform: translateY(0px) rotate(1deg); }
        100% { transform: translateY(-8px) rotate(-1deg); }
    }

    /* MOBILE RESPONSIVENESS */
    @media (max-width: 768px) {
        .name-title { font-size: 85px !important; }
        .age-badge { font-size: 11px; padding: 6px 18px; }
        .cute-header { font-size: 50px; }
        .opening { font-size: 20px; }
        .body-text { font-size: 15px; }
    }
    </style>

    <div class="petal" style="left: 10%; animation-duration: 12s; animation-delay: 0s; background: #e8a0b0;"></div>
    <div class="petal" style="left: 25%; animation-duration: 15s; animation-delay: 4s; background: #f5d6de;"></div>
    <div class="petal" style="left: 45%; animation-duration: 10s; animation-delay: 2s; background: #c9a96e;"></div>
    <div class="petal" style="left: 65%; animation-duration: 14s; animation-delay: 7s; background: #e8a0b0;"></div>
    <div class="petal" style="left: 85%; animation-duration: 11s; animation-delay: 1s; background: #f5d6de;"></div>
    <div class="petal" style="left: 95%; animation-duration: 16s; animation-delay: 5s; background: #c9a96e;"></div>
""", unsafe_allow_html=True)


# Helper execution routing checks for images
def display_sticker(filename_base):
    for ext in [".jpeg", ".jpg", ".png"]:
        full_path = filename_base + ext
        if os.path.exists(full_path):
            st.markdown('<div class="sticker-layout">', unsafe_allow_html=True)
            st.image(full_path, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            return True
    return False


def display_polaroid(filename_base):
    for ext in [".jpeg", ".jpg", ".png"]:
        full_path = filename_base + ext
        if os.path.exists(full_path):
            st.markdown('<div class="gallery-block">', unsafe_allow_html=True)
            st.image(full_path, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            return True
    return False


# ==========================================
# SECTION 1: HEADER & BADGE
# ==========================================
st.markdown("""
    <div class="title-container">
        <div class="age-badge">Turning 18 &nbsp;·&nbsp; A New Chapter</div>
        <div class="name-title">Trishu</div>
        <div class="happy-bday">Happiest Birthday 🤍</div>
    </div>
""", unsafe_allow_html=True)

# Gold Styled Countdown
components.html("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@300;400&display=swap');
        body { margin: 0; font-family: 'Jost', sans-serif; }
        .countdown-container { display: flex; justify-content: center; gap: 12px; margin-top: 15px;}
        .time-box { background: #ffffff; border: 1px solid rgba(201,169,110,0.5); border-radius: 4px; width: 65px; height: 65px; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.03); }
        .time-val { font-family: 'Cormorant Garamond', serif; font-size: 24px; color: #3a1a24; line-height: 1; margin-bottom: 2px;}
        .time-label { font-size: 10px; color: #c9a96e; text-transform: uppercase; letter-spacing: 1px;}
    </style>
    <div class="countdown-container">
        <div class="time-box"><div class="time-val" id="d">00</div><div class="time-label">Days</div></div>
        <div class="time-box"><div class="time-val" id="h">00</div><div class="time-label">Hours</div></div>
        <div class="time-box"><div class="time-val" id="m">00</div><div class="time-label">Mins</div></div>
        <div class="time-box"><div class="time-val" id="s">00</div><div class="time-label">Secs</div></div>
    </div>
    <script>
        const target = new Date("May 26, 2026 00:00:00").getTime();
        setInterval(function() {
            const now = new Date().getTime(); const dist = target - now;
            if (dist < 0) { document.getElementById("d").innerText = "00"; document.getElementById("h").innerText = "00"; document.getElementById("m").innerText = "00"; document.getElementById("s").innerText = "00"; return; }
            document.getElementById("d").innerText = Math.floor(dist / (1000 * 60 * 60 * 24)).toString().padStart(2, '0');
            document.getElementById("h").innerText = Math.floor((dist % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0');
            document.getElementById("m").innerText = Math.floor((dist % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0');
            document.getElementById("s").innerText = Math.floor((dist % (1000 * 60)) / 1000).toString().padStart(2, '0');
        }, 1000);
    </script>
""", height=90)

# ==========================================
# SECTION 2: THE ELEGANT LETTER
# ==========================================
st.markdown("""
    <div class="elegant-divider">
        <div class="elegant-divider-line"></div>
        <div class="elegant-divider-icon">🌸</div>
        <div class="elegant-divider-line"></div>
    </div>
""", unsafe_allow_html=True)

col_msg1, col_msg2 = st.columns([4, 1])

with col_msg1:
    st.markdown("""
        <div class="message-box">
            <p class="opening">
              "To the sweetest person I had ever met,<br>
              and the kindest soul I had ever known…"
            </p>
            <p class="body-text">
              I wish this year brings all your sparks back in their fullest, and you shine like the brightest star — as you always have. Words will always feel less to express what I feel for you, but I really want to thank you for making me feel loved — so much that it still exists like it had never ended.
            </p>
            <p class="body-text">
              The way you made me smile is still the best smile I have ever smiled. Thank you for showing me what love actually is, and for being the first person to make me believe that there is something truly beautiful to feel from another person. I will be always grateful for that.
            </p>
            <p class="body-text">
              I know things have changed, but there is something of you in me that no one can ever take away — and I hope it stays for as long as I am here. I hope you always remain the kind of person who makes others feel their absolute best, with your kind-hearted soul that makes everyone around you feel loved and cared for.
            </p>
            <p class="body-text">
              You deserve the whole world, Trishu. I hope you get back to your best and rise above everything you're going through right now.
            </p>
            <p class="opening" style="margin-top: 30px; font-size: 22px;">
              It's your day — enjoy it to the fullest. 🩷🧿
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_msg2:
    display_sticker("flower")
    st.write("<br><br>", unsafe_allow_html=True)
    display_sticker("18-candle")

st.markdown("""
    <div class="elegant-divider">
        <div class="elegant-divider-line"></div>
        <div class="elegant-divider-icon">🩷</div>
        <div class="elegant-divider-line"></div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# SECTION 3: JUST US & THE VIBE
# ==========================================
st.markdown('<p class="cute-header">Just Us & The Vibe</p>', unsafe_allow_html=True)
col_us, col_music = st.columns([1.2, 1])

with col_us:
    display_polaroid("pic-us")

with col_music:
    st.markdown('<div class="soft-card">', unsafe_allow_html=True)
    st.markdown("""
        <div class="music-widget">
            <div class="spinning-record">💿</div>
            <div class="music-info">
                <h4>Trishu's Era</h4>
                <p>Press Play</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    if os.path.exists("song01.mpeg"):
        st.audio("song01.mpeg")
    elif os.path.exists("song01.mp3"):
        st.audio("song01.mp3")
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# SECTION 4: FRIENDS (VIDEO)
# ==========================================
st.markdown('<p class="cute-header">Friends & Forever Laughs</p>', unsafe_allow_html=True)
col_vid1, col_vid2, col_vid3 = st.columns([1, 4, 1])

with col_vid1:
    display_sticker("disco")

with col_vid2:
    if os.path.exists("vid01.mp4"): st.video("vid01.mp4")

with col_vid3:
    display_sticker("mcqueen")

# ==========================================
# SECTION 5: FAMILY & ROOTS
# ==========================================
st.markdown('<p class="cute-header">Family & Roots</p>', unsafe_allow_html=True)
family_pics = ["pic07", "pic08", "pic09"]

fam_cols = st.columns(3)
for i, p in enumerate(family_pics):
    with fam_cols[i]:
        display_polaroid(p)

# ==========================================
# SECTION 6: F1 / RACING TRACK SECTION
# ==========================================
st.markdown('<p class="cute-header" style="font-size: 55px;">Fast Lanes & Good Days</p>', unsafe_allow_html=True)
car_cols = st.columns(4)
with car_cols[0]: display_sticker("lewis44")
with car_cols[1]: display_sticker("ferrari")
with car_cols[2]: display_sticker("lewisf1")
with car_cols[3]: display_sticker("slr300")

# ==========================================
# SECTION 7: A GALLERY OF LOVE
# ==========================================
st.markdown('<p class="cute-header">A Gallery of Love</p>', unsafe_allow_html=True)
scrapbook_pics = ["pic01", "pic02", "pic03", "pic04", "pic05", "pic06", "pic10", "pic-special"]

gal_cols = st.columns(3)
for i, p in enumerate(scrapbook_pics):
    with gal_cols[i % 3]:
        display_polaroid(p)

# ==========================================
# SECTION 8: MAKE A WISH
# ==========================================
st.markdown('<p class="cute-header">Make a Wish</p>', unsafe_allow_html=True)
st.markdown('<div class="soft-card" style="text-align:center;">', unsafe_allow_html=True)

col_cake1, col_cake2, col_cake3 = st.columns([2.2, 1, 2.2])
with col_cake2:
    if not display_sticker("birthdaycake"):
        st.markdown('<div style="font-size: 80px;">🎂</div>', unsafe_allow_html=True)

st.markdown("""
    <h3 style="font-family: 'Cormorant Garamond', serif; font-style: italic; color:#3a1a24; font-size: 35px; margin-bottom: 5px;">Close your eyes...</h3>
    <p style="color:#c9a96e; font-size: 16px; letter-spacing: 1px; text-transform: uppercase;">Take a deep breath, make your biggest wish, and welcome to 18.</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown(
    "<br><p style='text-align:center; font-family: \"Cormorant Garamond\", serif; color:#c9a96e; font-size:14px; letter-spacing: 3px; text-transform: uppercase;'>Happy 18th, Trishu <br> <span style=\"font-size: 10px;\">With all the love, always</span></p>",
    unsafe_allow_html=True)