
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
import os
import json
# from basu import main as bs
import pandas as pd
from tenki import tenkii as tnk

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

flex_message = FlexSendMessage(
    alt_text='hello',
    contents={
        'type': 'bubble',
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Header text"
                }
            ]
        },
        'direction': 'ltr',
        'hero': {
            'type': 'image',
            'url': 'https://example.com/flex/images/image.jpg',
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Body text"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Footer text"
                }
            ]
        },
        "styles": {
            "comment": "See the example of a bubble style object"
        }

    }
)

messages = []

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# @関数名デコレータ（元ある関数を変更せずに要素を追加出来るやつ）になる
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    f = open('bus.json', 'r')
    flex_message_json_dict = json.load(f)
    print(type(flex_message_json_dict))
    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(
            alt_text='alt_text',
            # contentsパラメタに, dict型の値を渡す
            contents=flex_message_json_dict
        )
    )
    print("完了")


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)