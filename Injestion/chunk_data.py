from langchain_text_splitters import CharacterTextSplitter

def split_documents(documents, chunk_size=1000, chunk_overlap=0):
    print("Splitting documents into chunks...")
    
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
    )
    
    chunks = text_splitter.split_documents(documents)
    
    return chunks