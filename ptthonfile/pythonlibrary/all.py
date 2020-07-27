import re
import time
import requests
import lxml.html
from pymongo import MongoClient

def main():
#メイン関数   
    client=MongoClient('localhost',27017)
#MongoDBの接続
    collection=client.scraping.ebooks
#MongoDBのscrapingのデータベースからebooksというテーブル（コレクション）を作成
    collection.create_index('key',unique=True)
#テーブル内でkeyフィールド（key列）は一意制約を付与
    response = requests.get('https://gihyo.jp/dp')
#クローリング
    urls = scrape_list_page(response)
#「URL」を取得する関数を起動し、変数urlsに保存
    for url in urls:
        key=extract_key(url)
#「（書籍の）ISBN」を抜き出す関数を起動し、変数keyに保存
        ebook=collection.find_one({'key':key})
#テーブルebooksのkeyフィールドの中から変数keyと同じ値のものを探索する
        if not ebook:
            time.sleep(1)
            response=requests.get(url)
            ebook=scrape_detail_page(response)
            collection.insert_one(ebook)
#変数keyの値がkeyフィールド内に存在しない時、そのデータを新規のデータとしてDB内に保存する

        print(ebook)
#DB内（scrapingデータベース）にあるデータを出力する

def scrape_list_page(response):
#URLを抜き出す関数
    root = lxml.html.fromstring(response.content)
#スクレイピング
    root.make_links_absolute(response.url)
#responseのurl「https://gihyo.jp/dp」を絶対URLの頭の部分（第1引数）とする
    for a in root.cssselect('#listBook  a[itemprop="url"]'):
#変数rootからid属性の属性値が「listBook」であり、a要素のitemprop属性の属性値が「url」であるものを選択する
        url = a.get('href')
        yield url
#変数aからhref属性の属性値を抜き出す

def scrape_detail_page(response):
    root=lxml.html.fromstring(response.content)
    ebook={
        'url':response.url,
        'key':extract_key(response.url),
        'title':root.cssselect('#bookTitle')[0].text_content(),
        'price':root.cssselect('.buy')[0].text.strip(),
        'content':[normalize_spaces(h3.text_content()) for h3 in root.cssselect('#content > h3')],
#順番にURL、キー値（ISBN）、タイトル、値段、目次を抽出する
        }
    return ebook

def extract_key(url):
    m=re.search(r'/([^/]+)$',url)
#URLの末端部分である、ISBNを取り出す
    return m.group(1)

def normalize_spaces(s):
    return re.sub(r'\s+',' ',s).strip()
#目次の前後にある空白部分を削除する

if __name__ == '__main__':
    main()
#main関数の実行
