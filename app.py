import streamlit as st
from utils import generate_code, highlight_code
from templates import get_code_template
from auth import user_authentication
from config import OPENAI_API_KEY
import openai

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

# Streamlit UI components
st.title("AI-Powered Code Generator")

# User Authentication
user_logged_in = user_authentication()

if user_logged_in:
    # Multi-language support dropdown
    languages = ["Python", "JavaScript", "HTML", "CSS"]
    selected_language = st.selectbox("Select programming language", languages)

    # Code templates selection
    template = st.selectbox("Select Code Template", list(get_code_template().keys()))
    template_code = get_code_template()[template]
    
    st.code(template_code, language=selected_language.lower())

    # Text input for user query
    query = st.text_area("Describe what you want to generate:")

    # Generate code button
    if st.button("Generate Code"):
        if query:
            prompt = f"Generate a {selected_language} code that does the following: {query}"
            generated_code = generate_code(prompt, selected_language)

            # Highlighting code
            highlighted_code = highlight_code(generated_code, selected_language)
            st.markdown(f'<div style="overflow-x: auto;">{highlighted_code}</div>', unsafe_allow_html=True)

            # Show explanation option
            if st.checkbox("Show Code Explanation"):
                explanation = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"Explain this {selected_language} code:\n{generated_code}",
                    max_tokens=300,
                    temperature=0.7
                )
                st.write(explanation.choices[0].text.strip())

            # Copy and Save Options
            if st.button("Copy to Clipboard"):
                st.text(generated_code)

            if selected_language == "Python":
                st.download_button("Download Python Code", generated_code, file_name="generated_code.py")
            elif selected_language == "HTML":
                st.download_button("Download HTML Code", generated_code, file_name="generated_code.html")
else:
    st.write("Please log in to generate code.")
