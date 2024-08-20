import streamlit as st
import google.generativeai as genai
from pdfminer.high_level import extract_text

api_key = "AIzaSyDYKhQRaQY38yBpH0ZBKpgwMpfSiABgE5c"
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.8,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    },
  system_instruction="Generate notes on the given text\nRULES:\ndo not add new information and do not remove important details\nmake do not add text formatting\nbut you can add \"-\" for bullets",
)

st.title("🎈 My PDF Text Extractor App")
st.write(
    "Upload a PDF to extract its text and get insights from the AI."
)

uploaded_file = st.file_uploader('Choose your PDF file', type="pdf")

if uploaded_file is not None:
    extracted_text = extract_text(uploaded_file)
    
    st.subheader("Extracted Text")
    st.text_area("Extracted Text", extracted_text, height=300, disabled=True)
    
    chat_session = model.start_chat(history=[])

    try:
        response = chat_session.send_message(extracted_text)
        
        st.subheader("AI Response")
        st.text_area("AI Response", response.text, height=300, disabled=True)
    except Exception as e:
        st.error(f"Error while processing text with AI: {e}")
