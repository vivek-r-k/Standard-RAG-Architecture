import embedd_chunks
from dotenv import load_dotenv
import extract_data, chunk_data
load_dotenv()

# import google.generativeai as genai

# for model in genai.list_models():
#     print(model.name)

def main():
    print("=== RAG Document Ingestion Pipeline ===\n")
    documents = extract_data.load_documents("../docs")
    chunks = chunk_data.split_documents(documents,1500,0)
    vector_store = embedd_chunks.create_vector_store(chunks)

if __name__ == "__main__":
    main()