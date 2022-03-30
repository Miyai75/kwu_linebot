# yomikomi2.py
import pandas as pd
def center():

    df = pd.read_csv("support_center/center2.csv")#csvファイルを読み込み
    #print(list(df.loc[1]))

    # print("進路 履修 インターンシップ 奨学金 各種証明書に関する対応窓口に関する情報を教えます！")
    # word = input("知りたいことは何ですか?")
    # print("知りたいことは",word, "ですね")

    a = list#初期値

    for index, data in df.iterrows():  # データフレームで行ごとにデータを取得
        #print(index)
        #print(data)
        #print('--------')
        if word == "進路":
            a = list(df.loc[0])  # csvの1行目は項目なので2行目から数えるので2行目が[0]
            break  # breakしないと6個同じものが出力される
        elif word == "履修":
            a = list(df.loc[1])
            break
        elif word == "インターンシップ":
            a = list(df.loc[2])
            break
        elif word == "学費":
            a = list(df.loc[3])
            break
        elif word == "奨学金":
            a = list(df.loc[4])
            break
        elif word == "各種証明書":
            a = list(df.loc[5])
            break
        else:
            a = "いつでもどうぞ"
            break
    

    result_text = f"【センター名】\n{a[1]}\n【メールアドレス】\n{a[2]}\n【電話番号】\n{a[3]}\n【場所】\n{a[4]}"
    
    return result_text#戻り値
print(center())
