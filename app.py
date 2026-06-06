import os
import gradio as gr
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def chat(message, history):
    messages = [
        {"role": "system", "content": "あなたは日本語で自然に答える親切なAIです。"}
    ]

    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(fn=chat)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
