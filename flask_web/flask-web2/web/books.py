from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from web.bookdb import get_db 
from web.files import save_img, write_file

bp = Blueprint('books', __name__) #'authors'から書き換える

@bp.route('/books', methods=['GET'])
def all():
    db=get_db()
    alldata = db.execute('SELECT * FROM books').fetchall()
    return render_template('books/all.html', books=alldata)

@bp.route('/books/new', methods=['GET', 'POST'])
def new():
    db = get_db() #GETでもPOSTでもデータベースを使う
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        db.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author) #coverは初期値を用いる
        )
        db.commit()        
        return redirect(url_for('books.all'))
    #GETの場合、著者の集合authorsを渡す
    authors = db.execute('SELECT * FROM authors').fetchall()
    return render_template('books/new.html', authors=authors)

@bp.route('/books/show/<book_id>', methods=['GET'])
def show(book_id):
    db=get_db()
    book = db.execute('SELECT * FROM books where id=?', book_id).fetchone()
    return render_template('books/show.html', book=book)

@bp.route('/books/upload/<book_id>', methods=['GET', 'POST'])
def upload(book_id):
    db=get_db()
    if request.method == 'POST':
        if 'file' in request.files: #リクエストにファイル情報が含まれていたら
            file = request.files['file']
            save_img(file) #files.pyで定義したメソッド
            db.execute( #表booksでのファイル名を初期値から固有値に変更
            "UPDATE books SET cover=? where id=?",
            (file.filename, book_id)
            )
            db.commit()
        
        #ファイルのアップロードに失敗したときの処置
        return redirect(url_for('books.show',book_id=book_id) )

    #GETで読み込まれた時    
    book = db.execute('SELECT * FROM books where id=?', book_id).fetchone()
    return render_template('books/upload.html', book=book)

@bp.route('/books/write', methods=['GET'])
def write():
    cvs_str=""
    db=get_db()
    alldata = db.execute('SELECT * FROM books').fetchall()
    for data in alldata:
        cvs_str += ",".join([data['title'],data['author'],data['cover']])
        cvs_str += "\n"
    write_file("books.csv",cvs_str) 
    return render_template('books/write.html', str=cvs_str)


