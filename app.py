from flask import Flask, render_template, url_for, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from synthasizesong import play_music, stopMusic

app = Flask(__name__)

musicfile = './Music/output.mid'


@app.route('/')
def index():
    stopMusic()
    return render_template('index.html')


@app.route('/music')
def music():
    play_music(musicfile)
    return render_template('playingpage.html')


if __name__ == "__main__":
    app.run(debug=True)
