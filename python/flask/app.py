from flask import Flask, request, session, g, redirect, url_for, abort, flash

# アプリの初期化
app = Flask(__name__)
# コンフィグの追加（別ファイルの時は引数を変更する）
# app.config.from_object(__name__)
# 環境変数から設定を取得するとき
# app.config.from_envvar('FLASK_SETTINGS', silent=True)

# 直接このファイルが実行されたときのみ、アプリケーションが起動
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run()

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World\n'

@app.route('/post', methods=['POST'])
def post():
    return 'POST is success\n'