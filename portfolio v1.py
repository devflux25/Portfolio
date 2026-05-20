import streamlit as st 

st.markdown("""
<style>
/* cleaner font */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}
/* bigger title */
h1 {
    font-size: 3rem !important;
    font-weight: 700 !important;
}
/* add padding to main content */
.block-container {
    padding-top: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
}
/* skill label color */
h3 {
    color: #00C9A7 !important;
}
</style>
""", unsafe_allow_html=True)


st.title("Kairav Joshi Portfolio")

page  = st.sidebar.selectbox("Navigate",["About Me", "Skills", "Projects", "Contact"])

if(page=="About Me"):
    st.subheader("Python Developer |  AI Enthusiast")

    #st.write("I'm Kairav Joshi, a 1st year CSE student at Manipal University Jaipur, building AI-powered tools for students like StudyOS and Code Reviewer using Python, LangChain and Gemini API.")

    col1,col2 = st.columns([3,2])
    with col1:
        st.write("I'm Kairav Joshi, a 1st year CSE student at Manipal University Jaipur, building AI-powered tools for students like StudyOS and Code Reviewer using Python, LangChain and Gemini API.")
    with col2:
        st.write("🎓 Manipal University Jaipur")
        st.write("📍 Rajasthan, India")
        st.write("💻 CSE 1st Year")
    
    st.info("🔨 Open to internships and collaborations. Both projects live by July 2025.")


elif(page =="Skills"):
    st.subheader("My Skills")
    #st.write("Python")
    #st.progress(70)

    #st.write("Machine Learning")
    #st.progress(55)

    #st.write("Data Analysis / EDA")
    #st.progress(60)

    #st.write("SQL")
    #st.progress(45)

    #st.write("Web Scraping / Automation")
    #st.progress(70)

    st.subheader("Languages")
    st.markdown("`Python`  `SQL`")

    st.subheader("AI / ML")
    st.markdown("`Scikit-learn`  `Pandas`  `LangChain`  `Gemini API`")

    st.subheader("Tools & Frameworks")
    st.markdown("`Streamlit`  `FastAPI`  `Selenium`  `Git`")

    st.subheader("Currently Learning")
    st.markdown("`LangChain`  `FAISS`  `RAG`  `Deployment`")


elif(page=="Projects"):
    with st.container(border=True):
        st.subheader("IPL Match Outcome Predictor")
        st.write("Predicts match winner based on team stats and player data.")
        st.write("Tech: Python, Pandas, Scikit-learn")
        st.link_button("View on GitHub", "https://github.com/devflux25/ipl-match-outcome-prediction")
        st.divider()

    with st.container(border=True):
        st.subheader("Gpu-Exploratory-Data-Analysis")
        st.write("This project is a GPU-accelerated exploratory data analysis platform that enables fast dataset processing, visualization, and insight generation for machine learning workflows.")
        st.write("Tech: Python, Pandas, Matplotlib, Numpy")
        st.link_button("View on GitHub", "https://github.com/devflux25/gpu-exploratory-data-analysis")
        st.divider()

    with st.container(border=True):
        st.subheader("Auto-Attendance-Tracker")
        st.write("A Python bot using Selenium and PyAutoGUI that automatically collects attendance data from SLCM and sends it to WhatsApp. Note: This script works only for MUJ students with valid SLCM credentials.")
        st.write("Tech: Python, selenium , pyautogui ")
        st.link_button("View on GitHub", "https://github.com/devflux25/auto-attendance-tracker-MUJ-Students-only-")
        st.divider()

    with st.container(border=True):
        st.subheader("Python-Gui-Calculator")
        st.write("A simple desktop calculator built with Python Tkinter for basic arithmetic operations")
        st.write("Tech: Python, Tkinter ")
        st.link_button("View on GitHub", "https://github.com/devflux25/python-gui-calculator")
        st.divider()

    with st.container(border=True):
        st.subheader("Code Reviewer")
        st.write("AI-powered code reviewer built with Streamlit and Gemini API. Paste your code and get instant bug detection, improvements and quality score.")
        st.write("Tech: Python, Streamlit, Gemini API  ")
        st.link_button("View on GitHub", "https://github.com/devflux25/code-reviewer-bot")
        st.divider()

    with st.container(border=True):
        st.subheader("StudyOS")
        st.write("Coming Soon!!!")
        st.divider()


elif(page =="Contact"):
    st.write("📧 kairavjoshi2503@gmail.com")
    st.link_button("GitHub", "https://github.com/devflux25")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/kairav-joshi-b2bb59388/")