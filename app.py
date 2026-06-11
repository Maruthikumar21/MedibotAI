import streamlit as st
from PyPDF2 import PdfReader

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="MediBot AI",
    page_icon="🩺",
    layout="wide"
)

# ================== CLEAN UI THEME ==================
st.markdown("""
<style>
.stApp {
    background-color: #0B1220;
    color: #E5E7EB;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Headings */
h1, h2, h3 {
    color: #38BDF8 !important;
}

/* Inputs */
input, textarea {
    background-color: #1F2937 !important;
    color: white !important;
    border-radius: 8px !important;
}

/* Buttons */
.stButton button {
    background-color: #38BDF8;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}

/* Chat bubbles */
[data-testid="stChatMessage"] {
    background-color: #111827;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================== SIDEBAR ==================
st.sidebar.title("🩺 MediBot AI")
page = st.sidebar.radio("Navigate", [
    "Home",
    "Symptom Checker",
    "Doctor Recommender",
    "Report Explainer",
    "AI Chatbot",
    "Health Tools"
])

# ================== HOME ==================
if page == "Home":
    st.title("MediBot AI 🩺")
    st.write("AI-powered medical assistant for learning purposes only.")
    st.image("https://source.unsplash.com/1200x400/?hospital,technology")

# ================== SYMPTOM CHECKER ==================
elif page == "Symptom Checker":
    st.title("Symptom Checker 🔍")

    symptoms = st.multiselect(
        "Select your symptoms",
        ["Fever", "Cough", "Headache", "Fatigue", "Chest Pain",
         "Dizziness", "Nausea", "Breathing Issues"]
    )

    if st.button("Analyze Symptoms"):
        if len(symptoms) == 0:
            st.warning("Please select symptoms first")
        else:
            st.success("Analysis Complete")
            st.info("Possible condition: Please consult a general physician for proper diagnosis.")

# ================== DOCTOR RECOMMENDER ==================
elif page == "Doctor Recommender":
    st.title("Doctor Recommender 👨‍⚕️")

    disease = st.text_input("Enter your condition or symptoms")

    if st.button("Find Doctor"):
        if disease.strip() == "":
            st.warning("Please enter your condition")
        else:
            st.success("Recommended Specialist: General Physician")
            st.info("Based on your input, visit a nearby hospital for consultation.")

# ================== REPORT EXPLAINER ==================
elif page == "Report Explainer":
    st.title("Medical Report Explainer 📄")

    uploaded_file = st.file_uploader("Upload PDF Report", type="pdf")
    text_input = st.text_area("OR paste report text")

    def extract_pdf(file):
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        return text

    if st.button("Explain Report"):
        if uploaded_file:
            report_text = extract_pdf(uploaded_file)
            st.subheader("Simplified Explanation")
            st.write("Key Findings (AI Simulation):")
            st.info("Your report seems mostly within normal range. Please consult a doctor for confirmation.")

        elif text_input.strip():
            st.subheader("Simplified Explanation")
            st.write("Key Findings (AI Simulation):")
            st.info("The provided text indicates normal or mild conditions. Always consult a doctor.")

        else:
            st.warning("Upload a PDF or paste report text")

# ================== CHATBOT ==================
elif page == "AI Chatbot":
    st.title("AI Health Chatbot 💬")

    if "chat" not in st.session_state:
        st.session_state.chat = [
            {"role": "assistant", "content": "Hi! I am MediBot AI. Ask me anything about health."}
        ]

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Type your health question...")

    if user_input:
        st.session_state.chat.append({"role": "user", "content": user_input})

        reply = "This is an educational response. Please consult a real doctor for medical advice."

        st.session_state.chat.append({"role": "assistant", "content": reply})

# ================== HEALTH TOOLS ==================
elif page == "Health Tools":
    st.title("Health Tools 📊")

    weight = st.number_input("Weight (kg)", 1, 200)
    height = st.number_input("Height (cm)", 50, 250)

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / ((height / 100) ** 2)
            st.success(f"Your BMI is: {bmi:.2f}")
        else:
            st.error("Invalid height")

# ================== FOOTER ==================
st.markdown("---")
st.caption("⚠️ Educational Project Only | MediBot AI")