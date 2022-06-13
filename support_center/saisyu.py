# yomikomi2.py

from sre_constants import AT_MULTILINE
#from tkinter import W



def center():
    import pandas as pd


    print("進路 履修 インターンシップ 奨学金 各種証明書などの対応窓口に関する情報を教えます！")
    word = input("知りたいことは何ですか?")
    print("知りたいことは",word, "ですね")

    a = list#初期値
    import requests
    import json


    #基本情報の設定 JAをENにすれば英語のテキストを解析可能

    header = {'Content-Type': 'application/json'}

    body = {
        "document": {
        "type": "PLAIN_TEXT",
        "language": "JA",
        "content": word
    },
    "encodingType": "UTF8"
    }

  #json形式で結果を受け取る。
    response = requests.post('https://language.googleapis.com/v1beta2/documents:analyzeSyntax?key=AIzaSyDJalrMgWUSUA214E7Ue90dYYgm3a9JT5s', headers=header, json=body)

    print('status', response)#35行目でAPIに送り品詞に分ける

    print('text', response.text)

    response_ = json.loads(response.text)#jsonファイルのままだとpythonで動かないので辞書型に変えて、response_に格納してる.loads(response.text)



    for d in response_['tokens']:
        word = d['text']['content']
        #print(d)
        #print(word)
    #for word in word_mini:
        if word in "進路":
            a = '進路,進路・就職課,sinro@kyoto-wu.ac.jp,075-531-7060,L校舎4階,平日:8時45分~17時・休日:8時45分~12時'
            break  # breakしないと6個同じものが出力される
        elif word in ["履修",'災害時の授業に関して','病気・事故による試験未受験','転部・転科']:
            a = '教務課,kyomu@kyoto-wu.ac.jp,075-531-7048,L校舎1階,平日(開講期間):8時45分~17時・平日(休講期間):8時45分~11時10分・12時10分~17時'
            break
        elif word in "インターンシップ":
            a = 'キャリア開発センター,career@kyoto-wu.ac.jp,075-531-9177,L校舎3階,8時45分~17時（土曜日は窓口対応無し）'
            break
        elif word in ["学費","振込","実習費"]:
            a = '財務課,zaimu@kyoto-wu.ac.jp,075-531-7042,京都府京都市東山区今熊野北日吉町３５,9時~11時・12時10分~15時'
            break
        elif word in ["奨学金","学費の延滞","長期欠席","休学","退学","復学",]:
            a = '学生支援課,gakusei@kyoto-wu.ac.jp,075-531-7057,L校舎2階,平日:8時45分~17時・休日:8時45分~12時'
            break
        elif word in ["各種証明書","学割証","学生証"]:
            a = '証明書発行センター(学部事務課内),gakuji@kyoto-wu.ac.jp,075-531-7045,L校舎1階,9時~11時10分・12時10分~16時30分（土曜日は窓口対応無し）'
            break
        elif word in ["ATM"]:
            word = input("京都銀行・ゆうちょ銀行・三井住友銀行の内どれですか？")
            #if word in ["京都銀行","ゆうちょ銀行","三井住友銀行"]:
                #for n in word:
            if word in "京都銀行":
                a = '京都銀行・京都信用金庫,平日:9時~18時,土曜日:9時~18時,Q校舎'
            elif word in "ゆうちょ銀行":
                a = 'ゆうちょ銀行,平日:9時~19時,土曜日:9時~17時,Q校舎'
            elif word in "三井住友銀行":
                a = '三井住友銀行,平日:8時~20時,土曜日:8時~20時,C校舎'
            else:
                a = '京女にはありません。乙です！'
                break
            break
        else:
             a = 'いつでもどうぞ'
    return a#戻り値
print(center())
