import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'images'
images = []
personName = []
myList = os.listdir(path)
print(myList)
for cu_img in myList:
    current_Image = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Image)
    personName.append(os.path.splitext(cu_img)[0])
print(personName)

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = faceEncodings(images)
print("All Encodings Complete!!!!")

def attendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readLines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            
#         if name not in nameList:
#             time_now = datetime.now()
#             tStr = time_now.strftime('%H:%M:&S')
#             dStr = time_now.strftime('%d/%m/%Y')
#             f.writelines(f'{name},{tStr},{dStr}')
                                     
        
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
    
    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_locations(faces,facesCurrentFrame)
    
    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
        matchIndex = np.argmin(faceDis)
        
        # if matches[matchIndex]:
        #     name = personName[matchIndex].upper()
        #     print(name)
        #     y1, x2, y2, x1 = faceLoc
        #     y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        #     cv2.rectangle(frame, (x1,y1),(x2,y2), (0,225,0), 2)
        #     cv2.rectangle(frame, (x1,y2-35),(x2,y2), (0,225,0), cv2.FILLED)
        #     cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,225), 2)
        #     attendance(name)
            
        cv2.imshow("Camera", frame)
        if cv2.waitKey(10) == 13:
            break
    cap.relese()
    cv2.destroyAllWindows
