#2-1.py is basic of 2-2.py
#beautifulsoup4(requestsの取ってきた情報を改変して見やすくする,パーサーとも呼ばれる）は使わない
import requests as req
#URL取得
req_1=req.get("取得したいurl")
#ヘッダー情報取得
print(req_1.headers)
print("\n-------------------\n")
#文字コード情報(エンコード情報)取得
print(req_1.encoding)
print("\n-------------------\n")
#スクレイピング先のWebページのhtmlを取得
print(req_1.content)
