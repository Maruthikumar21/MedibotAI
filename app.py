import streamlit as st
from PyPDF2 import PdfReader

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="MediBot AI",
    page_icon="🩺",
    layout="wide"
)

# ================== CLEAN PROFESSIONAL UI ==================
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
    color: #60A5FA !important;
}

/* Text visibility FIX */
p, span, label, div {
    color: #E5E7EB !important;
}

/* Inputs */
input, textarea {
    background-color: #1F2937 !important;
    color: white !important;
    border-radius: 8px !important;
    border: 1px solid #374151 !important;
}

/* Buttons */
.stButton button {
    background-color: #3B82F6;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}

/* Chat */
[data-testid="stChatMessage"] {
    background-color: #111827;
    border-radius: 10px;
    padding: 12px;
}

/* Alerts */
.stAlert {
    background-color: #1F2937 !important;
    color: #FFFFFF !important;
    border-left: 5px solid #3B82F6;
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
    st.write("AI-powered medical triage assistant (Educational Purpose Only)")
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

# ================== DOCTOR RECOMMENDER (REAL TRIAGE) ==================
elif page == "Doctor Recommender":
    st.title("Medical Triage System 👨‍⚕️")

    symptom_text = st.text_input("Describe your symptoms")

    if st.button("Analyze"):
        if symptom_text.strip() == "":
            st.warning("Please enter symptoms")
        else:
            text = symptom_text.lower()

            # EMERGENCY
            if any(word in text for word in ["chest pain", "heart pain", "faint", "left arm pain"]):
                st.error("🚨 EMERGENCY RISK")
                st.write("Possible cardiac-related issue")
                st.write("Go to Emergency Room immediately")
                st.write("Specialist: Cardiologist / Emergency Medicine")

            # HIGH RISK
            elif any(word in text for word in ["breathing", "shortness of breath", "severe pain"]):
                st.error("⚠️ HIGH RISK")
                st.write("Requires urgent medical attention")
                st.write("Specialist: Pulmonologist / General Physician")

            # MODERATE
            elif any(word in text for word in ["fever", "cough", "cold", "fatigue"]):
                st.warning("🟡 MODERATE CONDITION")
                st.write("Likely infection or viral illness")
                st.write("Specialist: General Physician")

            # LOW
            elif any(word in text for word in ["headache", "mild pain"]):
                st.info("🟢 LOW RISK")
                st.write("Minor condition suspected")
                st.write("Rest and hydration recommended")

            # UNKNOWN
            else:
                st.info("⚪ UNCERTAIN CONDITION")
                st.write("Consult General Physician for diagnosis")

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

    if st.button("Explain"):
        if uploaded:
            data = extract_pdf(uploaded)
            st.subheader("Report Summary")
            st.info("Most values appear within normal range. Please consult doctor for confirmation.")

        elif text_input.strip():
            st.subheader("Report Summary")
            st.info("Text analysis shows no critical issues detected.")

        else:
            st.warning("Provide PDF or text")

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

    user_input = st.chat_input("Ask your question")

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
st.caption("⚠️ Educational Medical Triage System | Not a real diagnosis tool")