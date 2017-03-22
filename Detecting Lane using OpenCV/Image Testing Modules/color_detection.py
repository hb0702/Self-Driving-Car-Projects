import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

image = (mpimg.imread('t4.jpg')).astype('uint8')
img=image
line_image = np.copy(image)


white = [200, 200, 200]
yellow= [200, 200, 0] #choose whatever is above this value
color_thresholds = (image[:,:,0] < white[0]) | \
                    (image[:,:,1] < white[1]) | \
                    (image[:,:,2] < white[2])
color_thresholds2=(image[:,:,0] < yellow[0]) | \
                    (image[:,:,1] < yellow[1]) | \
                    (image[:,:,2] < yellow[2])

image[~color_thresholds2] = [255, 0, 0]
print(type(image))

#plt.imshow(line_image)
#plt.show()

w=np.copy(img)
y=np.copy(img)

lower_white = np.array([60, 0, 0])
upper_white = np.array([100, 100, 255])

lower_yellow = np.array([80, 100, 100])
upper_yellow = np.array([120, 255, 255])
white = cv2.inRange(img, lower_white, upper_white)
yellow = cv2.inRange(img, lower_yellow, upper_yellow)