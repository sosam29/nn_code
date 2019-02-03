import numpy as np 
import cv2

import os.path

srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_3.jpg"
if os.path.isfile(srcfname):
    img = cv2.imread(srcfname)
    cv2.imshow("Original", img)
else:
    raise "No such file exists"
#cv2.imshow("Original", img)
cv2.waitKey()

flipH = cv2.flip(img, 1)
cv2.imshow("Horz", flipH)
cv2.waitKey()

flipV = cv2.flip(img, 0)
cv2.imshow("Vert", flipV)
cv2.waitKey()


flipNeg = cv2.flip(img, -1)
cv2.imshow("Neg", flipNeg)
cv2.waitKey()

flipNeg2= cv2.flip(img, 7)
cv2.imshow("Neg2", flipNeg2)
cv2.waitKey()
# Close all windows
cv2.destroyAllWindows()
