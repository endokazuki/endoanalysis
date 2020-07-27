import lxml.html



tree = lxml.html.parse('result.html')

html = tree.getroot()



for a in html.cssselect('a'):

    print(a.get('href'),a.text)