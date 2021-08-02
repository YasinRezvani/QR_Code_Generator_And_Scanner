import qrcode

data= input("Enter your data for put to QR Code: ")
img = qrcode.make(data)
path = input("Enter the location to save QR Code(example --> C:/Usersyasin/Documents): ")
name = input("Enter Name for QR Code: ") 
img.save(path +'/'+ name + '.png')

# Made By Yasin Rezvani