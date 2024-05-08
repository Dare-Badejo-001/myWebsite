from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Oluwadare Badejo"
PAGE_ICON = ":wave:"
NAME = "Oluwadare(Dare) Badejo"
DESCRIPTION = """
Doctoral Researcher @ University of Delaware | PhD Candidate, Chemical and Biomolecular Engineering | Specializing in Mathematical Modeling & Optimization | Process Systems Engineering | Data Science | Sustainability
Utilizes advanced data analytics and mathematical modeling techniques to enhance decision-making and process efficiency. 
"""

EMAIL = "ooa.badejo@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/oluwadare-badejo/",
    "GitHub": "https://github.com/Dare-Badejo-001",
    "Google Scholar": "https://scholar.google.com/citations?user=gnYqDV8AAAAJ&hl=en&oi=ao",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Over 7 years extracting actionable insights from data in academia and industry.
- ✔️ Proficient in Python, MATLAB, GAMS, and Excel; skilled in algorithm development.
- ✔️ Demonstrated leadership in research projects, enhancing efficiency and innovation.
- ✔️ Experienced in dynamic simulation and cost-saving strategies in energy sectors.
- ✔️ Adept at mentoring teams, significantly improving project outcomes.
- ✔️ Engaged in cutting-edge research focused on resilience and data-driven modeling.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
    - 👩‍💻Programming: Python (Pandas, sklearn, TensorFlow, GIS), MATLAB, R, GAMS, VBA.
    - 📊Data Visualization: Expert in Plotly, Excel, Matplotlib, Bokeh, PowerBI.
    - 📚Modeling & Simulation: Mixed Integer Programming, Machine Learning (supervised, unsupervised, deep learning and CNN), Aspen Suites.
    - 🗄️Database Management: Proficient in SQL, Excel; MongoDB, MySQL, Hadoop, Spark.
    - 🛠️Additional Tools: version control Git, AWS, Azure.
    """
)


st.subheader("Soft Skills")
st.write(
    """
    - 📝 Communication: Skilled in documentation and presentations.
    - 🌀 Project Management: Expert in timely project execution.
    - 🤝 Leadership and Mentoring: Strong in team leadership and peer mentoring.
    - 🌐 Interdisciplinary Collaboration: Effective in multi-disciplinary team integration.
    """
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Graduate Research Assistant | University of Delaware, Department of Chemical and Biomolecular Engineering**")
st.write("Aug. 2019 – Present")
st.write(
    """
- ► Developed stochastic optimization models for supply chain resilience, enhancing decision-making under disruptions.
- ► Led data analytics initiatives, employing Python and MATLAB for predictive modeling and algorithm development.
- ► Engaged with interdisciplinary teams for plastic waste management, integrating LCA, TEA into supply chain solutions.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Graduate Research Assistant | University of Lagos, Department of Chemical and Petroleum Engineering**")
st.write("July 2018 – Aug. 2019")
st.write(
    """
- ► Pioneered a mentorship program, improving students performance.
- ► Provided technical tutoring in MATLAB, VBA, and Python.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Oilfield Engineer | Eunisell Limited, Lagos/Rivers State**")
st.write("Jan. 2018 – June 2018")
st.write(
    """
- ► Engineered optimization strategies for oil production optimization 
- ► Contributed to operational process improvements for oil production optimization
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Research Assistant | Landmark University, Omu-Aran, Kwara State**")
st.write("April 2016 – March 2017")
st.write(
    """
- ► Aided in developing educational experiments to increase scientific literacy among students.
- ► Coordinated lectures and tutorials.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Process Engineering Intern | Shell Petroleum Development Company of Nigeria, Rivers State**")
st.write("Aug. 2014 – Dec. 2014")
st.write(
    """
- ► Developed dynamic process simulation models with Aspen Hysys 
- ► Collaborated across teams to enhance gas quality, integrating flow parameter impacts into operations.s
"""
)

PROJECTS = {
    "🏆 Supply Chain Optimization(PhD Works) - Summary of prjects and findings": "https://dare-phd-project.streamlit.app/",
    "🏆 Real Time Breast cancer prediction and visualization  - Web App Developement": "https://appcancer-logreg.streamlit.app/",
    "🏆 LLM Finetuning for special problem - Web app development for PDFs ": "https://appcancer-logreg.streamlit.app/",
    "🏆 Reinforcement Learning  - Hybrid model to learn": "https://appcancer-logreg.streamlit.app/",
}

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
