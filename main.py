
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
# import requests
# from bs4 import BeautifulSoup
import tenkii as tnk
app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("Hello World")
    print(event.message.text)
    if event.message.text == "京都女子大学の天気":
        # line_bot_api.reply_message(
        # event.reply_token,
        # TextSendMessage(text="天気だね"))
        weather = tnk.Weather(6110)
        print(weather)
        line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text="天気だね"),TextSendMessage(text=weather)])
        

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="hello"))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)