import sqlite3

#表booksを作成
DROP_BOOKS="DROP TABLE IF EXISTS books"
CREATE_BOOKS='''CREATE TABLE books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
cover TEXT DEFAULT 'book.png')''' #初期値を設定

#データベース操作
conn = sqlite3.connect('bookdb.sqlite3')
c = conn.cursor()
c.execute(DROP_BOOKS)
c.execute(CREATE_BOOKS) #まだデータを入れない
conn.commit()
conn.close()