# GenAI Multi-Agent Customer Support System

A Generative AI-powered multi-agent system designed to assist customer support executives in retrieving both structured and unstructured data using natural language queries. This system allows users to interact with customer data in SQL databases and company policy documents (PDFs) through a unified chatbot interface.

---

## 🚀 Project Overview

Customer support executives often face difficulties in accessing and summarizing information spread across multiple systems and documents. This project solves that problem by implementing:

1. **Policy Agent** – Handles unstructured documents (PDFs) such as company policies and delivers context-aware answers.
2. **SQL Agent** – Handles structured customer data (SQL database) and provides natural language summaries.
3. **Router** – Determines which agent should handle the query.
4. **Streamlit UI** – A simple interface to interact with the system.

---

## 🏗️ System Architecture

  ```pgsql
                                              +---------------------------+
                                              |       Streamlit UI        |
                                              |  (User Natural Language)  |
                                              +---------------------------+
                                                             |
                                                             v
                                                  +-------------------+
                                                  |   Query Router    |
                                                  |  (Intent Logic)   |
                                                  +-------------------+
                                                     |             |
                                      ----------------              ----------------
                                      |                                              |
                                      v                                              v
                          +---------------------------+              +------------------------------+
                          |        SQL Agent          |              |        Policy Agent          |
                          | (Structured Data Handler) |              | (RAG - Unstructured PDFs)    |
                          +---------------------------+              +------------------------------+
                                      |                                              |
                                      v                                              v
                          +---------------------------+              +------------------------------+
                          |     SQLite Database       |              |   FAISS Vector Store         |
                          | (Customers & Tickets)     |              |  (Embedded PDF Chunks)       |
                          +---------------------------+              +------------------------------+
                                                     \                /
                                                      \              /
                                                       v            v
                                               +---------------------------+
                                               |     Groq LLM (Llama 3)    |
                                               |   Response Generation     |
                                               +---------------------------+
```

**Key Features:**

- Natural language query handling.
- Retrieval-Augmented Generation (RAG) for PDFs.
- Structured query processing via SQL database.
- Multi-agent routing for context-aware answers.

---

## 💻 Tech Stack

- **LLM:** Groq (`llama-3.3-70b-versatile`)  
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)  
- **Vector Store:** FAISS  
- **Database:** SQLite (for structured customer data)  
- **Web UI:** Streamlit  
- **Python Libraries:** LangChain, LangChain-Groq, langchain-embeddings, pypdf, python-dotenv, SQLAlchemy  

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/genai-multi-agent-support-system.git
cd genai-multi-agent-support-system
```

2. **Create a virtual environment and activate it**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add environment variables** <br>

Create a `.env` file in the project root that contains the Groq API key:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

5. **Prepare data**
* Place policy PDFs in data/policies/
* Ensure the SQLite database support.db exists in the project root with sample customer data.

## 🛠️ Running the Application
```bash
streamlit run app.py
```

* Open the URL displayed in the terminal (usually http://localhost:8501)
* Enter a natural language query in the input box and press Enter.

Example Queries:
1. Policy questions:

   * "What is the refund policy?"
   * "What is the method of payment for refunds?"
   * "Under what conditions are refunds granted at 70%?"

2. Customer data questions:

   * "Give me an overview of customer Ema Johnson and her support tickets."
   * "Show all open tickets for Daniel Lee."
   * "Which customers currently have resolved tickets?"

## ⚡ Notes
* The `k` parameter in similarity search determines how many PDF chunks are considered. Default is 3; increase if you want more context from multiple documents.
* Some complex aggregation queries in SQL may need simpler phrasing to ensure accurate responses.
* The system is designed for demo purposes with synthetic customer data.

## 📹 Demo
A video demo showcasing the functionality of the multi-agent system can be found here:<br>
[Demo Video]([PASTE_YOUR_GOOGLE_DRIVE_LINK_HERE](https://drive.google.com/file/d/1Cdzox8qT7x6nyBXPpXwP5ShUGGjIpTXa/view?usp=sharing))

## 📝 Author
Bethel Unwan – Software Developer
<br> Project submitted for: TCS GenAI Developer Assessment
