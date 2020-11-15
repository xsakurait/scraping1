import urllib.request as req
from bs4 import BeautifulSoup
import time

url="https://news.yahoo.co.jp/"
res=req.urlopen(url)

soup=BeautifulSoup(res,"html.parser")
link=soup.select("a[href]")
result=[]
for a in link:
    href=a.attrs["href"]
    title=a.string
    result.append((title,href))


for title,url in result:
    print("link="+url)
    #クローリングの負荷をWebサイト先のサーバーに負荷をかけない
    # ために、2秒間隔でアクセスを行う
    time.sleep(2)
    res_1=req.urlopen(url)
    soup_1=BeautifulSoup(res_1,"html,parser")
    #  リンクの<p>タグのテキスト抽出
    p_list=soup_1.find_all("p")
    for p in p_list:
        #  抽出したもの,記事タイトルごとにtxtファイルに書き込みを行う
        print(p.get_text())
        #withを用いたため,ファイルを閉じる処理は書かなくていい
        with open("{}.txt".format(title),mode="a") as f:
            f.write(p.get_text())