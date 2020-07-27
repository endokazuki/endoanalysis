import MySQLdb

conn = MySQLdb.connect(db='scraping',user='scraper',passwd='password',charset='utf8mb4')



c = conn.cursor()
#カーソルを取得する（DBを手に取る）
c.execute('DROP TABLE IF EXISTS family')
#過去にfamilyテーブルが存在する場合削除する
#execute:SQLを実行する
c.execute("""
CREATE TABLE family(
	rank integer,
	name text,
	age integer
)
""")
#familyテーブルの作成

c.execute('INSERT INTO family VALUES(%s,%s,%s)',(1,'setsuko',49))
#listオブジェクトの挿入

c.execute('INSERT INTO family VALUES(%(rank)s,%(name)s,%(age)s)',{'rank':2,'name':'kazuki','age':24})
#dictオブジェクトの挿入

c.executemany(
	'INSERT INTO family VALUES(%(rank)s,%(name)s,%(age)s)',
	[
	{'rank':3,'name':'tiaki','age':22},
	{'rank':4,'name':'tamaki','age':17},
	]
	)
#複数回のSQL文の実行

conn.commit()
#変更を保存する

c.execute('SELECT * FROM family')
for row in c.fetchall():
	print(row)

conn.close()
#コンソールを閉じる（DBを手放す）