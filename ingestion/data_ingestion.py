import os
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

#load environment variables
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# load and process documents
def load_documents(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# split text into chunks for vector search
def split_text(text, chunk_size=500, overlap = 50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return text_splitter.split_text(text)

# store embeddings
def store_embeddings(text):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_db = FAISS.from_texts(text, embeddings)
    vector_db.save_local("vector_store") # store embeddings locally
    print("text indexed")

if __name__ == "__main__":
    text = load_documents("notes.txt")
    text_chunks = split_text(text)
    store_embeddings(text_chunks)

