from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    title_receive = request.form['title_give']  
    text_receive = request.form['text_give'] 

    article = {'title': title_receive,'text': text_receive}

    db.articles.insert_one(article)

    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


@app.route('/memo', methods=['GET'])
def read_articles():
    result = list(db.articles.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)