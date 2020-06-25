import cv2
#Objects to hold the 3 different cascade files.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#function to detect the Haar like Cascade features.
def detect(gray, frame):
    #this function detects the grey converted image and the colored images.
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    #for each detected face.
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 1)
        #Now withing this frame we will detect the other 2 features to reduce the processing time.
        #We will create a region of interest within the face frame for both grey and colored image.
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #detect eyes within the face boundary.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 1)
        #detect smile within the face boundary.
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 35)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 1)
            #Add text to notify if smiling
            cv2.putText(frame, 'Smiling', (x, y-10), cv2.FONT_ITALIC, 0.7, (36,255,12), 2)
    return frame
    
#we will create a video capture object.
video_capture = cv2.VideoCapture(0) 
#Here 0 is for the primary camera 1 will be for external camera
#video_capture = cv2.VideoCapture('videofile.mp4') we can use this for capturing a video file directly.
#Now we will add a while loop and use 'q' to break the capture
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#this is used to convert the frame to grey image
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    #Now we shall add a keyboard interrupt to stop the process on pressing the 'q' key.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
#now to close the capture and also close the windows.
video_capture.release()
cv2.destroyAllWindows()