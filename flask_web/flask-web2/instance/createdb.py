import sqlite3 #sqlite3を操作するライブラリ

#表authorsを作成
DROP_AUTHORS="DROP TABLE IF EXISTS authors"  #すでにある場合は削除しておく
CREATE_AUTHORS='''CREATE TABLE authors
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT,
bio TEXT)'''

#authorsにテストデータを入れる
INSERT_AUTHOR='''INSERT INTO authors (name, bio)
VALUES ('ニュートン',
'「なぜリンゴが木から落ちるのかという疑問から万有引力の法則を発見した」という伝説がある')
''' 

#表authorsに入れたデータを表示
SELECT_AUTHORS="SELECT * FROM authors"

#データベース操作
conn = sqlite3.connect('bookdb.sqlite3') #作成されたデータベースファイル
c = conn.cursor() #カーソル

c.execute(DROP_AUTHORS)
c.execute(CREATE_AUTHORS)
c.execute(INSERT_AUTHOR) 
conn.commit() #一括実行

#表authorsを検索
c.execute(SELECT_AUTHORS)
result=c.fetchone() #ひとつだけ読み出す
print(result)
