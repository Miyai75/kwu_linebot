
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
import os
import json
import bus
from tenki import tenkii as tnk

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

class SendMessage:
    def __init__(self): # インスタンス化されて渡ってくる値を受ける変数を定義します
        # インスタンス変数（属性の初期化）
        self.self.bus_scene = 0 # 実行順③
        print("コンストラクタが呼ばれました") # # 実行順④]

    def handle_message(event,self):
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

        # if event.message.text == "大学生活に関する窓口":
        #     line_bot_api.reply_message(
        #     event.reply_token,
        #     [TextSendMessage(text="進路 履修 インターンシップ 奨学金 各種証明書に関する対応窓口に関する情報を教えます！"),TextSendMessage(text="何について知りたいですか？")])
        #     word = input()
        #     df = pd.read_csv("center2.csv")#csvファイルを読み込み
        #     #print(list(df.loc[1]))

        #     a = list#初期値

        #     for index, data in df.iterrows():  # データフレームで行ごとにデータを取得
        #         #print(index)
        #         #print(data)
        #         #print('--------')
        #         if event.message.text == "進路":
        #             a = list(df.loc[0])  # csvの1行目は項目なので2行目から数えるので2行目が[0]
        #             break  # breakしないと6個同じものが出力される
        #         elif event.message.text == "履修":
        #             a = list(df.loc[1])
        #             break
        #         elif event.message.text == "インターンシップ":
        #             a = list(df.loc[2])
        #             break
        #         elif event.message.text == "学費":
        #             a = list(df.loc[3])
        #             break
        #         elif event.message.text == "奨学金":
        #             a = list(df.loc[4])
        #             break
        #         elif event.message.text == "各種証明書":
        #             a = list(df.loc[5])
        #             break
        #         else:
        #             a = "いつでもどうぞ"
        #             break
            
        #     line_bot_api.reply_message(
        #     event.reply_token,
        #     [TextSendMessage(text=a)])

        if event.message.text == "バスの時刻":
            print("フラグ")
            print(self.bus_scene) 
            line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text="登校しますか？下校しますか？"),TextSendMessage(text="1.市バス 2.プリンセスバス")])
            self.bus_scene = 1

        if self.bus_scene == 1:
            bus_choices = {1:"市バス", 2:"プリンセスバス"} 
            if event.message.text in bus_choices:
                answer1 = bus_choices[event.message.text]
                print(answer1)
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=answer1))
            
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="hello"))

message = SendMessage()
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)