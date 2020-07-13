# --- image
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
print('height x10%', height10)


columns = img.shape[0]
rows = img.shape[1]

pixel = img[1,1]
print(pixel)

startColumn = 0
startRow = 0

for i in range(startColum, rows):
    for j in range(startRow, columns):
        print(img[j,i])
startColumn = startColumn + width10
startRow = startRow + height10

# get the dimensions of the iamge and slice in a grid, can be 10 x 10

# input


# backbone

# --- cutmix and mosaic , csp darknet 53, darknet 52 ? cnn, all of the rest is to enchance the cnn performance

# neck

# --- fpn , pan, rfb

# dense predictions

# --- rpn, yolo, ssd

# sparse predictions

# faster r-cnn , rfcn

