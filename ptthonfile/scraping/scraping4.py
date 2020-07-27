import re
from html import unescape

with open('dp.html') as f:
#with open(r'C:\Users\遠藤主基\Desktop\share\pythonfile\dp.html') as f:
#with open(r'C:\Users\遠藤主基\Desktop\share\pythonfile\dp.html','r',encoding="utf-8_sig") as f:
    html = f.read()
#windows環境だと文字コードが「cp932」となり使えないため、「"utf-8_sig"」に変換する

#dp.htmlを展開し、変数htmlに保存



#f = open(r'C:\Users\遠藤主基\Desktop\share\pythonfile\dp.html','r',encoding="utf-8")
#html = f.read()

for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>',html,re.DOTALL):
#変数htmlから「<a itemprop="url"～</ul>　</a></li>」を抽出（「.」は改行と認識）し、結果を変数partial_htmlに保存
    url = re.search(r'<a itemprop="url" href="(.*?)">',partial_html).group(1)
    #変数partial_htmlから「<a itemprop="url" href="(グループ１)">」を抽出し、「グループ１」を抽出し、変数urlに保存
    url = 'https://hiyho.jp' + url

    title = re.search(r'<p itemprop="name".*?</p>',partial_html).group(0)
    #変数partial_htmlから「<p itemprop="name"～</p>」を抽出し、変数titleに保存
    title = title.replace('<br/>',' ')
    #<br/>を空白にする
    title = re.sub(r'<.*?>','',title)
    #<>を削除
    title = unescape(title)

    print(url,title)

print('helloworld')
