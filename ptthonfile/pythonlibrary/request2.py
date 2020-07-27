import requests
 
# 取得するURL
url_top = "https://yahoo.co.jp"
 
#「https://yahoo.co.jp」トップページ取得
response = requests.get(url_top)
response.encoding = response.apparent_encoding
 
response_html = response.text
 
# 例えばresult.htmlに保存するなら…
with open('result.html', 'w', encoding='utf-8') as f:
    f.write(response_html)
 
print('ファイルに保存')