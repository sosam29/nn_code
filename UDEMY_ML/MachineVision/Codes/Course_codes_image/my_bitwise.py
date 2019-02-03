import cv2
import numpy as np 


#Circle drawing
rect = np.zeros((200, 200), np.uint8 )

rectangle = cv2.rectangle( rect, (20,20),(180, 180), 255, -1)

cv2.imshow("Rectangle", rectangle)

cv2.waitKey()

#Circle drawing
cir = np.zeros((200, 200), np.uint8)

circle = cv2.circle(cir, (100, 100), 100, 255, -1)

cv2.imshow("Circle", circle)
cv2.waitKey()

# bit AND operatioins
And = cv2.bitwise_and( circle, rectangle)
cv2.imshow("Anded", And)
cv2.waitKey()


# bit OR operatioins
OR = cv2.bitwise_or( circle, rectangle)
cv2.imshow("ORR", OR)
cv2.waitKey()

# bit OR operatioins
XOR = cv2.bitwise_xor( circle, rectangle)
cv2.imshow("XRR", XOR)
cv2.waitKey()

#
XORR = cv2.bitwise_xor( rectangle, circle)
cv2.imshow("XRRO", XORR)
cv2.waitKey()
 #bit nor operatioins
XNOR= cv2.bitwise_not( circle, rectangle)
cv2.imshow("XNOR", XNOR)
cv2.waitKey()

 #bit nor operatioins
NOTEXOR= cv2.bitwise_not( rectangle ,circle)
cv2.imshow("NOTEXOR", NOTEXOR)
cv2.waitKey()

cv2.destroyAllWindows()