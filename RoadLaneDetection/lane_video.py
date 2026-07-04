import cv2
import numpy as np

cap = cv2.VideoCapture('road_video.mp4.mp4') 

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
        
    # Resize taaki video saaf dikhe
    frame = cv2.resize(frame, (800, 600)) 
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny parameters ko thoda badha kar dekhein
    edges = cv2.Canny(blur, 100, 200) 
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=50)
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            
    cv2.imshow('Real-time Lane Detection', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'): # 25ms delay se video smooth chalegi
        break

cap.release()
cv2.destroyAllWindows()