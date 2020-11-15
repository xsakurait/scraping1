import requests as req
from bs4 import BeautifulSoup as bs

html=req.get("yahoonewsのurl")
#スクレイピングしたWebページのhtml要素
req_1=bs(html.content,"html.parser")

#テキストとしてp要素(タイトル)を出力
for title in req_1.select("p"):
    print(title.getText())