import streamlit as st
from pathlib import Path
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "absFig.png"
profile_pic2 = current_dir / "assets" / "profile-pic.png"
dis_pic1 = current_dir / "assets" / "GraphAbstractII.tif"
dis_pic2 = current_dir / "assets" / "newFigure1.tif"
modular_pic = current_dir / "assets" / "modular.tif"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "PhD Projects | Oluwadare Badejo"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#st.set_page_config(layout="wide")


# Set the title of the web app
st.markdown("""
<h1 style='text-align: center;'>Welcome to My PhD Projects Showcase</h1>
""", unsafe_allow_html=True)

# Create columns for the text and image
col1, col2 = st.columns([1, 3])  # Adjust these ratios based on your preference for text and image size

# Column 1: Introduction Text in Column1
with col2:
    st.markdown("""
    <div style="text-align: justify;">
    Hello! I'm  Oluwadare Badejo, a PhD researcher passionate about Process systems Engineering and Data science and Optimization. 
    This application showcases the various projects I have worked on throughout my PhD journey. 
    Each project below is presented with a detailed description, including the problem statement, 
    approach, results, and applications, along with the computational tools used.
    </div>
    """, unsafe_allow_html=True)
profile_pic2 = Image.open(profile_pic2)
with col1:
    st.image(profile_pic2, width=150)

# Add the description for Project 1
# Add a subheader for Project 1
st.subheader('Project 1: Enterprise-Wide Optimization')
# Image path

#create columns
col1, col2 = st.columns([1,1])  # Adjust the ratio as needed for visual balance

# Add the unified description for Project 1

with col1:
    st.markdown("""
    <div style="text-align: justify;">
In this work, we developed a novel methodology for integrating tactical planning, operational planning, and scheduling within supply chain management.
This approach addresses inefficiencies found in traditional sequential problem-solving methods by leveraging enterprise data and feasibility analysis. 
Our methodology,  is validated through two distinct case studies, demonstrating its capability to achieve optimal costs and improve customer satisfaction 
in the face of market volatilities and regulatory uncertainties. 
    </div>
    """, unsafe_allow_html=True)

st.write("""
    <div style="text-align: justify;"> 
By integrating machine learning insights into strategic decision-making phases, our approach 
optimizes trade-offs across various supply chain functions, simplifies the complexity of integrated models, and speeds up decision-making processes. 
This aligns with digital transformation trends in process industries and enhances the resilience and robustness of decision-making systems.
        <br><br>
        <strong>Read the full paper:</strong> <a href="https://www.sciencedirect.com/science/article/abs/pii/S0098135422001004">Link to the paper</a>
    </div>
    """, unsafe_allow_html=True)


# Add computational tools and model type
st.write("""
**Keywords:** Integrated Supply Chain Optimization, Machine Learning, Feasibility Analysis, Scheduling, Multi-Objective Optimization, Data-Driven Optimization.
""")
st.write("""
**Tools:** Optimization (MIP) , Statistics , Mathematical Programming ( supply chain and scheduling ), Machine leanring and Data Analysis. 
""")
st.write("""
**Software:** Python, GAMS, MatLab
""")

profile_pic = Image.open(profile_pic)
with col2:
    st.image(profile_pic, caption='Integrated supply chain', width=400, use_column_width='always')


# Add the description for Project 2
# Add a subheader for Project 2
st.subheader('Project 2: Supply Chain Design Under Disruptions')
# Image path

#create columns
col1, col2 = st.columns([1,1])  # Adjust the ratio as needed for visual balance

# Add the unified description for Project 1

with col1:
    st.markdown("""
    <div style="text-align: justify;">
        This work presents a mathematical programming approach to optimize tactical and operational decisions in supply chains during disruptions. 
        It highlights the complexity and vulnerability of supply chains in the face of various risks and uncertainties, emphasizing the need for robust and resilient strategies.  
    </div>
    """, unsafe_allow_html=True)

