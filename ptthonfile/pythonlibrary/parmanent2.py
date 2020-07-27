
import requests
import lxml.html

def main():
    response = requests.get('https://gihyo.jp/dp')
#クローリング
    urls = scrape_list_page(response)
    for url in urls:
        print(url)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
#スクレイピング
    root.make_links_absolute(response.url)
#responseのurl「https://gihyo.jp/dp」を絶対URLの頭の部分（第1引数）とする
    for a in root.cssselect('#listBook  a[itemprop="url"]'):
#変数rootからid属性の属性値が「listbook」であり、a要素のitemprop属性の属性値が「url」であるものを選択する
        url = a.get('href')
        yield url
#変数aからhref属性の属性値を抜き出す
if __name__ == '__main__':
    main()
