from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("movies_details.csv")
df.columns = df.columns.str.strip()
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=(
                f"Movie Title: {row['Title']}\n"
                f"Year: {row['Year']}\n"
                f"OTT Platform: {row['OTT_Platform']}\n"
                f"Genre: {row['Genre']}\n"
                f"Director: {row['Director']}\n"
                f"Country: {row['Country']}\n"
                f"Status: {row['Status']}"
            ),
            metadata={
                "movie_id": row["Movie_ID"],
                "title": row["Title"],
                "rating": row["ratings"],
                "year": row["Year"],
                "genre": row["Genre"]
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="movie_details",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)