import csv

with open('name.csv','w',newline='') as f :
    writer = csv.writer(f)
    writer.writerow(['rank','name','age'])
    writer.writerows([
        ['1','遠藤節子','49'],
['2','遠藤主基','24'],
['3','遠藤智映','22'],
['4','遠藤珠姫','17'],
])