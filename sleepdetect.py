import cv2
import numpy as np
import serial

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
open_eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
right_eyes = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
left_eyes = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
cap=cv2.VideoCapture(0)

while(True):
	ret,frame = cap.read()
	gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	face = face_detect.detectMultiScale(gray,1.2,2)
	
	for (x,y,w,h) in face:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_color = frame[y:y+h,x:x+w]
		roi_gray = frame[y:y+h,x:x+w]
		oeyes = open_eyes.detectMultiScale(roi_gray,1.3,30)
		reyes = right_eyes.detectMultiScale(roi_gray,1.3,20)
		leyes = left_eyes.detectMultiScale(roi_gray,1.3,20)
		print(len(oeyes))		
		for (oex,oey,oew,oeh) in oeyes:
			cv2.rectangle(roi_color,(oex,oey),(oex+oew,oey+oeh),(0,255,0),2)
		for (rex,rey,rew,reh) in reyes:
			cv2.rectangle(roi_color,(rex,rey),(rex+rew,rey+reh),(0,0,255),2)
		for (lex,ley,lew,leh) in leyes:
			cv2.rectangle(roi_color,(lex,ley),(lex+lew,ley+leh),(0,255,255),2)

		if len(leyes)!=0:
			if len(oeyes) == 0:
				print('Sleep')
			else:
				print('Wake')

		if len(reyes)!=0:
			if len(oeyes) == 0:
				print('Sleep')
			else:
				print('Wake')


	cv2.imshow('frame',frame)


	k= cv2.waitKey(10) & 0xff
	if k== ord('q'):
		break

cap.release()
cv2.DestroyAllWindows()