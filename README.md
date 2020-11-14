# Moodzik

## MindMap:
![mindmap](./mindmap/mindmap.png)

## 1. Face detection:
- [ ] Get input from camera
- [ ] Build / Train CNN_01:
    - [ ] Find face dataset
- [ ] Capture face:
    - [ ] Capture frame
    - [ ] Crop frame to identify face only
- [ ] Process captured face
- [ ] Feed to CNN_02

## 2. Mood detection:
- [ ] Get face image from CNN_01
- [ ] Build CNN_02:
    - [x] Design network architecture:
        - [x] Convolution layers.
        - [x] Fully connected Neural Network.
        - [x] Define activation functions.
        - [ ] Define output labels.
        - [x] Define optimizer / loss function.

- [ ] Train CNN_02:
    - [ ] Dataset:
        - [ ] Pre-processing:   
            - [ ] Normalize data
        - [ ] Image processing:
            - [ ] Convert to grayscale
    - [ ] Train model
    - [ ] Save model as JSON

- [ ] Predict mood from image

## 3. Music Generation:
- [ ] Get mood from CNN_02
- [ ] Train Music generator Neural Network:
    - [ ] Find music dataset
    - [ ] Feed music in ABC format
- [ ] Generate music based on mood:
    - [ ] MIDI file format

## 4. Play Music:
- [ ] Desing GUI
- [ ] Use library / software to play generated midi file

## 5. Publish web-app:
- [ ] Use flask to serve app
- [ ] Host in a remote server
- [ ] Purchase domain name
- [ ] Deploy
