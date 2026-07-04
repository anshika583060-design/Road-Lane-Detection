import cv2
import numpy as np

# 1. Image load karein
image = cv2.imread('images 1.jpg') 
if image is None:
    print("Error: Image load nahi hui. File ka naam check karein.")
else:
    # 2. Grayscale mein convert karein
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Blur aur Canny Edge Detection
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    # 4. Hough Transform se lines detect karein
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=10)

    # 5. Lines draw karein
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # 6. Output show karein
    cv2.imshow('Road Lane Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()