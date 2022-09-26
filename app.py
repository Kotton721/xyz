# -*- coding: utf-8 -*-
from flask import Flask
from hashlib import new
from importlib.resources import path
from flask import Flask,render_template,send_from_directory
from flask import request
import folium
import pandas as pd
import re
from folium import plugins
app = Flask(__name__)


fname="gpsexa.gpx"
with open(fname, mode='r') as f:
    r = f.read()
    
#座標データのみ取得
origin=re.findall(r'<trkpt.*>',r)

# 上のリストから、座標のみ取得
strlist = [re.findall('\d{1,8}\.\d{1,8}',i) for i in origin]

data = [[float(j) for j in i] for i in strlist]

savename="locations.csv"
df=pd.DataFrame(data)
df.to_csv(savename,index=None)

df_read=pd.read_csv(savename)

center=df.mean().tolist()

data=df.to_numpy().tolist()



#「/」へアクセスがあった場合に、testhtmlを表示
@app.route("/mainpage",methods=['GET'])
def hello():
    return render_template("test.html")

#音声ファイルを返す
@app.route("/music/voice")
def play_music():
    return send_from_directory("music", "la.wav")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return render_template('login.html')

def do_login():
    user_name = request.form['user_name']
    password = request.form['password']
    if user_name != 'xyz' or password != 'kumikomi':
        return render_template('login.html', error_message='ユーザー名かパスワードが間違っています')
    return render_template('login.html', success_message='ログイン処理成功！')

#「/nextpage」へアクセスがあった場合に、地図を返す
@app.route("/nextpage", methods=["GET"])
def map():
    map=folium.Map(
        location=center,
        zoom_start=20
    )
    antpath=plugins.AntPath(
        locations=data).add_to(map)
    return map._repr_html_()

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run()
