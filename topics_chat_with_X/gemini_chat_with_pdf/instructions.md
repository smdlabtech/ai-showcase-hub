
# 🤖 Chat with PDF Files using Gemini AI  

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-red?style=flat&logo=streamlit)
![AI-Powered](https://img.shields.io/badge/AI-Gemini-orange?style=flat&logo=google)

## 📌 Project Overview  

This project is a **Streamlit-based AI-powered chatbot** that enables users to interact with **PDF files** using **Gemini AI**.  

✅ **Upload and extract text from PDFs**  
✅ **Ask questions about the content**  
✅ **Get AI-powered responses from Gemini**  
✅ **Export conversations to CSV for future reference**  

---

## 🏗️ How It Works  

1️⃣ **Upload a PDF file**  
   - Uses `PyMuPDF (fitz)` to extract text.  
   - Stores files in a `data` folder.  

2️⃣ **Select & Preview PDF Content**  
   - View extracted text directly in Streamlit.  

3️⃣ **Ask Questions About the PDF**  
   - Sends the text and user query to **Gemini AI**.  
   - Receives an intelligent response based on the document content.  

4️⃣ **Export Results**  
   - Save interactions as a `.csv` file.  

---

## 🛠️ Technologies Used  

- **Python 3.8+**  
- **Streamlit** (Frontend UI)  
- **PyMuPDF (fitz)** (PDF text extraction)  
- **Google Gemini AI** (Text analysis & responses)  
- **Pandas** (Data processing & CSV export)  

---

## 📂 Directory Structure  

```bash
📦 pdf_chatbot  
 ┣ 📂 pdf_history  
 ┃ ┣ 📂 data  # Stores uploaded PDFs  
 ┣ 📜 app.py  # Streamlit App  
 ┣ 📜 requirements.txt  
```



