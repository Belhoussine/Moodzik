from flask import Flask, render_template, url_for, request, redirect, Response
from datetime import datetime
from PlaySong import play_music, stopMusic, pauseMusic,unpauseMusic
from Scripts.FaceNet import facecapture

app = Flask(__name__)

musicfile = './Static/MidiFiles/output.mid'

started = False

@app.route('/')
def index():
    stopMusic()
    global started 
    started = False
    return render_template('index.html')


@app.route('/music')
def music():
    global started
    play_music(musicfile)
    started = True
    return render_template('musicpage.html')

@app.route('/music/pause')
def musicpause():
    pauseMusic()
    return render_template('musicpage.html')

@app.route('/music/play')
def musicplay():
    unpauseMusic()
    return render_template('musicpage.html')

@app.route('/camera')
def camera():
    return Response(facecapture(), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return render_template('camerapage.html')


if __name__ == "__main__":
    app.run(debug=True)
