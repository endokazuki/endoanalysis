import lxml.html
from pymongo import MongoClient

tree = lxml.html.parse('index.html')
html = tree.getroot()
#index.htmlを解析し、結果をhtmlにHtmlElementオブジェクトを保存

client =  MongoClient('localhost',27017)
db = client.scraping
collection = db.links
#MongodbにDB:scrapingを作成し、その中にコレクション（テーブル）linksを作成

collection.delete_many({})
#コレクション内にデータ（bson）がある場合、全て削除

for a in html.cssselect('a'):
    collection.insert_one({
        'url':a.get('href'),
        'title':a.text,
        })
#index.html内のaタグからhref要素とテキストのデータをコレクション内に追加する

for link in collection.find().sort('_id'):
    print(link['_id'],link['url'],link['title'])
#コレクション内のデータを「_id」の順番で出力する

for link in collection.find():
    print(link['_id'],link['url'],link['title'])
#コレクション内のデータを適当に出力する

