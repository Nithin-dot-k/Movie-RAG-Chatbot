from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama2")

template = """
You are a movie database assistant.

STRICT RULES:
- Answer ONLY from the context below
- Do NOT use your own knowledge
- If answer is not found, say: "Not found in database"
- Give short and direct answers

Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")

    if question == "q":
        break

    # 🔥 Step 1: Retrieve documents
    docs = retriever.invoke(question)

    # 🔥 Step 2: Convert to text (VERY IMPORTANT)
    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔥 Step 3: Send clean data to LLM
    result = chain.invoke({
        "context": context,
        "question": question
    })

    print("Answer:\n", result)
