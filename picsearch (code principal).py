#by code.sleep
#merci d'installé les 3 module ci desssous
# ci vous voulez plus de temps, dans la ligne 44 je vous fait attandre 3 seconde vous pouvez teleharge les version fast ou supprimer le module time et la ligne.merci
import cv2
import pytesseract
import time

print ("by debug my best friends")

imageinput = input("enter picture, please")

print("please wait !")


google = "https://www.google.com/search?q="

img = cv2.imread(imageinput)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,

cv2.CHAIN_APPROX_NONE)
 

im2 = img.copy()
 
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    file = open("recognized.txt", "a")
    text = pytesseract.image_to_string(cropped)

if ' ' in text:
    text.replace(" ", "+")

finaltext = google + text

print (text)

time.sleep (3)
print (finaltext)

print ("ps: is pic-search, and is he thank you")
