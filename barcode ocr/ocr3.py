import os, io
import json
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision_v1 import types
import cv2
from PIL import Image

# Instantiates a client
client = vision.ImageAnnotatorClient()

def detect_text():
    
    
    image = cv2.imread('images/meds.jpg')
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    image2 = cv2.imread('images/notgood.jpg')

    y=500
    x=0
    h=200
    w=1300

    crop_img = image[y:y+h, x:x+w]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)

    cv2.imwrite("wash5.jpg",crop_img)

    crop_img2 = image[y:y+h, x:x+w]


    """Detects text in the file."""
    with io.open('wash5.jpg', 'rb') as image_file:
        content = image_file.read()
        
 		
    image = types.Image(content=content)
    
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
        
    string = string.replace(" ", "")
    string = string.replace('"', "")
    string = string.split("\n")
    print(string[0])
    return string[0]
    
    
detect_text()


try: 
    os.remove("wash5.jpg")
except: pass




