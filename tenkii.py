import requests
from bs4 import BeautifulSoup

  #YAHOO天気のHTML情報をすべて取得
def Weather(AreaCode):
    url = "https://weather.yahoo.co.jp/weather/jp/26/" + str(AreaCode) + ".html"
    r = requests.get(url)
     #HTMLからBeautifulsoupオブジェクトを作る
    soup = BeautifulSoup(r.text, 'html.parser')
    rs = soup.find(class_='forecastCity')
    #strip()で文字列前後の空白を削除
    rs = [i.strip() for i in rs.text.splitlines()]
    rs = [i for i in rs if i != ""]

    print(rs[0] + "の天気は" + rs[1] + "、明日の天気は" + rs[19] + "です。")
    result = rs[0] + "の天気は" + rs[1] + "、明日の天気は" + rs[19] + "です。"
    return result
print(Weather(6110))
