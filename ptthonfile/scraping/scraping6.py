from xml.etree import ElementTree

tree = ElementTree.parse('rss2.xml')
#parse関数にxmlファイルを読み込み、ElementTreeオブジェクト（XMLの木構造）を得る[パースを行う]
root = tree.getroot()
#解析結果の取得

for item in root.findall('channel/item'):
#channelの子要素であるitem要素を取得
    title = item.find('title').text
    #title要素を取得
    url = item.find('link').text
    #link要素を取得
    print(url,title)

