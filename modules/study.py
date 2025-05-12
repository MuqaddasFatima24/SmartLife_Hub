import streamlit as st
import random

class StudyAssistant:
    def __init__(self, text):
        self.text = text.strip()
        self.sentences = self.text.split(". ")
        self.word_count = len(self.text.split())
        
    def summarize(self, num_sentences=3):
        if not self.sentences:
            return "Hmm... I couldn't find enough content to summarize."
        return ". ".join(self.sentences[:num_sentences]) + "."
    
    def generate_flashcards(self):
        flashcards = [s.strip() for s in self.sentences if len(s.strip()) > 10][:5]
        if flashcards:
            return flashcards
        return ["Not enough content for flashcards. Consider adding more details."]
    
    def question_answer(self, question):
        question = question.lower()
        for sentence in self.sentences:
            if question.split()[0] in sentence.lower() or any(word in sentence.lower() for word in question.split()):
                return f"🔍 Found an answer: {sentence}"
        return "🤔 Hmm... I couldn't find an answer. Could you try rephrasing your question?"

    def extract_concepts(self):
        return [word.strip().capitalize() for word in self.text.split() if len(word) > 7][:5]

    def study_plan(self):
        if self.word_count < 100:
            return "📖 Quick 15-minute review session."
        elif self.word_count < 300:
            return "⏰ Focused 30-minute study session."
        else:
            return "🧠 In-depth 45+ minute study session with breaks."

    def random_tip(self):
        tips = [
            "🧩 Break topics into smaller chunks for easier digestion.",
            "🎯 Set small, clear goals for better focus.",
            "📴 Eliminate distractions to enhance concentration.",
            "🔁 Regular revision is key to retaining information.",
            "🛌 Don't forget to rest your mind. It’s important!"
        ]
        return random.choice(tips)

    def analyze_text(self):
        num_sentences = len(self.sentences)
        avg_length = round(self.word_count / num_sentences, 2) if num_sentences > 0 else 0
        long_words = [word for word in self.text.split() if len(word) > 8]
        return {
            "Total Sentences": num_sentences,
            "Average Sentence Length (words)": avg_length,
            "Long Words (8+ chars)": len(long_words)
        }

def show_study_ui(st):
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Inter:wght@400;600&display=swap');
            html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f5f3ef; color: #2e2e2e; }
            .study-header { font-family: 'Playfair Display', serif; font-size: 2em; font-weight: 600; text-align: center; color: #3a3a3a; padding: 20px 0; border-bottom: 2px solid #e0ddd7; }
            .stButton button { background-color: #a67c52; color: white; border: none; border-radius: 8px; padding: 0.5em 1.5em; font-weight: 600; transition: 0.3s ease; }
            .stButton button:hover { background-color: #8b6e45; }
            .stTextInput input, .stTextArea textarea { border-radius: 8px; padding: 0.5em; border: 1px solid #d8d4ce; }
            .stSelectbox div { background-color: #fffaf6; border-radius: 12px; padding: 10px; border: 1px solid #d8d4ce; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="study-header">📚 AI Study Assistant</div>', unsafe_allow_html=True)
    st.markdown("I’m here to help you summarize, understand, and plan your study sessions. Let’s make studying more efficient and fun!")

    text = st.text_area("✍️ Paste your study content here:", height=200)

    if st.button("🧠 Analyze Content"):
        if text.strip():
            assistant = StudyAssistant(text)
            analysis = assistant.analyze_text()
            st.markdown("### 📊 Content Analysis:")
            for key, value in analysis.items():
                st.markdown(f"- **{key}:** {value}")
        else:
            st.warning("Please provide some content first. I can't analyze an empty page!")

    if text.strip():
        assistant = StudyAssistant(text)

        st.markdown(f"📝 **Word Count:** {assistant.word_count}")
        st.markdown(f"📅 **Suggested Study Plan:** {assistant.study_plan()}")

        if st.button("🔍 Generate Summary"):
            if assistant.word_count < 20:
                st.warning("It seems your content is a bit short. Try with at least 20 words.")
            else:
                with st.spinner("⏳ Summarizing..."):
                    st.success("✅ Summary Generated!")
                    st.markdown(assistant.summarize())

        if st.button("📌 Create Flashcards"):
            flashcards = assistant.generate_flashcards()
            st.info("🧠 Flashcards:")
            for i, card in enumerate(flashcards, 1):
                st.markdown(f"**{i}.** {card}")

        st.markdown("### ❓ Ask Me Anything:")
        user_q = st.text_input("What do you want to ask about the content?")
        if user_q:
            answer = assistant.question_answer(user_q)
            st.success(f"💬 Answer: {answer}")

        st.markdown("### 📘 Key Concepts Highlighted:")
        st.markdown(", ".join(assistant.extract_concepts()) or "No significant concepts found. Try providing longer content.")

        st.markdown("### 💡 Tip of the Day:")
        st.markdown(assistant.random_tip())

        st.markdown("---")
        st.info("🚀 More features are coming soon: revision scheduler, quiz generator, and peer Q&A system!")

