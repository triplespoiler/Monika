from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    UPLOAD_FOLDER = 'C:/Users/user/Downloads/flask_web/flask-web2/web/static'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from . import authors   #同じフォルダ内にあるauthors.pyを参照
    app.register_blueprint(authors.bp)  #オブジェクトbpを登録した

    from . import books
    app.register_blueprint(books.bp)

    app.config.from_mapping(  
        SECRET_KEY='temp',   #暗号化キー。実際はもっと複雑なものを用いるべし
        DATABASE=os.path.join(app.instance_path, 'bookdb.sqlite3'),
         #フォルダ「instance」（既定）に置いた「bookdb.sqlite3」を参照
    )

   #このアプリで安心してデータベースを使えるようにする
    from . import bookdb
    bookdb.init_app(app)

    return app