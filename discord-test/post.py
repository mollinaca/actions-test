#!/usr/bin/env python3
import datetime
import os
import sys
import requests
#from dotenv import load_dotenv
#load_dotenv()  # take environment variables

def main():
    # Webhook URL（先ほどコピーしたURLをここに貼り付け）
    WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL_TEST")

    # message
    if len(sys.argv) > 1:
        # 引数がある場合、それを結合（複数行を含む1つの文字列として扱う）
        message = " ".join(sys.argv[1:])
    else:
        # 引数がない場合はデフォルト値
        message = DEFAULT_MESSAGE

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
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    DEFAULT_MESSAGE = f"test from post.py : {now_str}"
    main()
