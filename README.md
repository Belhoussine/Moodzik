# Moodzik

### Clone & Install dependencies:
```
    git clone https://github.com/Belhoussine/Moodzik.git  
    cd Moodzik/  
    sudo apt-get install build-essential libasound2-dev ffmpeg libjack-dev portaudio19-dev timidity freepats
    pip3 install -r requirements.txt  
```

### Run Moodzik locally:
```
    python ./WebApp/app.py  
    firefox http://127.0.0.1:5000/
```

## MindMap:
![mindmap](./MindMap/mindmap.png)

## 1. Face detection:
- [x] Get input from camera
- [x] Use Haar_Cascade model
- [x] Capture face:
    - [x] Capture frame
    - [x] Crop frame to identify face only
- [x] Process captured face
- [x] Feed to CNN_02

## 2. Mood detection:
- [x] Get face image from CNN_01
- [x] Build CNN_02:
    - [x] Design network architecture:
        - [x] Convolution layers.
        - [x] Fully connected Neural Network.
        - [x] Define activation functions.
        - [x] Define output labels.
        - [x] Define optimizer / loss function.

- [x] Train CNN_02:
    - [x] Dataset:
        - [x] Pre-processing:   
            - [x] Normalize data
        - [x] Image processing:
            - [x] Convert to grayscale
    - [x] Train model
    - [x] Save model as JSON

- [x] Predict mood from image
- [x] Display mood

## 3. Music Generation:
- [ ] Get mood from CNN_02
- [ ] Train Music generator Neural Network:
    - [ ] Find music dataset
    - [ ] Feed music in ABC format
- [ ] Generate music based on mood:
    - [ ] Generate MIDI file based on mood

## 4. Play Music:
- [ ] Desing GUI
- [x] Use Pygame on generated midi file

## 5. Publish web-app:
- [ ] Use flask to serve app
- [ ] Host in a remote server
- [ ] Purchase domain name
- [ ] Deploy
