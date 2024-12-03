from langchain_huggingface import HuggingFaceEmbeddings
from fastapi import FastAPI
import uvicorn
app = FastAPI()

embedding_models = ["sentence-transformers/all-MiniLM-L6-v2","sentence-transformers/paraphrase-MiniLM-L6-v2"]

@app.get("/embeddings")
def get_embeddings(model_name:str,query:str):
    if model_name not in embedding_models:
        return {"error": "Model not found"}
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings.embed_query(query)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)