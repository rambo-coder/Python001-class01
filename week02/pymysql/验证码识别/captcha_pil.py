
# 先安装依赖库libpng, jpeg, libtiff, leptonica
# brew install leptonica
# 安装tesseract
# brew install  tesseract
# 与python对接需要安装的包
# pip3 install Pillow
# pip3 install pytesseract

import requests
import os
from PIL import Image
import pytesseract

im = Image.open('cap.jpg')
im.show()

gray = im.convert('L')
gray.save('c_gray2.jpg')
im.close()

threshold = 100
table = []

for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table,'1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


print(pytesseract.image_to_string(th,lang='eng'))