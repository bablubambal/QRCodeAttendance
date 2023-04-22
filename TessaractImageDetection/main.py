import cv2
import pytesseract

img = cv2.imread('imag.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
h, w, c = img.shape
text = pytesseract.image_to_string(img)
boxes = pytesseract.image_to_boxes(img) 
data = pytesseract.image_to_data(img)
# print(data)
# for d in data.splitlines("\n"):
#     print(d)
# print(boxes)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('imag', img)
cv2.waitKey(0)
print(text)