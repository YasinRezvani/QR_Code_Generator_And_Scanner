import qrcode

data= input("Enter your data for put to QR Code: ")
img = qrcode.make(data)
path = input("Enter the location to save QR Code(example --> C:/Users/yasin/Documents): ")
name = input("Enter Name for QR Code: ") 
img.save(path +'/'+ name + '.png')

print("-- Your QR Code generated successfully in this Path --> (%s) --" %(path))

# Made By Yasin Rezvani