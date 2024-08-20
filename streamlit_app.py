import streamlit as st
import google.generativeai as genai
import os
from pdfminer.high_level import extract_text

genai.configure(api_key=["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎈 My PDF Text Extractor App")
st.write(
    "Let's start extracting text from your PDF file! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

uploaded_file = st.file_uploader('Choose your PDF file', type="pdf")

generation_config = {
  "temperature": 0.8,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Generate notes on the given text, the MANDATORY RULES = DO NOT change , remove, or add information\n",
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("extracted_text")

print(response.text)

if uploaded_file is not None:
    extracted_text = extract_text(uploaded_file)
    
    st.text_area("Extracted Text", response.text, height=300)