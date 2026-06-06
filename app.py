from groq import Groq
import gradio as gr
import os

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def chat(message, history):
    messages = []

    messages.append({
        "role": "system",
        "content": "あなたは親切な日本語アシスタントです。"
    })

    messages.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(chat)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
