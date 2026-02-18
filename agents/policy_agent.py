import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

# Build vector store once
def build_vectorstore():
    documents = []

    for file in os.listdir("data/policies"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"data/policies/{file}")
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    splits = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(splits, embeddings)

    return vectorstore


vectorstore = build_vectorstore()


def get_policy_response(query: str):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    docs = vectorstore.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a company policy assistant.

    Use ONLY the context below to answer the question.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content
