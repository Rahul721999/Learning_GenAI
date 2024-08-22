from transformers import pipeline

nlp = pipeline("text-generation", model="gpt2")

def generate_answer(question):
    response = nlp(question, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]

question = "What is AI?"
print(generate_answer(question))


from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
nlp = pipeline("text-generation", model="gpt2")

@app.post("/ask")
def ask_question(question: str):
    response = nlp(question, max_length=50, num_return_sequences=1)
    return {"answer": response[0]["generated_text"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
