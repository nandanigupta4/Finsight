from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import*


def create_vector_db():
    
    dir_loader =DirectoryLoader(
        DATA_DIR_PATH,
        glob= '*.pdf',
        loader_cls= PyPDFLoader)
    
    docs= dir_loader.load()
    print("PDF Loader")
    
    splitter= RecursiveCharacterTextSplitter(
        chunk_size= CHUNK_SIZE,
        chunk_overlap= CHUNK_OVERLAP
    )
    inp_text = splitter.split_documents(docs)
    print("Data Chunks created")
    
    
    hfembeddings = HuggingFaceEmbeddings(
        model_name= EMBEDDER,
        model_kwargs = {'device': 'cpu'}

    )
    
    vector_db = FAISS.from_documents(inp_text,hfembeddings)
    vector_db.save_local(VECTOR_DB_PATH)
    print("Vector Store Creation Complete")
    
if __name__ == "__main__":
    create_vector_db()