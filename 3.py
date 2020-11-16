# Exception handling added to 2_2
#2_2に例外処理を追加したもの
import requests as req
from bs4 import BeautifulSoup as bs

try:
    #スクレイピングしたいURL入れる
    html=req.get("url")
    req_1=bs(html.content,"html.parser")
    #a要素取得
    tags=req_1.find_all("a")
    for tags in tag:
        print(tag.get_text())
except:
    print("取得することができません")
    