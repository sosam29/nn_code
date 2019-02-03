import numpy as np 
import cv2

import os.path

srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_2.jpg"
if os.path.isfile(srcfname):
    img = cv2.imread(srcfname)
    cv2.imshow("Original", img)
else:
    raise "No such file exists"
#cv2.imshow("Original", img)
cv2.waitKey()
#Image scaling section
img_inter_cubic = cv2.resize(img, None, fx=.75, fy=.75,interpolation=cv2.INTER_CUBIC)

cv2.imshow("CUBIC", img_inter_cubic)

cv2.waitKey()

img_inter_area= cv2.resize(img, (600, 300), interpolation=cv2.INTER_AREA)

cv2.imshow("inter area", img_inter_area)

cv2.waitKey()


img_inter_linear= cv2.resize(img, None, fx=.5, fy=.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("inter Linear", img_inter_linear)

cv2.waitKey()




# Close all windows
cv2.destroyAllWindows()