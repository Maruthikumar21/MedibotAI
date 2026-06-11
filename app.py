import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="MediBot AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================== CLEAN PROFESSIONAL DARK THEME ==================
st.markdown("""
    <style>
    .stApp {
        background-color: #0A0C10;
        color: #F0F0F0;
    }
    /* Dark Sidebar */
    .css-1d391kg, .sidebar .sidebar-content, section[data-testid="stSidebar"] {
        background-color: #12151C !important;
    }
    
    h1, h2, h3, h4 {
        color: #00FFCC !important;
    }
    
    p, label, .stMarkdown {
        color: #E0E0E0 !important;
    }
    
    /* Inputs */
    .stTextInput input, .stSelectbox, .stMultiselect, .stNumberInput input, textarea {
        background-color: #1F2937 !important;
        color: #FFFFFF !important;
        border: 1px solid #4B5563;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #00FFAA;
        color: #0A0C10;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    
    /* Alerts */
    .stSuccess, .stWarning, .stInfo, .stError {
        background-color: #1F2937;
        color: #FFFFFF;
        border-left: 5px solid #00FFAA;
    }
    </style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
st.sidebar.title("🩺 MediBot AI")
st.sidebar.markdown("**Professional AI Medical Assistant**")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", 
    "🔍 Symptom Checker", 
    "👨‍⚕️ Doctor Recommender",
    "📄 Report Explainer", 
    "💬 AI Chatbot", 
    "📊 Health Tools"
])

# ================== PAGES ==================
if page == "🏠 Home":
    st.title("Welcome to MediBot AI 🩺")
    st.markdown("### Professional AI Medical Assistant")
    st.image("https://source.unsplash.com/800x400/?doctor,modern,technology", width="stretch")
    st.success("Clean • Professional • Educational Project")

elif page == "🔍 Symptom Checker":
    st.title("🔍 AI Symptom Checker")
    st.warning("**Educational Demo Only** — Not for real medical diagnosis")
    
    symptoms = ['Fever', 'Cough', 'Headache', 'Fatigue', 'Sore Throat', 
                'Body Ache', 'Nausea', 'Shortness of Breath', 'Chest Pain', 
                'Dizziness', 'Runny Nose']
    
    selected = st.multiselect("Select your symptoms", symptoms)
    
    if st.button("🔎 Predict Condition", type="primary"):
        if selected:
            st.success("**Most Likely:** Viral Infection / Flu")
            st.info("**Advice:** Rest well, drink water, and consult a real doctor.")
            st.session_state.last_disease = "Viral Infection"
        else:
            st.error("Please select at least one symptom")

elif page == "👨‍⚕️ Doctor Recommender":
    st.title("👨‍⚕️ Doctor Recommender")
    disease = st.text_input("Enter condition or symptom", 
                           value=st.session_state.get("last_disease", ""))
    
    if st.button("Get Recommendation"):
        if disease:
            st.success("**Recommended Doctor:** General Physician")
            st.info("Visit a nearby hospital or clinic.")
        else:
            st.warning("Please enter a condition")

elif page == "📄 Report Explainer":
    st.title("📄 Medical Report Explainer")
    uploaded = st.file_uploader("Upload PDF Report", type="pdf")
    text = st.text_area("Or paste report text", height=180)
    
    if st.button("Explain in Simple Language"):
        if uploaded or text.strip():
            st.subheader("Simplified Explanation")
            st.success("**Key Points:** Most values are normal.")
            st.write("Please consult your doctor with the full report.")
        else:
            st.warning("Upload PDF or paste text")

elif page == "💬 AI Chatbot":
    st.title("💬 AI Health Chatbot")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    if prompt := st.chat_input("Ask your question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        reply = "Thank you. Remember, this is an educational project. Please consult a real doctor."
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)

elif page == "📊 Health Tools":
    st.title("📊 Health Tools")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", 20, 250, 70)
        height = st.number_input("Height (cm)", 100, 250, 170)
        if st.button("Calculate BMI"):
            bmi = weight / ((height/100)**2)
            st.metric("Your BMI", f"{bmi:.1f}")

# Footer
st.markdown("---")
st.caption("⚠️ Educational Project Only • Always consult a licensed medical professional")