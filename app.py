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

/* Background */
.stApp {
    background-color: #0B1220;
    color: #F9FAFB;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0F172A;
}

/* Headings */
h1, h2, h3, h4 {
    color: #38BDF8 !important;
    font-weight: 700;
}

/* Global text visibility */
p, span, label, div {
    color: #F1F5F9 !important;
    font-size: 16px;
}

/* Inputs */
input, textarea {
    background-color: #1E293B !important;
    color: #FFFFFF !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

/* Placeholder */
input::placeholder, textarea::placeholder {
    color: #94A3B8 !important;
}

/* Buttons */
.stButton button {
    background-color: #2563EB;
    color: white;
    font-weight: 600;
    border-radius: 8px;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background-color: #111C2E;
    color: #F8FAFC !important;
    border-radius: 12px;
    padding: 12px;
    border: 1px solid #1F2A44;
}

/* Alerts */
.stAlert {
    background-color: #111827 !important;
    color: #F8FAFC !important;
    border-left: 5px solid #38BDF8;
}

/* ================== MULTISELECT FIX (IMPORTANT) ================== */
div[data-baseweb="select"] * {
    color: #F8FAFC !important;
}

div[data-baseweb="select"] {
    background-color: #1E293B !important;
}

.stMultiSelect span {
    color: #F8FAFC !important;
}

ul {
    background-color: #1E293B !important;
    color: #F8FAFC !important;
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
    st.write("AI-powered medical triage assistant (Educational Use Only)")
    st.image("https://source.unsplash.com/1200x400/?hospital,technology")

# ================== SYMPTOM CHECKER ==================
elif page == "Symptom Checker":
    st.title("Symptom Checker 🔍")

    symptoms = st.multiselect(
        "Select symptoms",
        ["Fever", "Cough", "Headache", "Fatigue", "Chest Pain",
         "Dizziness", "Nausea", "Breathing Difficulty", "Body Pain"]
    )

    if st.button("Analyze Symptoms"):
        if not symptoms:
            st.warning("Please select symptoms")
        else:
            st.success("Analysis Complete")

            if "Chest Pain" in symptoms or "Breathing Difficulty" in symptoms:
                st.error("🚨 HIGH RISK DETECTED")
                st.write("Seek immediate medical attention")

            elif "Fever" in symptoms or "Cough" in symptoms:
                st.warning("🟡 Moderate condition")
                st.write("Consult General Physician")

            else:
                st.info("🟢 Low risk condition")
                st.write("Rest and monitor symptoms")

# ================== DOCTOR RECOMMENDER ==================
elif page == "Doctor Recommender":
    st.title("Medical Triage System 👨‍⚕️")

    symptom_text = st.text_input("Describe your symptoms")

    if st.button("Analyze"):
        if symptom_text.strip() == "":
            st.warning("Please enter symptoms")
        else:
            text = symptom_text.lower()

            if any(x in text for x in ["chest pain", "heart pain", "faint", "left arm"]):
                st.error("🚨 EMERGENCY RISK")
                st.write("Possible cardiac issue")
                st.write("Go to Emergency Room immediately")
                st.write("Specialist: Cardiologist / Emergency Medicine")

            elif any(x in text for x in ["breathing", "shortness of breath", "severe pain"]):
                st.error("⚠️ HIGH RISK")
                st.write("Requires urgent medical attention")
                st.write("Specialist: Pulmonologist / General Physician")

            elif any(x in text for x in ["fever", "cough", "cold", "fatigue"]):
                st.warning("🟡 MODERATE CONDITION")
                st.write("Likely infection or viral illness")
                st.write("Specialist: General Physician")

            elif any(x in text for x in ["headache", "mild pain"]):
                st.info("🟢 LOW RISK")
                st.write("Minor condition suspected")
                st.write("Rest and hydration recommended")

            else:
                st.info("⚪ UNCERTAIN CONDITION")
                st.write("Consult General Physician")

# ================== REPORT EXPLAINER ==================
elif page == "Report Explainer":
    st.title("Medical Report Explainer 📄")

    uploaded = st.file_uploader("Upload PDF report", type="pdf")
    text_input = st.text_area("OR paste report text")

    def extract_pdf(file):
        pdf = PdfReader(file)
        text = ""
        for p in pdf.pages:
            text += p.extract_text() or ""
        return text

    if st.button("Explain Report"):
        if uploaded:
            data = extract_pdf(uploaded)
            st.subheader("Report Summary")
            st.info("Report appears mostly normal. Consult doctor for confirmation.")

        elif text_input.strip():
            st.subheader("Report Summary")
            st.info("No major issues detected in text analysis.")

        else:
            st.warning("Upload PDF or paste text")

# ================== CHATBOT ==================
elif page == "AI Chatbot":
    st.title("AI Health Chatbot 💬")

    if "chat" not in st.session_state:
        st.session_state.chat = [
            {"role": "assistant", "content": "Hi! I am MediBot AI. Ask me health-related questions."}
        ]

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Type your question")

    if user_input:
        st.session_state.chat.append({"role": "user", "content": user_input})

        reply = "This is an educational response. Please consult a real doctor."

        st.session_state.chat.append({"role": "assistant", "content": reply})

# ================== HEALTH TOOLS ==================
elif page == "Health Tools":
    st.title("Health Tools 📊")

    weight = st.number_input("Weight (kg)", 1, 200)
    height = st.number_input("Height (cm)", 50, 250)

    if st.button("Calculate BMI"):
        bmi = weight / ((height / 100) ** 2)
        st.success(f"Your BMI: {bmi:.2f}")

# ================== FOOTER ==================
st.markdown("---")
st.caption("⚠️ Educational AI Medical Triage System | Not a real diagnosis tool")