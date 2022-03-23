# sity_bus1.py
import pandas as pd
import datetime as dt

def sity_bus1(y):
    # データフレームを読み込む
    df = pd.read_csv("京都駅発.csv", encoding='shift_jis')

    # 欠損値を削除する
    df = df.dropna()

    # リスト化する
    sity_bus = df[["限","系統","出発","到着"]].values

    # 文字を入力する
    y = int(input("大学には何限目に着きたいですか？"))
    print(y, "限に着くには...")
    print()

    for sb1 in sity_bus:
        if sb1[0] == y:
            print(sb1[1], "系統")
            print(sb1[2], "京都駅発～")
            print(sb1[3], "東山七条着")
            print()
            
    print("がオススメです。")
