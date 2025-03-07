# 🚀 AI-Powered Chatbots

This repository showcases multiple **AI-driven chatbots**, each designed for a specific use case. Built using **Google Gemini**, **Streamlit**, and **FAISS**, these chatbots demonstrate expertise in **NLP, embeddings, vector search, and AI-driven document/image analysis**.

## 🔥 Key Features

✅ **AI-powered responses** using **Gemini models**  
✅ **Streamlit UI** for seamless interaction  
✅ **PDF Q&A chatbot** with **FAISS vector search**  
✅ **Invoice Reader** using **OCR (Tesseract) & AI-powered insights**   
✅ **Conversational memory** for better user engagement  
✅ **Multi-modal AI** (text + image processing)

---

## 📌 Project Breakdown

### 1️⃣ **General Q&A Chatbot** (`app.py`)
*   Uses **Gemini-1.5-pro-latest** to generate responses.
*   Simple **text-based** interaction with AI.

### 2️⃣ **PDF Chatbot** (`pdf_chat.py`)
*   Allows users to **upload PDFs** and ask questions.
*   Uses **LangChain, FAISS, and Gemini embeddings** to fetch relevant answers.
*   Supports **large document processing** efficiently.

### 3️⃣ **Invoice Reader Chatbot** (`invoice_reader.py`)
*   Uses **OCR (Tesseract via pytesseract)** and AI-powered insights to analyze invoices.
*   Extracts key details like **invoice number, total amount, due date, and vendor details**.
*   Utilizes **Gemini-1.5-pro-latest** for **context-aware document understanding**.
*   **Real-world application:** Can be used in **financial automation** or **business workflows**.

### 4️⃣ **Chatbot with History** (`chat_history.py`)
*   Maintains **chat history** for conversational memory.
*   Uses Streamlit’s session state for **persistent context**.
*   Supports long-form AI conversations.

### 5️⃣ **Multi-Modal AI Chatbot** (`image_text_chat.py`)
*   Accepts **both text and image inputs**.
*   Uses **Gemini-1.5-flash** for **faster responses**.
*   Processes images using **PIL (Python Imaging Library)**.

---

## 💡 Skills & Technologies Used

*   **Google Gemini API** for NLP and multi-modal AI
*   **LangChain** for document processing
*   **FAISS (Facebook AI Similarity Search)** for **efficient vector search**
*   **Streamlit** for creating interactive AI-powered web apps
*   **OCR (Optical Character Recognition) via Tesseract & pytesseract** for invoice analysis
*   **Environment Variables (.env)** for secure API key management

---

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/arnavjoshi/ai-chatbots.git
cd ai-chatbots

# Install dependencies
pip install -r requirements.txt

# Run the chatbot app
streamlit run app.py
```

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📩 Contact
For any queries or collaborations, feel free to reach out:
📧 Email: arnavjoshi020@gmail.com  
🔗 LinkedIn: [[linkedin.com/in/arnavjoshi](https://linkedin.com/in/arnavjoshi)](https://www.linkedin.com/in/arnav-joshi-038693291/)
