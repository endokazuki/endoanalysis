import json

family = [
    {'rank':1,'name':'setuko','age':49},
    {'rank':2,'name':'kazuki','age':24},
    {'rank':3,'name':'tiaki','age':22},
    {'rank':4,'name':'tamaki','age':17}
    ]
#家族構成のdict（辞書）オブジェクトを変数familyに格納する

print(json.dumps(family))
#変数familyをjson形式で標準出力する
#但し、このままだとascii以外の文字は適正に出力されない

print(json.dumps(family,ensure_ascii=False,indent=2))
#変数familyをjson形式で指定出力する
#ensure_ascii:ascii以外の文字を適正な形で出力する
#indent:改行＋インデントを実行

