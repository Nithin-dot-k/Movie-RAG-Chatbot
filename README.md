# 🎬 Movie RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** based chatbot that provides intelligent movie recommendations using a dataset and vector search.

This project combines **LLM + Vector Database + Structured Movie Data** to answer user queries accurately.

---

## 🚀 Features

- 🎥 Movie recommendation based on user queries
- 🧠 RAG-based intelligent responses
- ⚡ Fast semantic search using vector embeddings
- 📊 CSV dataset integration
- 🔍 Filter movies by year, OTT platform, genre, etc.

---

## 🧠 How It Works

1. User enters a query  
   _(e.g., "Give me action movies on Netflix in 2020")_

2. Query is converted into embeddings

3. Vector database retrieves relevant movie data

4. Retrieved data is passed to LLM

5. LLM generates a meaningful response

---

## ⚙️ Tech Stack

- **Python**
- **LangChain**
- **ChromaDB (Vector Database)**
- **Pandas**
- **LLM (OpenAI / Local Model)**

---

## 📂 Project Structure

Movie-RAG-Chatbot/
│── main.py # Main chatbot logic
│── vector.py # Vector database creation & retrieval
│── movies_details.csv # Movie dataset
│── requirements.txt # Dependencies
│── README.md # Project documentation

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Nithin-dot-k/Movie-RAG-Chatbot.git
cd Movie-RAG-Chatbot

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the project
python main.py

💡 Example Queries
“Movies on Netflix in 2020”
“Action movies by Christopher Nolan”
“Top comedy movies in India”
“Give me thriller movies after 2015”
📸 Sample Output

👉 (Add your screenshot here for better presentation)

Example:

User: Movies on Netflix in 2020

Bot:
- Movie Title: Extraction
- Genre: Action
- Director: Sam Hargrave
- Platform: Netflix

🔥 Key Concepts Used
RAG (Retrieval-Augmented Generation)
Combines retrieval of relevant data with LLM generation
Vector Embeddings
Converts text into numerical vectors for similarity search
Semantic Search
Finds meaning-based results instead of keyword matching
```
