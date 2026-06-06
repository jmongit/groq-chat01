from groq import Groq
import gradio as gr
import os

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def chat(message, history):
    messages = []

    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(chat)

demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)
