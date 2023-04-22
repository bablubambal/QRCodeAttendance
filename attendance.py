import os
import datetime
import time

import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np

log_path = 'attendance.csv'
most_recent_access = {}
authorized_users =[]
time_between_logs_th = 25
print(most_recent_access)

def GetAuthorizedStudentList():
    with open('students.csv', 'r') as f:
        authorized_users.extend([l[:-1] for l in f.readlines() if len(l) > 2])
        print("authorized users: ",authorized_users)
        f.close()




def DecodeAttendance(frame):
    qr_info = decode(frame)
    if len(qr_info) > 0:
        qr = qr_info[0]
        data = qr.data
        rect = qr.rect
        polygon = qr.polygon
        print(data.decode(),authorized_users)
        print(data.decode() in authorized_users)
        print(most_recent_access)
        if data.decode() in authorized_users:
            cv2.putText(frame, 'ACCESS GRANTED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            if data.decode() not in most_recent_access.keys() or time.time() - most_recent_access[data.decode()] > time_between_logs_th:
                most_recent_access[data.decode()] = time.time()
                with open(log_path, 'a') as f:
                    f.write('{},{}\n'.format(data.decode(), datetime.datetime.now()))
                    f.close()
            if data.decode()  in most_recent_access.keys():
                cv2.putText(frame, 'Attendance Already Marked', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)


        else:
            cv2.putText(frame, 'ACCESS DENIED', (rect.left, rect.top - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                            (0, 255, 0), 5)

        frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)

    cv2.imshow('webcam', frame)

    

GetAuthorizedStudentList()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    DecodeAttendance(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    

cap.release()
cv2.destroyAllWindows()
