import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(user_question, context):
    messages = [
        {"role": "system", "content": "Eres un asistente experto en una tienda virtual. Usa el contexto para responder."},
        {"role": "user", "content": f"{context}\n\nPregunta: {user_question}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message["content"]
