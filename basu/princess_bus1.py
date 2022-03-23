# princess_bus1.py
import pandas as pd
import datetime as dt

def princess_bus1(y):
    # データフレームを読み込む
    df = pd.read_csv("京都駅八条口.csv")

    # 欠損値を削除する
    df = df.dropna()

    # リスト化する
    princess_bus = df[["限","出発","到着"]].values

    y = int(input("大学には何限目に着きたいですか？"))
    print(y, "限に着くには...")
    print()

    for pb1 in princess_bus:
        if pb1[0] == y:
            print(pb1[1], "京都駅八条口発～")
            print(pb1[2], "京都女子大学着")
            print()
            
    print("がオススメです。")