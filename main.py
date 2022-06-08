
from cgitb import text
from flask import Flask, request, abort
from waitress import serve

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, PostbackEvent, QuickReplyButton, MessageAction, QuickReply
)
import os
import json
from tenki import tenkii as tnk
from basu import main as bus
from support_center import yomikomi2 as sc
from classroom.b import SerchClass

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

bus_select_data = [0,0,0] # バスの結果を数値でデータ格納[登下校,バスの種類,何限]
bus_select_data_text = ["","",""] # バスの結果をそのまま格納[登下校,バスの種類,何限]
periods_dict = {"go_home":0, "first_period":1, "second_period":2, "third_period":3, "fourth_period":4, "fifth_period":5}
support_list = ["履修", "進路", "インターンシップ", "奨学金", "学費", "各種証明書"]
semester = ["前期","後期"]
search_bool = False
sclass = SerchClass()
sem_result = sclass.kyousitu("前期")
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

    result_contents = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,result_contents)
    print("完了")
    """
        global search_bool
        global sem_result
        print(event)

        

        # 教室検索モード
        if search_bool:
            print("bool値Trueです！！")
            if event.message.text in semester:
                print(sem_result)
                sem_result = sclass.kyousitu(event.message.text)
                result_contents = [
                    TextSendMessage(text = f"{event.message.text}ですね！"),
                    TextSendMessage(text = "続いて調べたい教科のキーワードを入力してください")
                ]
                print(sem_result)    
            else:
                classroom = sclass.kyousitu(event.message.text, sem_result)
                print(classroom)
                result_contents = TextSendMessage(text = classroom)
                search_bool = False

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

        if event.message.text == "教室":
            items = [QuickReplyButton(action=MessageAction(label=f"{sem}", text=f"{sem}")) for sem in semester]
            result_contents = [
                FlexSendMessage(alt_text='教室検索モード', contents = openJsonFile('json/modeexp.json')),
                TextSendMessage(text = "学期を選択してください", quick_reply=QuickReply(items=items))
            ]
            print("教科名を入力してください")
            search_bool = True
            print(search_bool)   

        if event.message.text == "大学生活に関する窓口":
            items = [QuickReplyButton(action=MessageAction(label=f"{support}", text=f"{support}")) for support in support_list]
            result_contents = [
                    TextSendMessage(text="進路 履修 インターンシップ 奨学金 各種証明書に関する対応窓口に関する情報を教えます！"),
                    TextSendMessage(text="知りたいことは何ですか?", quick_reply=QuickReply(items=items))
                ]


        # ユーザーが送ったメッセージがsupport_listに含まれていたら反応する
        if event.message.text in support_list:
            result_contents = [
                TextSendMessage(text = f"{event.message.text}の情報はこちらになります！"),
                TextSendMessage(text = sc.center(event.message.text))
            ]

        if event.message.text == "テスト":
            items = [QuickReplyButton(action=MessageAction(label=f"{support}", text=f"{support}")) for support in support_list]
            result_contents = TextSendMessage(text="どの言語が好きですか？",quick_reply=QuickReply(items=items))
        """


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
    
    # periods_dict = {"first_period":1, "second_period":2, "third_period":3, "fourth_period":4, "fifth_period":5}
    # 上のdictのキーと押されたボタンのデータが一緒の時の結果をresult_contentsに代入
    if event.postback.data in periods_dict:
        bus_result = whatPeriod(event.postback.data)
        print(bus_result)
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

# 登下校のボタンからデータ受け取ってバスの関数を回して結果のテキストと時間を返す
# periodにはperiods_dictのキーが入る
def whatPeriod(period):
    if period != "go_home":
        # 登校、何限かをbus_select_dataに代入
        bus_select_data[0], bus_select_data[2] = 1, periods_dict[period]
        # 選んだ結果確認用テキストをbus_select_data_textに代入
        bus_select_data_text[0], bus_select_data_text[2] = "登校", periods_dict[period]
        # result_textに選択の最終確認のテキスト代入
        result_text = f"「{bus_select_data_text[1]}で{bus_select_data_text[2]}限に{bus_select_data_text[0]}」ですね！"
        

    
    else:
        bus_select_data[0], bus_select_data[2] = 2, periods_dict[period]
        bus_select_data_text[0] = "下校"
        result_text = f"「{bus_select_data_text[1]}で{bus_select_data_text[0]}」ですね！"


    print(bus_select_data)
    print(bus_select_data_text)
    print(result_text)
    # bus_tmpにBusTimeのインスタンス化、resultに関数の結果代入
    bus_tmp = bus.BusTime(bus_select_data[0],bus_select_data[1],bus_select_data[2])
    bus_result = bus_tmp.bus()
    return result_text, bus_result



    

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    # app.run(host="0.0.0.0", port=port)
    serve(app, host="0.0.0.0",port = port)