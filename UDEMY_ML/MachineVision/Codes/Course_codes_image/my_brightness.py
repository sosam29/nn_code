import numpy as np 
import cv2

import os

srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_5.jpg"
if os.path.isfile(srcfname):
    img = cv2.imread(srcfname)
    cv2.imshow("Original", img)
    print(img.shape)
else:
    raise "No such file exists"
#cv2.imshow("Original", img)
cv2.waitKey()

matrix = np.ones(img.shape, dtype='uint8')*128
# zerosmatrix = np.zeros(img.shape,dtype='uint8')*255

img_added = cv2.add(img, matrix)
cv2.imshow("ADDED", img_added) 
cv2.waitKey()

dilateby = np.ones((3,3), dtype='uint8')
img_subtracted = cv2.dilate(img, dilateby)
cv2.imshow("Dilated", img_subtracted)
cv2.waitKey()
   

# Close all windows
cv2.destroyAllWindows()