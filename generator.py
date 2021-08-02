import qrcode

data= input("Enter yout data for put to QR Code: ")
img = qrcode.make(data)
path = input("Enter the location to save QR Code(example --> C:/Usersyasin/Documents): ")
name = input("Enter Name for QR Code: ") 
img.save(path +'/'+ name + '.png')
