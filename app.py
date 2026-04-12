import streamlit as st
import pandas as pd
import time
import base64
import streamlit.components.v1 as components
from ml.recommend import recommend
from ml.clustering import cluster_users

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Learning Platform Recommender",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= THEME STATE =================
if "theme" not in st.session_state:
    st.session_state.theme = "light"

def toggle_theme():
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# ================= LOAD IMAGE =================
@st.cache_data
def load_image_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None


image_base64 = load_image_base64("assets/abc.svg")

# ================= CSS =================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@1&display=swap');
.stSelectbox > div > div {{
    background-color: #1e2a3a !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
}}

.stSelectbox > div > div > div {{
    color: white !important;
}}

.stSelectbox [data-baseweb="select"] > div {{
    background-color: #1e2a3a !important;
    color: white !important;
}}

.hero {{
    background: linear-gradient(135deg, rgba(15,40,84,0.5), rgba(15,40,84,0.3))
    {f", url('data:image/svg+xml;base64,{image_base64}')" if image_base64 else ""};
    background-size: cover;
    background-position: center;
    height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    border-radius: 0 0 20px 20px;
}}

.stApp {{
   background: #0f172a;
}}

.stSelectbox label {{
    color: #0ea5e9;
}}

h3 {{
    color: #0ea5e9 !important;
}}

.hero h1 {{ font-size: 3rem; }}
.hero p {{
    font-size: 1.2rem;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #90cdf4;
    letter-spacing: 1px;
}}

.logo-scroll {{
    width: 100%;
    overflow: hidden;
    background: transparent;
    padding: 20px 0;
}}

.logo-track {{
    display: flex;
    width: max-content;
    animation: scroll-left 30s linear infinite;
}}

.platform-logo {{
    width: 40px;
    height: 40px;
    margin: 0 1.5rem;
    filter: grayscale(50%);
    opacity: 0.8;
    transition: all 0.3s ease;
}}

.platform-logo:hover {{
    filter: grayscale(0%);
    transform: scale(1.15);
    opacity: 1;
}}

@keyframes scroll-left {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-50%); }}
}}

.form-container {{
    background: #1e2a3a;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12);
    max-width: 750px;
    margin: auto;
}}

.stButton>button {{
    background: #0ea5e9;
    color: white;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    width: 100%;
    margin-top: 20px;
}}

.stButton>button:hover {{
    background: #0284c7;
}}

</style>
""", unsafe_allow_html=True)

# ================= THEME BUTTON =================
st.markdown('<div class="theme-toggle">', unsafe_allow_html=True)
st.button("🌙 / ☀️", on_click=toggle_theme)
st.markdown('</div>', unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
<div class="hero">
  <div>
    <h1>Learn Smarter</h1>
    <p>AI-powered platform recommendation for developers</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ================= LOGO SCROLL =================
st.markdown("""
<div class="logo-scroll">
  <div class="logo-track">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" alt="Java">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" alt="C++">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg" alt="Ruby">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg" alt="Go">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" alt="C#">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" alt="Next.js">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" alt="Vue.js">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angular/angular-original.svg" alt="Angular">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" alt="MySQL">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" alt="MongoDB">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg" alt="AWS">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg" alt="Azure">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" alt="Google Cloud">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" alt="Kubernetes">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="VS Code">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jetbrains/jetbrains-original.svg" alt="JetBrains">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" alt="Node.js">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg" alt="Express">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" alt="Flask">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg" alt="Spring">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/laravel/laravel-plain.svg" alt="Laravel">
    <!-- duplicate pour loop infini -->
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" alt="Java">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" alt="C++">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg" alt="Ruby">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker">
    <img class="platform-logo" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" alt="Kubernetes">
  </div>
</div>
""", unsafe_allow_html=True)

# ================= FORM =================
st.subheader("🎯 Build your learning profile")
st.markdown('<div class="form-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox("Programming language", ["Python", "Java", "C++", "JavaScript"])
    level = st.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
    learning_format = st.selectbox("Learning format", ["Text", "Video", "Hands-on"])

with col2:
    budget = st.selectbox("Budget", ["Free", "Paid"])
    goal = st.selectbox("Goal", ["Discovery", "Professional skills", "Certification"])

st.markdown("</div>", unsafe_allow_html=True)

# ================= ACTION =================
if st.button("🚀 Generate recommendations"):
    with st.spinner("Running ML model..."):
        time.sleep(1)

        users_df = cluster_users()

        new_user = pd.DataFrame([{
            "user_id": 999,
            "language": language,
            "level": level,
            "format": learning_format,
            "budget": budget,
            "goal": goal
        }])

        users_df = pd.concat([users_df, new_user], ignore_index=True)
        clustered_users = cluster_users(users_df)
        results = recommend(999, users_df=clustered_users)

    st.success("Here are your best platforms 👇")

    for _, row in results.iterrows():
        components.html(f"""
        <div style="
            background: #1e2a3a;
            padding: 20px;
            border-radius: 12px;
            margin: 5px 0;
            font-family: sans-serif;
        ">
            <h3 style="color: white; margin-top: 0;">{row['platform']}</h3>
            <p style="color: #a0aec0;">
                <b style="color: white;">Score:</b> {row['score']:.2f}
            </p>
            <a href="{row['platform_url']}" target="_blank"
               style="color: #0ea5e9; font-weight: 600; text-decoration: none;">
               Visit platform →
            </a>
        </div>
        """, height=150)

# ================= FOOTER =================
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; color: #666;">
    <p>Learning Platform Recommender • Powered by AI/ML</p>
</div>
""", unsafe_allow_html=True)