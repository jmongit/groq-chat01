from groq import Groq
import gradio as gr
import os

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def chat(message, history):
    messages = [
        {
            "role": "system",
            "content": "あなたは親切な日本語アシスタントです。"
        }
    ]

    # 過去の会話をmessagesに追加
    for user_message, assistant_message in history:
        messages.append({
            "role": "user",
            "content": user_message
        })
        messages.append({
            "role": "assistant",
            "content": assistant_message
        })

    # 今回のユーザー発言を追加
    messages.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(chat)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
