import codecs #指定した文字コードでファイルを開く
import csv
import imp
from itertools import count #csvモジュール
import re #正規表現

def kyousitu(keyword):

    list =[]
    result_text = ""
    f = codecs.open('classroom/output.csv', 'r','utf-8')

    dataReader = csv.reader(f) #csvreaderはデフォルトで、列はカンマ、行は\n で分割される。
    # keyword = input('教科名を入力してください : ')
    for i in dataReader: #まず外側のfor文で行数分の要素数だけ回します。これのカウント変数をiとしています。
        # print(i)
        for m in i:
            match = re.search(keyword,m) #正規表現でキーワード検索をしています
            # print(match)
            if match:
              #print(m)
              list.append(m)
    if not list:
        list.append("項目が見つかりませんでした")
    f.close()
    print(list)

    for data in list:
        result_text += f"{data}\n"
    
    result_text += f"\nの{len(list)}件見つかりました。"
    return result_text
# kyousitu()