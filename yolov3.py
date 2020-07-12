# look at the image once


# divide the image into a grid with several squares with different sizes

# bounding box, predict either a box exists or not and the class of that boudning box

 
import cv2
 
# read image
img = cv2.imread('rsz_car.jpg', cv2.IMREAD_UNCHANGED)
 
# get dimensions of image
dimensions = img.shape
 
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

width10 = width / 10
height10 = height / 10

print('width x10%', width10)
print('height x10', height10)


