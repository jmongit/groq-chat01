import os
import gradio as gr
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

SYSTEM_PROMPT = "あなたは親切な日本語AIアシスタントです。"

def chat(message, history):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    if history:
        for item in history:
            # 新形式: {"role": "...", "content": "..."}
            if isinstance(item, dict):
                role = item.get("role")
                content = item.get("content")
                if role in ["user", "assistant"] and content:
                    messages.append({"role": role, "content": content})

            # 旧形式: [user_msg, assistant_msg]
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                user_msg, assistant_msg = item[0], item[1]
                if user_msg:
                    messages.append({"role": "user", "content": user_msg})
                if assistant_msg:
                    messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1000,
    )

    return response.choices[0].message.content


demo = gr.ChatInterface(
    fn=chat,
    title="chat test",
    description="会話履歴ありのテスト"
)

port = int(os.environ.get("PORT", 10000))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)
