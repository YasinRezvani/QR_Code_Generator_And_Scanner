from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(input("Enter Your location of QR Code(example --> C:/Users/yasin/Documents/yasin.png): "))

res = decode(img)

print(res)

# Made By Yasin Rezvani