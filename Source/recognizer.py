import cv2
import numpy as np
import os
import time
import datetime
from create_excel import append_data_to_excel
from serach import search_for_number_in_excel_column
from file_dialog import YourClass

people = [name for name in os.listdir('../Resources/Faces') if os.path.isdir(os.path.join('../Resources/Faces', name))]
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('../Resources/Models/face_trained_model.yml')

CONFIDENCE_THRESHOLD = 60


def recognize_face(faces_roi):
    label, confidence = face_recognizer.predict(faces_roi)

    if confidence < CONFIDENCE_THRESHOLD:
        return label, confidence
    else:
        return -1, confidence


def process_image(image_path, people):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Error: Failed to read the image at {image_path}")
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # haar_cascade = cv2.CascadeClassifier('lbp_face.xml')
    haar_cascade = cv2.CascadeClassifier('../Resources/Models/haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y + h, x:x + w]
        label, confidence = recognize_face(faces_roi)

        if label != -1:
            person_name = people[label]
            confidence_percent = round(100 - confidence)
            label_text = f"{person_name}"

            if search_for_number_in_excel_column(f"Attendance/{datetime.date.today()}.xlsx", int(person_name)):
                print(f"The number {person_name} exists in the first column of the Excel file.")
            else:
                append_data_to_excel(f"Attendance/{datetime.date.today()}.xlsx", [[int(person_name)]])

            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), thickness=2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        else:
            unknown_label_text = f"Unknown"
            cv2.putText(frame, unknown_label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), thickness=2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)

    cv2.imshow('Processed Image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


your_instance = YourClass()
image_path = your_instance.start()
# image_path = "ourImage.jpg"
# process_image(image_path)
process_image(image_path, people)
