import requests

r = requests.get('https://gihyo.jp/dp')

type(r)
r.status_code

r.headers['content-type']

r.encoding

r.text

print('HTTP status code')
print(r.status_code)

print('HTTP header')
print(r.headers['content-type'])

print('literal code')
print(r.encoding)

print('HTML output')
print(r.text)