from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.oxtkdhc.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/mypage')
def mypage():
   return "This is my page"

# @app.route("/connect")
# def connect():
#     # return jsonify({'msg':'연결완료!'})
#     return redirect(url_for('mypage'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)