import os
from http.client import HTTPException

from fastapi import FastAPI, HTTPException
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#initialize FastAPI
app = FastAPI()

#load stored vector database
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vector_db = FAISS.load_local("../ingestion/vector_store", embeddings
                             , allow_dangerous_deserialization=True)  #trust the FAISS index files generated earlier

#Initialize LLM
llm = ChatOpenAI(model_name="gpt-4",openai_api_key=OPENAI_API_KEY)

@app.get("/ask/")
async def ask_question(query: str):
    try:
        #defne a confidence threshold
        min_retrieval_threshold = 0.1

        # Retrieve relevant docs
        docs_with_score = vector_db.similarity_search_with_score(query, k = 3)

        # filter docs that meet confidence
        filtered_docs = [doc for doc, score in docs_with_score if score > min_retrieval_threshold]

        if not filtered_docs: # there are no high confidence documents to prevent hallucination
            return {"question" : query, "answer": "I cannot find relevant information in the notes provided."}

        context = "\n".join([doc.page_content for doc in filtered_docs])

        if not context.strip(): # fallback response if no relevant retrieval
            return {"question": query, "answer": "I cannot find relevant information in the notes provided."}

        # Generate response from LLM
        prompt =  f"""
        You are an AI that only answers questions using the provided study materials.
        
        If the answer is not in the study materials, respond with: "I cannot find relevant information in the study materials provided."
        
        study materials: 
        {context}
        
        Question: {query}
        
        Answer:
        """
        response = llm.predict(prompt) # fall's back to LLM's general knowledge leading to hallucination


        return {"question": query, "answer": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))