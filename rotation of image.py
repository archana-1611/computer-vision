import cv2
image=cv2.imread(r"C:\Users\trasr\OneDrive\Desktop\COMPUTER VISION\mountain.jpg")
clockwise=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
counter=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("clockwise",clockwise)
cv2.imshow("counter clockwise",counter)
cv2.waitKey(0)
cv2.destroyAllWindows()
