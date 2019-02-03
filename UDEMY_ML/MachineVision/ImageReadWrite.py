import numpy as np 
import cv2
import sys
import os.path

srcfname = "/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_1.jpg"
if os.path.isfile(srcfname):
    img = cv2.imread(srcfname)
    cv2.imshow("Original", img)
else:
    raise "No such file exists"
#cv2.imshow("Original", img)

cv2.waitKey(0)

if  not os.path.isdir("/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/"):
    print("No such directory")
else:
    try:
        cv2.imwrite("/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Course_codes_image/Image_1_2.jpg", img)
    except:
        print ("Unexpected error:", sys.exc_info()[0])
        raise
        


# Close all windows
cv2.destroyAllWindows()

