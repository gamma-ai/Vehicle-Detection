import cv2
filename = 'traffic1.avi'
cap = cv2.VideoCapture(filename)
reference_frame =None #first frame
image_area = None
while True:
	ret,frame = cap.read()
	#print ret = frame = True, last frame =false

	if ret is False:
		break

	else: #getting grayscale/threshold frame
		if reference_frame is None:
			reference_frame = frame
			reference_frame = cv2.cvtColor(reference_frame,cv2.COLOR_BGR2GRAY)
			image_area = reference_frame.shape[0] * reference_frame.shape[1]
			continue
###COLORSCALES#######
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		difference = cv2.absdiff(reference_frame,gray)
		blur = cv2.medianBlur(difference,31)
####FIND CONTOURS
		f, threshold = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
		(_,contours,_) = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
######DRAW CONTOURS
		for i in contours:
			contour_area = cv2.contourArea(i)
			if (contour_area > 0.001*image_area)and( contour_area <0.08 *image_area): #-->removing false contours

				(x,y,w,h)=cv2.boundingRect(i) #--> RECTANGLE FOR EACH CAR
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2) ###-> COLOR FOR BOX

		cv2.imshow("frames",frame)
		if cv2.waitKey(1) == ord('q'):
			break