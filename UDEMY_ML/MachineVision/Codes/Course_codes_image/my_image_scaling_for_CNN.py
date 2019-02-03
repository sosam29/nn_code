import cv2

# Import Numerical Python package - numpy as np
import numpy as np
import os

# From Operating System(os) to return a list containing names
# of the entries in the directory given by path - os.listdir(path)
from os import listdir
 
# os.path.isfile(path) - Returns True if path is an existing file
from os.path import isfile, join
import send2trash
# Face images for training are taken from human_faces folder
path = '/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Image_processing_projects/Project_5-Real_time_Human_Face_Recognition/human_faces/'
alterpath = '/Users/samuelsonawane/Downloads/UDEMY_ML/MachineVision/Codes/Image_processing_projects/Project_5-Real_time_Human_Face_Recognition/TrainingFaces/'

# Delete everything from dest directory
def delete_directory(path, ext):
    for f in os.listdir(path):
        if f.endswith(ext):
            filename = path+f
            print(filename)
            send2trash.send2trash(filename)

delete_directory(alterpath, "jpg")



def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

listedfiles = listdir_nohidden(path)
filespresent =False
# To filter only files in the specified path we use:
#path_files = [f for f in listdir(path) if isfile(join(path, f))]
path_files = [f for f in listedfiles if isfile(join(path, f))]
index =0 
for f in path_files:
    try:
        index += 1
        read_original = cv2.imread(path+f)
        imgray = cv2.cvtColor(read_original,cv2.COLOR_BGR2GRAY)
        img_inter_area= cv2.resize(imgray, (128, 128), interpolation=cv2.INTER_AREA)
        fname = "resized" + str(index)+".jpg"
        cv2.imwrite(alterpath+fname, img_inter_area)
    except Exception as e:
        print("could not convert image to format due to ", str(e) )
        raise
    
print("resized all!!!")
    
# cv2.imshow("inter area", img_inter_area)

# cv2.waitKey()


# img_inter_linear= cv2.resize(img, None, fx=.5, fy=.5, interpolation=cv2.INTER_LINEAR)

# cv2.imshow("inter Linear", img_inter_linear)

# cv2.waitKey()




# # Close all windows
# cv2.destroyAllWindows()