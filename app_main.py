from flask import Flask, redirect
from flask import request
from flask import render_template
from flask import session
import json
app = Flask(__name__,#__name__代表目前執行的模組
            static_folder="static",#靜態檔案的資料夾名稱
            static_url_path="/static",#靜態檔案對應到的網址路徑(/後面空白默認資料夾名稱)
            )

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)