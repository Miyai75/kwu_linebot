
from cgitb import text
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, PostbackEvent
)
import os
import json
# from basu import main as bs
import pandas as pd
from tenki import tenkii as tnk
from basu import main as bus


app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

bus_select_data = [0,0,0] # バスの結果を数値でデータ格納[登下校,バスの種類,何限]
bus_select_data_text = ["","",""] # バスの結果をそのまま格納[登下校,バスの種類,何限]
periods_dict = {"first_period":1, "second_period":2, "third_period":3, "fourth_period":4, "fifth_period":5}


# f = open('bus_option.json', 'r')
# flex_message_json_dict = json.load(f)
# print(flex_message_json_dict)


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
# テキストメッセージを受け取った時に動く関数
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)

    result_contents = TextSendMessage(text="hello")

    if event.message.text == "京都女子大学の天気":
        weather = tnk.Weather(6110)
        print(weather)
        result_contents = TextSendMessage(text=weather)
        # sendMessage(event, "text", weather)

    if event.message.text == "バスの時刻":
        result_contents = FlexSendMessage(
            alt_text='利用バス選択',
            # contentsパラメタに, dict型の値を渡す
            contents=openJsonFile('json/bus_option.json')
            )

    if event.message.text == "テスト":
        result_contents = FlexSendMessage(
            alt_text='利用バス選択',
            # contentsパラメタに, dict型の値を渡す
            contents=openJsonFile('json/test.json')
        )

    line_bot_api.reply_message(event.reply_token,result_contents)
    print("完了")

# ボタン押したときに動く関数
@handler.add(PostbackEvent)
def on_postback(event):

    result_contents = TextSendMessage(text="hello")

    if event.postback.data == "princess_line_bus":
        print(event.postback.data)
        result_contents = [
            TextSendMessage(alt_text='princess_line_bus',text = "プリンセスラインバスですね！"),
            FlexSendMessage(alt_text='バス利用目的', contents = openJsonFile('json/bus_purpose.json'))
        ]
        bus_select_data[1] = 2
        bus_select_data_text[1] = "プリンセスラインバス"

    if event.postback.data == "municipal_bus":
        print(event.postback.data)
        result_contents = [
            TextSendMessage(alt_text='municipal_bus',text = "市バスですね！"),
            FlexSendMessage(alt_text='バス利用目的', contents = openJsonFile('json/bus_purpose.json'))
        ]
        bus_select_data[1] = 1
        bus_select_data_text[1] = "市バス"
    
    if event.postback.data in periods_dict:
        bus_result = whatPeriod(event.postback.data)
        result_contents = [TextSendMessage(text = bus_result[0]),TextSendMessage(text = bus_result[1])]

    
    print(bus_select_data)
    print(bus_select_data_text)
    line_bot_api.reply_message(event.reply_token,result_contents)
    
# FlexMessageの用意
# ファイルを読み込んだ変数を返す関数
def openJsonFile(filename):
    with open(filename) as f:
        print("ロード中")
        flex_message_json_dict = json.load(f)
        print(flex_message_json_dict)
        return flex_message_json_dict

# ○○時限に登校するのを格納したバス用の関数、テキストと時間を返す
# periodには何時限かが入るよ
def whatPeriod(period):
    # 登校、何限かをbus_select_dataに代入
    bus_select_data[0], bus_select_data[2] = 1, periods_dict[period]
    # 選んだ結果確認用テキストをbus_select_data_textに代入
    bus_select_data_text[0], bus_select_data_text[2] = "登校", periods_dict[period]
    print(bus_select_data)
    print(bus_select_data_text)
    # result_textに選択の最終確認のテキスト代入
    result_text = f"「{bus_select_data_text[1]}で{bus_select_data_text[2]}限に{bus_select_data_text[0]}」ですね！"
    print(result_text)

    # bus_tmpにBusTimeのインスタンス化、resultに関数の結果代入
    bus_tmp = bus.BusTime(bus_select_data[0],bus_select_data[1],bus_select_data[2])
    bus_result = bus_tmp.bus()
    return result_text, bus_result



    

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)