import cv2
import numpy as np 
import os

srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_5.jpg"
if os.path.isfile(srcfname):
    img = cv2.imread(srcfname)
    cv2.imshow("Original", img)
    # print(img.shape)
else:
    raise "No such file exists"
#cv2.imshow("Original", img)
cv2.waitKey()

# blurred = cv2.blur(img, (20,20))
# cv2.imshow("BLurred", blurred)

# cv2.waitKey()

blur = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("Gaussionblur", blur)

cv2.waitKey()

smooth = cv2.addWeighted(blur,2,img,-1,0)

cv2.imshow("Smooth", smooth)
cv2.waitKey()

bxoreds = cv2.bitwise_xor(blur, smooth)
cv2.imshow("bxoreds", bxoreds)

cv2.waitKey()


xoredb = cv2.bitwise_xor(smooth,blur)
cv2.imshow("xoredb", xoredb)

cv2.waitKey()

ANDED = cv2.bitwise_and(smooth,blur)
cv2.imshow("ANDED", ANDED)

cv2.waitKey()

REVENDED = cv2.bitwise_and(blur, smooth)
cv2.imshow("REVANDED", REVENDED)

cv2.waitKey()

cv2.destroyAllWindows()