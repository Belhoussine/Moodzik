from flask import Flask, render_template, url_for, request, redirect, Response
from datetime import datetime
from PlaySong import play_music, stopMusic
from Scripts.FaceNet import facecapture, get_mood
from GenerateSong.main import generateMoodzik
import os

app = Flask(__name__)

musicfile = './Static/MidiFiles/output.mid'


@app.route('/')
def index():
    stopMusic()
    return render_template('index.html')


@app.route('/music')
def music():
    mood = get_mood()
    play_music(musicfile)
    return render_template('playingpage.html')

@app.route('/camera')
def camera():
    return Response(facecapture(), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return render_template('camerapage.html')
    
if __name__ == "__main__":
    app.run(debug=True)
