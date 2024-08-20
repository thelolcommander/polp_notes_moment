import streamlit as st
import google.generativeai as genai
import os
from pdfminer.high_level import extract_text

genai.configure(api_key=os.environ["AIzaSyBlkU-ZjWk29YFFsjj2hqbhFg8CGU0jVRw"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎈 My PDF Text Extractor App")
st.write(
    "Let's start extracting text from your PDF file! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

uploaded_file = st.file_uploader('Choose your PDF file', type="pdf")

if uploaded_file is not None:
    extracted_text = extract_text(uploaded_file)
    
    st.text_area("Extracted Text", extracted_text, height=300)

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
    {
      "role": "user",
      "parts": [
        "History of Programming\nFORTRAN\nIBM Mathematical Formula Translating System (FORTRAN): Developed by John Backus' team at IBM in the 1950s for scientific and engineering applications on the IBM704.\nPurpose: General-purpose, procedural, imperative language suited for numeric computation and scientific computing.\nKey Features:\nComments, assignment statements, control structures (conditional, loop).\nSubroutines and functions, I/O formatting, machine-independent code, arrays.\nPioneered compiler development, optimizing compilers, and procedural programming.\nSuccess Factors:\nEfficient use of programmer time, easy to learn, and heavily supported by IBM.\nStill popular in high-performance computing and benchmarks for supercomputers.\nVersions:\nFortran 0 (1954): Basic constructs like assignment, if, goto, do loop.\nFortran I (1955-1957): First implemented compiler.\nFortran II (1958): Procedural programming, pass by reference, independent subroutine compilation.\nFortran IV (1961-1962): Machine independence, logical operations, explicit type declarations.\nFortran 66 (1966): First standard based on Fortran IV.\nCOBOL\nCOmmon Business-Oriented Language: Designed for business, finance, and administrative systems.\nOrigin: Created in 1959 by Grace Hopper and others, inspired by FLOW-MATIC and COMTRAN.\nKey Features:\nEnglish-like syntax, ease of use for business people, emphasis on data description.\nMachine-dependent (environment division) and independent data descriptions.\nMacros, hierarchical data structures, descriptive variable names, I/O formatting.\nChallenges:\nPoor early compiler performance, limited influence on subsequent languages, primarily used for business data applications.\nLanguage evolution was limited due to its strong standardization.\nLegacy: Despite its age, COBOL remains crucial in many business and government systems worldwide.\nLISP\nOrigin: Created by John McCarthy in 1958, influenced by Alonzo Church’s lambda calculus.\nKey Contributions:\nPioneered functional programming, tree data structures, automatic storage management, and dynamic typing.\nSelf-hosting compiler (eval function) enables reflective programming.\nStrongly associated with artificial intelligence, common variants include Scheme and Common Lisp.\nKey Features:\nEmphasizes symbolic computations, recursion, and linked lists.\nSupports functional programming where all computations are function-based.\nPioneered languages like ML, Miranda, Haskell, and F#.\nALGOL\nALGOrithmic Language: A family of imperative languages developed in the mid-1950s, heavily influencing many others.\nDevelopment: Joint effort by American (ACM) and European (GAMM) experts.\nGoals:\nMachine independence, mathematical notation, algorithm description, and ease of translation to machine instructions.\nKey Innovations:\nIntroduced code blocks, local variables, structured control statements, recursion, dynamic arrays, and memory allocation.\nFirst language to use formal notation (BNF) for syntax description.\nVersions:\nALGOL-58: Initially called IAL, implemented mainly in Europe.\nALGOL-60: Introduced lexical scoping, pass by value/name, and recursion; influenced many languages.\nALGOL-68: Added advanced features like array slicing, typecasting, and parallel processing but became too complex.\nALGOL-W (1966): Early development of Pascal by Niklaus Wirth.\nPASCAL\nOrigin: Designed by Niklaus Wirth in 1968-1969, published in 1970; named after Blaise Pascal.\nPurpose: Encourage structured programming and data structuring.\nFeatures:\nBased on ALGOL-60, includes array control structures, user-defined types, records, case statements, pointers, enumerations, and sets.\nInspired by SIMULA 67, ALGOL-68, and Wirth’s earlier work (EULER, ALGOL-W).\nLegacy:\nWidely used in education for teaching structured programming.\nLed to Object Pascal, used in Delphi for object-oriented programming.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## History of Programming Languages:\n\n**FORTRAN**\n\n* **Developed by:** John Backus' team at IBM in the 1950s.\n* **Purpose:** Scientific and engineering applications.\n* **Key Features:**\n    * General-purpose, procedural, imperative language.\n    * Numeric computation and scientific computing focus.\n    * Comments, assignment statements, control structures (conditional, loop).\n    * Subroutines and functions, I/O formatting, machine-independent code, arrays.\n* **Success Factors:**\n    * Efficient use of programmer time.\n    * Easy to learn.\n    * Heavily supported by IBM.\n* **Versions:**\n    * Fortran 0 (1954): Basic constructs.\n    * Fortran I (1955-1957): First compiler implementation.\n    * Fortran II (1958): Procedural programming, pass by reference, independent subroutine compilation.\n    * Fortran IV (1961-1962): Machine independence, logical operations, explicit type declarations.\n    * Fortran 66 (1966): First standard based on Fortran IV.\n* **Legacy:** Still popular in high-performance computing and benchmarks for supercomputers.\n\n**COBOL**\n\n* **Developed by:** Grace Hopper and others in 1959.\n* **Purpose:** Business, finance, and administrative systems.\n* **Key Features:**\n    * English-like syntax.\n    * Ease of use for business people.\n    * Emphasis on data description.\n    * Machine-dependent (environment division) and independent data descriptions.\n    * Macros, hierarchical data structures, descriptive variable names, I/O formatting.\n* **Challenges:**\n    * Poor early compiler performance.\n    * Limited influence on subsequent languages.\n    * Primarily used for business data applications.\n    * Limited language evolution due to strong standardization.\n* **Legacy:** Remains crucial in many business and government systems worldwide.\n\n**LISP**\n\n* **Developed by:** John McCarthy in 1958.\n* **Key Contributions:**\n    * Pioneered functional programming.\n    * Tree data structures, automatic storage management, and dynamic typing.\n    * Self-hosting compiler (eval function) enabling reflective programming.\n* **Key Features:**\n    * Emphasizes symbolic computations, recursion, and linked lists.\n    * Supports functional programming where all computations are function-based.\n* **Legacy:** Strongly associated with artificial intelligence. Common variants include Scheme and Common Lisp. Pioneered languages like ML, Miranda, Haskell, and F#.\n\n**ALGOL**\n\n* **Development:** Joint effort by American (ACM) and European (GAMM) experts in the mid-1950s.\n* **Goals:**\n    * Machine independence.\n    * Mathematical notation.\n    * Algorithm description.\n    * Ease of translation to machine instructions.\n* **Key Innovations:**\n    * Introduced code blocks, local variables, structured control statements, recursion, dynamic arrays, and memory allocation.\n    * First language to use formal notation (BNF) for syntax description.\n* **Versions:**\n    * ALGOL-58: Initially called IAL, implemented mainly in Europe.\n    * ALGOL-60: Introduced lexical scoping, pass by value/name, and recursion; influenced many languages.\n    * ALGOL-68: Added advanced features but became too complex.\n    * ALGOL-W (1966): Early development of Pascal by Niklaus Wirth.\n\n**PASCAL**\n\n* **Developed by:** Niklaus Wirth in 1968-1969, published in 1970.\n* **Purpose:** Encourage structured programming and data structuring.\n* **Features:**\n    * Based on ALGOL-60, includes array control structures, user-defined types, records, case statements, pointers, enumerations, and sets.\n    * Inspired by SIMULA 67, ALGOL-68, and Wirth's earlier work (EULER, ALGOL-W).\n* **Legacy:** Widely used in education for teaching structured programming. Led to Object Pascal, used in Delphi for object-oriented programming. \n",
      ],
    },
  ]
)

response = chat_session.send_message("extracted_text")

print(response.text)