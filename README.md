# 📚 Personalized Learning Assistant

**A Retrieval-Augmented Generation (RAG) AI-powered learning assistant that answers educational queries using curated study materials.**

---

## 🚀 Features
- **Retrieval-Augmented Generation (RAG):** Enhances responses with relevant context from study materials.
- **FastAPI Backend:** Handles AI query processing and vector search.
- **Streamlit UI:** Simple web-based chatbot interface for asking questions.
- **FAISS Vector Store:** Efficient similarity search for retrieving relevant content.
- **Modular Architecture:** Separate components for ingestion, backend, and UI.

---

## 📂 Project Structure
```
learning-assistant/
│── ingestion/          # Data ingestion & embedding storage
│   ├── data_ingestion.py   # Script to load, split, and store embeddings
│   ├── study_material.txt  # Sample study material (text file)
│   ├── vector_store/       # Folder to store FAISS index
│
│── backend/           # API & business logic
│   ├── main.py          # FastAPI backend
│   ├── requirements.txt # Backend dependencies
│   ├── config.py        # Configuration settings
│
│── ui/                # User interface (Streamlit frontend)
│   ├── app.py          # Streamlit UI
│   ├── assets/         # UI assets (images, icons, etc.)
│
│── env/               # Virtual environment (not committed to Git)
│── .env               # API keys & environment variables
│── .gitignore         # Ignore unnecessary files
│── README.md          # Documentation
```

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/learning-assistant.git
cd learning-assistant
```

### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r backend/requirements.txt
pip install -r ui/requirements.txt
```

### **4️⃣ Generate Study Material Embeddings**
```bash
cd ingestion
python data_ingestion.py
```

### **5️⃣ Start Backend (FastAPI)**
```bash
cd ../backend
uvicorn main:app --reload
```

### **6️⃣ Start UI (Streamlit)**
```bash
cd ../ui
streamlit run app.py
```

---

## 🔍 Usage
- **Ask a question** through the Streamlit interface.
- The system retrieves **relevant study material** from FAISS.
- The AI generates an answer **strictly based on study material** (to prevent hallucination).

---

## 🛠 Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Vector Store:** FAISS
- **LLM:** OpenAI GPT-4 (or LLaMA/Mistral)
- **Embeddings:** OpenAI's `text-embedding-ada-002`

---

## 📌 Example Queries
### ✅ **Valid Queries (Covered in Study Material)**
- *What is supervised learning?*
- *Explain reinforcement learning with an example.*
- *How does a decision tree work?*

### ❌ **Negative Test Cases (Out-of-Scope Queries)**
- *Who discovered the theory of relativity?* (Not in study material)
- *Explain the history of blockchain.* (Irrelevant to ML topics)
- *What are the latest AI trends?* (Not covered in study material)

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Feel free to fork this repository, submit issues, or create pull requests to enhance functionality!