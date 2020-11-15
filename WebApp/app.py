from flask import Flask, render_template, url_for, request, redirect, Response
from datetime import datetime
from PlaySong import play_music, stopMusic, pauseMusic,unpauseMusic
from NeuralNets.FaceNet import facecapture, get_mood
# import GenerateSong.utils 
from GenerateSong.generate import generateSong

app = Flask(__name__)

# musicfile = './GenerateSong/GeneratedSong/moodzik.mid'

musicfile = './static/MidiFiles/POC.mid'

mood = 'neutral'

@app.route('/')
def index():
    stopMusic()
    return render_template('index.html')

@app.route('/generating')
def generating():
    global mood
    mood = get_mood()
    print(mood.upper())
    # generateSong(mood.lower()).apply
    play_music(musicfile)
    return render_template('musicpage.html')


@app.route('/music')
def music():
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
