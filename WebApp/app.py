from flask import Flask, render_template, url_for, request, redirect, Response
from datetime import datetime
from PlaySong import play_music, stopMusic, pauseMusic,unpauseMusic
from NeuralNets.FaceNet import facecapture, get_mood
from GenerateSong.generate import generateSong

app = Flask(__name__)

moodzik = './GenerateSong/GeneratedSongs/moodzik.mid'
generated = False

@app.route('/')
def index():
    stopMusic()
    return render_template('index.html')

@app.route('/generating')
def loading():
    return render_template('loadingpage.html')


@app.route('/loading')
def generating():
    global generated
    mood = get_mood()
    if not generated:
        print(mood.upper())
        generated = True
        generateSong(mood)
    return redirect("/music", code=302)
    
@app.route('/music')
def music():
    global generated
    generated = False
    play_music(moodzik)
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
