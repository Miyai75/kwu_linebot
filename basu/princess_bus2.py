# princess_bus2.py
import pandas as pd
import datetime as dt
import time

def princess_bus2():
    # データフレームを読み込む
    df = pd.read_csv("京都女子大学.csv")

    # 欠損値を削除する
    df = df.dropna()

    # リスト化する
    princess_bus = df[["出発","到着"]].values
    # print(princess_bus)

    # 結果格納用リスト
    listpb2 = []

    # 現在時刻の取得
    dt_now = dt.datetime.now()
    hour = dt_now.hour
    minute = dt_now.minute
    y = dt_now.strftime("%H:%M") # 日付を文字列化
    print("プリンセスバスで下校するには...")
    print()

    for pb2 in princess_bus:
        st1 = pb2[0] # 出発時刻
        st2 = y # 現在時刻
        x = dt.datetime.now()+dt.timedelta(minutes=20) # 現在時刻から20分後の時刻
        st3 = x.strftime("%H:%M") # 日付を文字列化
        #print(st1)

        if st1 > st2 and st1 < st3: # 現在時刻 < バスの出発時刻 < 現在時刻の20分後
            print(pb2[0], "京都女子大学発～")
            print(pb2[1], "京都駅八条口着")
            print()
            listpb2.append(pb2)
    print("がオススメです。")

    return listpb2