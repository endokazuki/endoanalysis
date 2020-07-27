import sqlite3

conn = sqlite3.connect('family.db')
#family.dbファイルを開き、コネクションを取得する

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

c.execute('INSERT INTO family VALUES(?,?,?)',(1,'setsuko',49))
#listオブジェクトの挿入

c.execute('INSERT INTO family VALUES(:rank,:name,:age)',{'rank':2,'name':'kazuki','age':24})
#dictオブジェクトの挿入

c.executemany(
	'INSERT INTO family VALUES(:rank,:name,:age)',
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