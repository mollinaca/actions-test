#!/usr/bin/env python3
import os
import requests
#from dotenv import load_dotenv
#load_dotenv()  # take environment variables

def main():
    # Webhook URL（先ほどコピーしたURLをここに貼り付け）
    WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL_TEST")

    # 送信したいメッセージ
    message = "こんにちは！これはWebhookを使って送信されたメッセージです。"

    # メッセージのペイロードを設定
    payload = {
        "content": message
    }

    # POSTリクエストを送信してメッセージを送信
    response = requests.post(WEBHOOK_URL, json=payload)

    # レスポンスの確認
    if response.status_code == 204:
        print("メッセージが正常に送信されました！")
    else:
        print(f"メッセージ送信に失敗しました。ステータスコード: {response.status_code}")

if __name__ == '__main__':
    main()
