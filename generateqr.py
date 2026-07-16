import qrcode

print("==== QR code generator ====")

data = input("enter url or text : ")

img = qrcode.make(data)

file_name = input("enter file name (without.png): ")

img.save(file_name + ".png")

print("qrcode is successfully generated")
print("file is saved as " +  file_name +".png") 