from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://eastjin:1q2w3e4r@cluster0.nb3pybc.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/mypage')
def mypage():
    return render_template('upload.html')

@app.route('/')
def homepage():
    return render_template('main.html')

# @app.route("/connect")
# def connect():
#     return jsonify({'msg': '연결완료!'})
#     return redirect(url_for('mypage'))


# 등록 화면
@app.route('/upload', methods=['GET'])
def home():
    # if request.method =='POST':
    #     return redirect(url_for('upload_post'))
    return render_template('upload.html')


# 등록 동작방식
@app.route("/upload_post", methods=["POST"])
def bucket_post():
    # title_receive = request.form['title_give']
    # url_receive = request.form['url_give']
    # contents_receive = request.form['contents_give']

    title_receive = request.form['title']
    url_receive = request.form['url']
    contents_receive = request.form['contents']

    print(title_receive)

    hobby_list = list(db.hobby.find({}, {'_id': False}))
    count = len(hobby_list) + 1

    doc = {
        'num': count,
        'title': title_receive,
        'url': url_receive,
        'contents': contents_receive
        # 'delete':0
    }
    db.hobby.insert_one(doc)
    # return jsonify({'msg': 'save'})
    return render_template('main.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