st.write("""
    <div style="text-align: justify;"> 
 The study introduces a discrete time-expanded model within a rolling horizon framework to address these challenges dynamically. This model represents the supply chain as a graph network of nodes (suppliers, manufacturers, warehouses, customers) and arcs (transport links), 
where disruptions can affect both nodes and arcs. The approach allows for the adjustment of routing plans, inventory levels, and capacity utilization to mitigate the impact of disruptions. 
Furthermore, we explore the interplay between disruptions and operational uncertainty in supply chain management.  Here we propose a two-stage stochastic programming model that handles disruptions at both the supplier and transportation levels, as well as operational uncertainties
such as fluctuating demand.  The first stage involves making decisions on supplier choice, manufacturing and warehouse capacity, and transportation modes based on available information,
while the second stage adjusts these decisions as new information on demands and disruptions becomes available. The approach improves decision-making by providing a 
more dynamic response to uncertainties compared to traditional deterministic models, leading to better operational resilience and cost efficiency. 
This works demonstrates the model's effectiveness through comparisons with a multi-period deterministic model, showing the advantages of incorporating stochastic elements 
into supply chain management strategies
        <br><br>
        <strong>Read the full paper:</strong> <br>
        <strong>Paper 1:</strong> <a href="https://pubs.acs.org/doi/abs/10.1021/acs.iecr.2c01641">Link to the paper</a> <br>
        <strong>Paper 2:</strong> <a href="https://aiche.onlinelibrary.wiley.com/doi/abs/10.1002/aic.18037">Link to the paper</a>
    </div>
    """, unsafe_allow_html=True)

# Add computational tools and model type
# Add computational tools and model type
st.write("""
**Keywords:** Mathematical Programming, Supply Chain Management, Disruptions, Tactical and Operational Decisions, Resilience, Disruption, 
                          Operational Uncertainty, Two-Stage Stochastic Programming, Decision Making, Uncertainty Management. 
         
**Tools:** Network Optimization, Decomposition, Optimization (MIP ) , Statistics , Mathematical Programming, and Data Analysis 
         
**Software:**  Python, GAMS, Matlab 
""")
dis_pic1 = Image.open(dis_pic1)
with col2:
    st.image(dis_pic1, caption='supply chain disruption', width=400, use_column_width='always')


# Add the description for Project 2
# Add a subheader for Project 2
st.subheader('Project 3: Modular Supply Chain Network Design')
# Image path

#create columns
col1, col2 = st.columns([1,1])  # Adjust the ratio as needed for visual balance

# Add the unified description for Project 1

with col1:
    st.markdown("""
    <div style="text-align: justify;">
This work addresses the integration of modular supply chain optimization under conditions of demand uncertainty, focusing on minimizing risks and costs across the network. 
Modular supply chain design offers significant advantages, such as flexibility in adjusting to fluctuating demand and reduced capital investments, which are essential in the 
face of increasing market volatility. 
By employing a mixed integer two-stage stochastic programming model, we explore the potential of modular manufacturing to adapt more dynamically 
    </div>
    """, unsafe_allow_html=True)

st.write("""
    <div style="text-align: justify;"> 
compared to centralized approaches. The inclusion of downside risk measures in our models allows for more conservative and risk-averse planning. We apply this methodology to two case studies, illustrating its effectiveness 
in real-world scenarios. The results underline the strategic value of modular designs, showing their capacity to adapt operations and investments responsively, ensuring operational efficiency 
and cost-effectiveness. This approach not only aligns with current trends towards more agile and sustainable manufacturing practices but also provides a robust framework for future research 
in supply chain management under uncertainty.
   <br><br>
        <strong>Read the full paper:</strong> <a href="https://aiche.onlinelibrary.wiley.com/doi/abs/10.1002/aic.17367">Link to the paper</a>
    </div>
    """, unsafe_allow_html=True)

# Add computational tools and model type
# Add computational tools and model type
st.write("""
**Keywords:** Integrated Supply Chain Optimization, Machine Learning, Feasibility Analysis, Scheduling, Multi-Objective Optimization, Data-Driven Optimization. 
         
**Tools:** Network Optimization, Decomposition, Flexibility analysis, stochastic programming, Optimization, Algorithm development,
          Statistics , Mathematical Programming, Machine leanring and Data Analysis 
         
**Software:**  Python, GAMS, Matlab
""")

modular_pic = Image.open(modular_pic)
with col2:
    st.image(modular_pic, caption='modular supply chain network', width=400, use_column_width='always')