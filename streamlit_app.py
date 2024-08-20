import streamlit as st
import google.generativeai as genai
from pdfminer.high_level import extract_text

# Configure the Generative AI model
api_key = "AIzaSyDYKhQRaQY38yBpH0ZBKpgwMpfSiABgE5c"  # Ensure this API key is correct and valid
genai.configure(api_key=api_key)

# Define the Generative AI model and configuration
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    },
  system_instruction="Generate notes on the given text\nRULES:\ndo not add new information and do not remove important details\nreturn as raw text withotu format",
)

st.title("🎈 My PDF Text Extractor App")
st.write(
    "Upload a PDF to extract its text and get insights from the AI."
)

# File uploader for PDF
uploaded_file = st.file_uploader('Choose your PDF file', type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    extracted_text = extract_text(uploaded_file)
    
    # Display the extracted text
    st.text_area("Extracted Text", extracted_text, height=300)
    
    # Create a chat session with the AI model
    chat_session = model.start_chat(history=[])

    # Send the extracted text to the AI model
    try:
        response = chat_session.send_message(extracted_text)
        # Display the AI-generated response
        st.text_area("AI Response", response.text, height=300)
    except Exception as e:
        st.error(f"Error while processing text with AI: {e}")
