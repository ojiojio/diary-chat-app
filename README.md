# diary-chat-app
対話型日記生成システム

# 対話型日記生成システム

ChatGPT APIを使って、ユーザーと対話しながら日記を生成するWebアプリです。

## スクリーンショット
![screenshot](https://github.com/user-attachments/assets/02ab330a-c10d-4655-8775-9583bd8d11d0)

## 概要

- Flask + OpenAI APIで構成
- チャット形式で会話
- 会話履歴から日記を生成

## 使用技術

- Python（Flask）
- HTML / CSS / JavaScript
- OpenAI GPT-3.5 API

## ローカルでの使い方（OpenAI APIキーが必要）

```bash
git clone https://github.com/oijojio/diary-chat-app.git
cd diary-chat-app
pip install -r requirements.txt
```

1. `.env` ファイルを作成して、以下を記述してください：

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

2. アプリを起動：

```bash
python app.py
```

## 制作背景

このアプリは、**大学の研究の一環として、論文を読んで追実装したもの**です。
対話処理と日記生成のロジックは自身で実装しましたが、Webアプリ化やUIデザインなどの部分についてはAIの力を借りて構築しています。
