import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
image = cv2.imread("car.jpg")

# convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # perform the canny edge detector to detect image edges
# edges = cv2.Canny(gray, threshold1=30, threshold2=100)



# Window name in which image is displayed 
window_name = 'Image'

# Start coordinate, here (0, 0) 
# represents the top left corner of image 
start_point = (500, 500) 
  
# End coordinate, here (250, 250) 
# represents the bottom right corner of image 
end_point = (1000, 1000) 
  
# Green color in BGR 
color = (0, 255, 0) 
  
# Line thickness of 9 px 
thickness = 40
  
# Using cv2.line() method 
# Draw a diagonal green line with thickness of 9 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 

face_cascade = cv2.CascadeClassifier('cars.xml')
  
# car detection.
cars = face_cascade.detectMultiScale(image, 1.1, 2)

ncars = 0
for (x,y,w,h) in cars:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    ncars = ncars + 1
# # Displaying the image  
# cv2.imshow(window_name, image)  

# show the grayscale image
plt.imshow(image, cmap="gray")
plt.show()