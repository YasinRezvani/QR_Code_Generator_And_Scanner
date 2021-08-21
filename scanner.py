from pyzbar.pyzbar import decode
from PIL import Image

print("------------------------------------------------------")

img = Image.open(input("\nEnter Your location of QR Code(example --> C:/Users/yasin/Documents/yasin.png): "))

res = decode(img)

print("\n")
print(res)
print("\n")

print("------------------------------------------------------")

input()

# Made By Yasin Rezvani