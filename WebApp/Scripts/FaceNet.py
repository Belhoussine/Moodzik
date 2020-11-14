import os
import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image


mood_map = {
    0: 'angry',
    1: 'disgust',
    2: 'fear',
    3: 'happy',
    4: 'sad',
    5: 'surprise',
    6: 'neutral',
}


def mood_to_num(mood):
    for key, value in mood_map.items():
        if mood == value:
            return key


def num_to_mood(num):
    return mood_map[num]


def crop_face(frame, x, y, w, h):
    # Cropping face
    face = frame[y: y+w, x: x+h]

    # Processing face
    face = cv2.resize(face, (48, 48))
    face_array = image.img_to_array(face)
    face_array = np.expand_dims(face_array, axis=0)
    face_array /= 255.0
    return face_array


def facecapture():
    # Defining path
    models_path = "../Models/"

    # Loading EmotioNet and adding weights
    EmotioNet = model_from_json(
        open(models_path + "Model_1_0.81/EmotioNet_1.json", "r").read())
    EmotioNet.load_weights(models_path + 'Model_1_0.81/EmotioNet_weights_1.h5')

    # Loading FaceNet model
    FaceNet = cv2.CascadeClassifier(
        models_path + 'haar_cascade/haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = capture.read()
        if not ret:
            continue

        # Turning frame to gray sclae
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_faces = FaceNet.detectMultiScale(gray_frame, 1.32, 5)

        for (x, y, w, h) in detected_faces:
            # Drawing rectangle around detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h),
                          (100, 200, 100), thickness=5)

            # Cropping detected face and feeding it to EmotioNet
            face = crop_face(gray_frame, x, y, w, h)
            prediction = num_to_mood(np.argmax(EmotioNet.predict(face)))

            cv2.putText(frame, prediction, (int(x), int(y)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the resulting frame
        # cv2.imshow('frame', frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    capture.release()
    cv2.destroyAllWindows()
