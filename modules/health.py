import streamlit as st
from modules.disease_data import DISEASES

class SymptomAnalysis:
    def __init__(self, user_input):
        self.user_input = user_input.strip()
        self.found_disease = None

    def analyze_symptoms(self):
        if not self.user_input:
            return None, "Please describe your symptoms or condition."
        
        for disease in DISEASES:
            if disease.matches(self.user_input):
                self.found_disease = disease
                return disease, None
        
        return None, "❌ No matching disease found. Please consult a doctor."

class SymptomCheckerUI:
    def __init__(self):
        self.user_input = ""
        self.disease_info = None
        self.error_message = ""

    def display_ui(self):
        st.subheader("🩺 SmartHealth - Symptom Checker")
        self.user_input = st.text_area("Describe your symptoms or condition", "")

        if st.button("Analyze"):
            analysis = SymptomAnalysis(self.user_input)
            self.disease_info, self.error_message = analysis.analyze_symptoms()

            if self.error_message:
                st.warning(self.error_message)
            elif self.disease_info:
                self._display_disease_info()

    def _display_disease_info(self):
        # Display disease details..
        st.success(f"Possible Match: **{self.disease_info.name}**")
        st.markdown(f"**Symptoms:** {', '.join(self.disease_info.symptoms)}")
        st.markdown(f"**Medication:** {self.disease_info.medication}")
        st.markdown(f"**Precautions:** {self.disease_info.precautions}")
        st.markdown(f"**Tips:** {self.disease_info.tips}")


def get_health_ui():
    checker_ui = SymptomCheckerUI()
    checker_ui.display_ui()
