import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# http://127.0.0.1:5000をルートとして、("")の中でアクセスポイント指定
# @app.route("hoge")などで指定すると、http://127.0.0.1:5000/hogeでの動作を記述できる。


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/bc")  # buisiness card
def bc():
    with open("bc.json", encoding="utf-8_sig") as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()
