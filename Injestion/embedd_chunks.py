from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import os

def create_vector_store(chunks, persist_directory="../db/chroma_db"):
    print("Creating embeddings and storing in ChromaDB...")
        
    # embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    # embedding_model = OpenAIEmbeddings(
    #     model="text-embedding-3-small",
    #     api_key=os.getenv("OPENAI_API_KEY"),
    #     openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/"
    # )
    
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    print("--- Creating vector store ---")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory, 
        collection_metadata={"hnsw:space": "cosine"}
    )
    print("--- Finished creating vector store ---")
    
    print(f"Vector store created and saved to {persist_directory}")
    return vectorstore