import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Tia Gustiana CV",
    page_icon="💼",
    layout="wide"
)

# GREEN & WHITE THEME CSS
st.markdown("""
<style>
    .main-title {
        font-size: 44px;
        font-weight: bold;
        color: #1B5E20;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #4CAF50;
        margin-bottom: 20px;
    }

    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #2E7D32;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }

    .highlight {
        color: #2E7D32;
        font-weight: bold;
    }

    .stApp {
        background-color: #f3fff4;
    }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="main-title">Tia Gustiana</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Electronics Systems Engineering Student | IoT Enthusiast</div>', unsafe_allow_html=True)

st.write("---")

# SIDEBAR MENU
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Home", "About", "Education", "Skills", "Projects", "Contact"]
)

# HOME
if menu == "Home":
    st.markdown("## 👋 Welcome")
    st.success("Welcome to my personal CV website 🌿")
    st.info("Focused on IoT, Electronics, and Industrial Automation")

# ABOUT
elif menu == "About":
    st.markdown("## 👤 About Me")

    st.markdown("""
    <div class="card">
    I am a student passionate about <span class="highlight">IoT, electronics, instrumentation, and automation systems</span>.  
    I enjoy building real-world projects and learning modern technology.
    </div>
    """, unsafe_allow_html=True)

# EDUCATION
elif menu == "Education":
    st.markdown("## 🎓 Education")

    st.markdown("""
    <div class="card">
    • SMA Negeri 7 Dumai  
    • Politeknik Caltex Riau (2024 - Present)
    </div>
    """, unsafe_allow_html=True)

# SKILLS
elif menu == "Skills":
    st.markdown("## 💡 Skills")

    st.markdown("""
    <div class="card">
    ✔ Python  
    ✔ Arduino  
    ✔ LabVIEW  
    ✔ SQL Basics  
    ✔ Proteus  
    ✔ IoT Development  
    </div>
    """, unsafe_allow_html=True)

# PROJECTS
elif menu == "Projects":
    st.markdown("## 🛠️ Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🎹 Touch Sensor Piano")
        st.write("Electronic music instrument using sensors")

        st.success("🔁 Flip-Flop Circuit")
        st.write("Digital electronics project")

    with col2:
        st.success("🤖 Line Follower Robot")
        st.write("Automation robot using sensors")

# CONTACT
elif menu == "Contact":
    st.markdown("## 📞 Contact")

    st.markdown("""
    <div class="card">
    📧 Email: tia24trse@mahasiswa.pcr.ac.id  
    📱 Phone: 0851-9479-2996  
    🏢 Organization: ICON  
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.sidebar.write("---")
st.sidebar.write("💚 Green Theme CV")
st.sidebar.write("© 2026 Tia Gustiana")