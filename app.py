from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from datetime import datetime
import os

app = Flask(__name__)
conversation_history = []

client = OpenAI()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input")
    response = get_chat_response(user_input)
    return jsonify({"response": response})

@app.route("/generate_journal", methods=["POST"])
def journal():
    journal = generate_journal()
    return jsonify({"journal": journal})

def get_chat_response(user_input):
    prompt = "あなたはユーザーのお友達です。ユーザーが一日の終わりに対話をしに来るのでユーザーの一日の出来事についてタメ口で質問してください。"
    messages = [{"role": "system", "content": prompt}] + conversation_history + [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150
    )
    reply = response.choices[0].message.content.strip()
    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

def generate_journal():
    prompt = "あなたは日記を書くアシスタントです。以下の会話を基に、今日の出来事を簡潔にまとめた日記を書いてください。日付は必要ありません。\n" + \
             "\n".join([f"ユーザー: {entry['content']}" if entry['role'] == "user" else f"アシスタント: {entry['content']}" for entry in conversation_history])
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    app.run(debug=True)





#cd Users\ojiri\Desktop\task_dialog_system
#python3 dialog_system.py

#What 
#Why なぜ。これをすることで世界がどう変わるのか。
#How
#もし具体的に何か研究テーマが決まっていたら、ｗｈａｔ　ｗｈｙ　ｈｏｗを具体的に書く。
#work で今期何をやったか。
#作った対話システムを説明。
#RG Portalで過去のスライドがみられる。