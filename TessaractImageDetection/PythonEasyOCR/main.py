import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import re

#gst regex
regex = "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$"
 # Compile the ReGex
p = re.compile(regex)

def isValidMasterCardNo(str):

	# Regex to check valid
	# GST (Goods and Services Tax) number
	regex = "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$"
	
	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty
	# return false
	if (str == None):
		return False

	# Return if the string
	# matched the ReGex
	if(re.search(p, str)):
		return True
	else:
		return False


# read image
image_path = 'data/4.jpg'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    # print(t)

    bbox, text, score = t
    print(text)

    if score > threshold:
	    # print(score)
	    cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        # cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
	    # print(isValidMasterCardNo(text))
        # if(isValidMasterCardNo(text)):
        #     print(text)
	    
        # print(text.find('BILL NO.'))
        # print(text.find('DATE'))
        # print(re.search(p, text))
        # print(text.find('Bill No'))
        # cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        # cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
