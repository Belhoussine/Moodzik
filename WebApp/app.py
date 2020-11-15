from flask import Flask, render_template, url_for, request, redirect, Response
from datetime import datetime
from PlaySong import play_music, stopMusic, pauseMusic,unpauseMusic
from Scripts.FaceNet import facecapture

app = Flask(__name__)

musicfile = './Static/MidiFiles/moodzik.mid'

# moodzik = generateSong(mood)

@app.route('/')
def index():
    stopMusic()
    return render_template('index.html')

@app.route('/generating')
def generating():
    generateSong(mood)
    return render_template('musicpage.html')


@app.route('/music')
def music():
    mood = get_mood()
    play_music(musicfile)
    return render_template('musicpage.html')

@app.route('/music/pause')
def musicpause():
    pauseMusic()
    return render_template('pausedmusic.html')

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
