import pygame


def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    pygame.mixer.music.load(music_file)
    try:
        pygame.mixer.music.load(music_file)
        print("Music file %s loaded!" % music_file)
    except:
        print("File %s not found! " % (music_file))
        return
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():
    #     pygame.time.wait(1000)
    

def stopMusic():
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()

def pauseMusic():
    pygame.mixer.music.pause()
def unpauseMusic():
    pygame.mixer.music.unpause()

# pick a midi music file you have ...
midi_file='./GenerateSong/GeneratedSongs/POC.mid'
freq=44100    # audio CD quality
bitsize=-16   # unsigned 16 bit
channels=2    # 1 is mono, 2 is stereo
buffer=1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
# try:
#     play_music(midi_file)
# except KeyboardInterrupt:
#     # if user hits Ctrl/C then exit
#     # (works only in console mode)
#     pygame.mixer.music.fadeout(1000)
#     pygame.mixer.music.stop()
#     raise SystemExit



