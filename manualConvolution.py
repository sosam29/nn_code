import numpy as np 
import cv2
from skimage.exposure import rescale_intensity

def convolve(image, K):
    (iH, iW)= image.shape[:2] # image dimesion
    (kH, kW)= K.shape[:2]  # kernel Dim

    pad = (kW -1 )//2   # using padding to keep image size intact
    image = cv2.copyMakeBorder(image, pad, pad,pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype='float')

    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad , iW + pad):
            roi= image[y-pad:y+pad+1, x-pad:x+pad+1]
            k = (roi * K).sum()
            output[y-pad, x-pad]=k
        output = rescale_intensity(output, in_range=(0, 255))
        output = (output * 255).astype("uint8")
        return output

smallblur = np.ones((7,7), dtype='float')*(1.0/(7*7))
bigblur = np.ones((21, 21), dtype='float')*(1.0/(21*21))

sharpen = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), dtype='int')
laplacean = np.array(([0,1,0],[1,-4,1],[0,1,0]), dtype='int')
sobelX = np.array(([-1,0,1],[-2,0,2],[-1,0,1]), dtype='int')
sobelY = np.array(([-1,-2,-1],[0,0,0],[1,2,1]), dtype='int')
emboss = np.array(([-2,-1,0],[-1,1,1],[0,1,2]), dtype='int')

kerenelBank = (("smallblue", smallblur),("bigblur", bigblur),("sharpen", sharpen),("laplacean", laplacean),("sobel_x", sobelX),("sobel_y", sobelY), ("emboss", emboss))

image = cv2.imread(r"C:\\Users\\Sam\\Downloads\\dlib\\examples\\johns\\John_Schneider\\000325_00925954.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for (kernelName, K) in kerenelBank:
    convolveOutput = convolve(gray, K)
    opencvOutput = cv2.filter2D(gray, -1, K)

    cv2.imshow("Original", image)
    cv2.imshow("{} - convolve".format(kernelName), convolveOutput)
    cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



