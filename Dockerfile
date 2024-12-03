FROM python:3.11
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the model during build
RUN python -c "from langchain_huggingface import HuggingFaceEmbeddings; HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')"

COPY . .

EXPOSE 9696
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]