
import os
import streamlit as st
import pandas as pd
import fitz
import google.generativeai as genai

# 📂 Define directories
ROOT_DIR = os.path.join(os.getcwd(), "pdf_history")
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  # Create folder if it does not exist

# 📌 Streamlit Interface
st.set_page_config(page_title="Chat with PDF Files", layout="wide")
st.title("🤖Chat with PDF Files using Gemini AI")

# 📌 Enter Gemini API Key
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

# 📌 Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    
    for page_num, page in enumerate(doc):
        text += f"\n--- Page {page_num + 1} ---\n"
        text += page.get_text("text")
    
    return text.strip()

# 📌 Load PDF files
def load_pdf_files(folder):
    pdf_files = [f for f in os.listdir(folder) if f.endswith(".pdf")]
    extracted_data = {}

    for file in pdf_files:
        file_path = os.path.join(folder, file)
        extracted_data[file] = extract_text_from_pdf(file_path)

    return extracted_data

# 📌 Function to interact with Gemini AI
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# 📌 File Upload via Streamlit
uploaded_file = st.sidebar.file_uploader("📂 Upload a PDF file", type=["pdf"])

if uploaded_file:
    file_path = os.path.join(DATA_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"✅ File {uploaded_file.name} uploaded successfully!")

# 📌 Load PDF files
pdf_data = load_pdf_files(DATA_DIR)

if pdf_data:
    st.sidebar.success(f"📄 {len(pdf_data)} PDF files available.")

    # 📌 Select a PDF file
    selected_file = st.sidebar.selectbox("📑 Select a file", list(pdf_data.keys()))

    # 📌 Display extracted content
    if selected_file:
        # st.subheader(f"📃 Content of: {selected_file}")
        st.subheader(f"📃 Content of: {selected_file}")
        st.text_area("Extracted text:", pdf_data[selected_file][:5000], height=300)  # Limit display

        # 📌 Ask a question about the PDF
        st.subheader("💬 Ask a question about this file")
        user_query = st.text_input("Enter your question")

        if st.button("🚀 Submit Question") and api_key:
            with st.spinner("Analyzing..."):
                full_prompt = f"Here is the content of a PDF file:\n{pdf_data[selected_file]}\n\nAnswer this question: {user_query}"
                response = ask_gemini(full_prompt)
                st.write("**🧠 Gemini's Response:**")
                st.markdown(response)

            # 📌 Export results to CSV
            if st.button("📤 Export to CSV"):
                df = pd.DataFrame([{"File": selected_file, "Question": user_query, "Response": response}])
                csv_path = os.path.join(DATA_DIR, "chat_results.csv")
                df.to_csv(csv_path, index=False, encoding="utf-8")
                st.success(f"✅ Export successful! File saved as: {csv_path}")

else:
    st.sidebar.warning("⚠️ No PDF files found in the 'data' folder.")
