from flask import Flask, render_template, request, jsonify

import jwt, datetime, requests

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.fgag4po.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)
@app.route('/detail')
def page_detail():
    return render_template('detail.html')

### 댓글 포스트
@app.route("/api/comments", methods=["POST"])
def posting_comments():
    comment_receive = request.form['comment_give']
    comment_list = list(db.comments.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
         'num': count,
         'comment': comment_receive
    }
    db.comments.insert_one(doc)

    return jsonify({'msg': '저장되었습니다!'})

# @app.route("/api/comments", methods=["POST"])
# def posting_comments():
    # token_receive = request.cookies.get('mytoken')
    # try:
    #     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #
    #     # 댓글 포스팅하기
    #     user_info = db.users.find_one({"login-id": payload["id"]})
    #     hobby_info = db.hobby.find_one({"num": payload["id"]})
    #     comment_receive = request.form["comment_give"]
    #
    #     print(type(date_receive))
    #     doc = {
    #         "username": user_info["username"],
    #         "num": hobby_info["num"],
    #         "comments": comment_receive
    #     }
    #     db.comments.insert_one(doc)
    #
    #     return jsonify({"result": "success", 'msg': '포스팅 성공'})
    #
    # except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
    #     return redirect(url_for("/detail"))

@app.route("/detail/comments_list", methods=["GET"])
def comments_list_get():
    comments_list = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})

@app.route("/api/comments/delete", methods=["POST"])
def comment_delete():
    comment_receive = request.form['comment_give']
    db.comments.delete_one({"comment":comment_receive})

    return jsonify({'msg': '삭제되었습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)