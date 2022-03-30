# sity_bus2.py
import pandas as pd
import datetime as dt
import time

def sity_bus2():
    # データフレームを読み込む
    df = pd.read_csv("basu/東山七条発.csv")

    # 欠損値を削除する
    df = df.dropna()

    # リスト化する
    sity_bus = df[["系統","出発","到着"]].values

    # print (sity_bus)
    # 現在時刻の取得
    dt_now = dt.datetime.now()
    hour = dt_now.hour
    minute = dt_now.minute
    y = dt_now.strftime("%H:%M") # 日付を文字列化
    # print(y)
    print("市バスで下校するには...")
    print()
    textsb2 = ""
    # foreach文を作成
    for sb2 in sity_bus:
        st1 = sb2[1] # 出発時刻
        st2 = y # 現在時刻
        x = dt.datetime.now()+dt.timedelta(minutes=20) # 現在時刻から20分後の時刻
        st3 = x.strftime("%H:%M") # 日付を文字列化
        # print(st1)
        # print(st2)
        # print(st3)
        
        if st1 > st2 and st1 < st3: # 現在時刻 < バスの出発時刻 < 現在時刻の20分後
            print(sb2[0], "系統")
            print(sb2[1], "東山七条発～")
            print(sb2[2], "京都駅着")
            print()
            textsb2 += f"{sb2[0]}系統\n{sb2[1]}東山七条発～\n{sb2[2]}京都駅着\n\n"

            
    print("がオススメです。")
    textsb2 += "がオススメです。"
    return textsb2

# print(sity_bus2())