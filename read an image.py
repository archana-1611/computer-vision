# Python code to read image
import cv2
img = cv2.imread(r"C:\Users\trasr\OneDrive\Pictures\Screenshots\Screenshot 2025-04-30 140834.png", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
