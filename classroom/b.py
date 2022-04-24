import codecs #指定した文字コードでファイルを開く
import csv
import imp
from itertools import count #csvモジュール
import re #正規表現

class SerchClass:
    datalist = []       

    # csvファイル読み込み、二重配列に格納
    with open('classroom/output.csv', 'r', encoding='utf-8') as f:
        dataReader = csv.reader(f) #csvreaderはデフォルトで、列はカンマ、行は\n で分割される。
        for row in dataReader:
            print(row)
            #二重配列にする
            datalist = [row for row in dataReader]


    def kyousitu(self, keyword, data = datalist):
        #############################################
        # keyword : 検索ワード
        # data : 参照するデータ
        # dataからkeywordを検索して検索結果を返すメソッド
        #############################################        

        self.list =[] # 検索結果を格納するリスト
        # keyword = input('教科名を入力してください : ')

        for i in data: # まず外側のfor文で行数分の要素数だけ回します。これのカウント変数をiとしています。
            for m in i:
                match = re.search(keyword,m) #正規表現でキーワード検索をしています
                if match:
                    # 文字列型をリスト型に変更
                    tmp = [m]
                    #print(tmp)
                    self.list.append(tmp)

        #print(SerchClass.list)

        if data != self.datalist:
            # keywordが前期か後期の時、showResultメソッドを回す
            return self.showResult()
        else:
            # ↑以外の時検索結果を二重配列のまま返す
            return self.list
            



    def showResult(self):
        #############################################
        # kyousituメソッドで得た検索結果（self.list）を加工して文字列にして返す
        #############################################     

        result_text = ""

        if not self.list:
            # self.listに何もない時
            self.list.append("項目が見つかりませんでした")
            result_text += "項目が見つかりませんでした"
        else:
            for data in self.list:
                #print(data[0])
                result_text += f"{data[0]}\n"
                
            result_text += f"\nの{len(self.list)}件見つかりました。"
        #print(result_text)
        return result_text


# a = SerchClass()
# result = a.kyousitu("前期")
# #print("\n\nここからだよ！\n",result)
# b = a.kyousitu("丸野", result)
# print(b)
