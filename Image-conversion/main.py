from PIL import Image,ImageFilter

import os

nome_da_imagem = input("Coloque aqui o nome da foto + formato do arquivo (Lembre-se, o arquivo deve estar na mesma página!!) ---->>")
image = Image.open(nome_da_imagem)
resize = input("Do you wanna resize your image?(y/n)")
if (resize=='y'):
	width0=input("Please, type the widht in pixels: ")
	width= int(width0)
	height0=input("Please, type the height in pixels: ")
	height= int(height0)
	image.resize((width,height))
else:
	print("OK.")

BlackWhite = input("Black and White Filter?(y/n)")

if (BlackWhite=='y'):
	image.convert(mode='L').save('image_blackandwhite.jpg')

else:
	print("OK.")

Pointers = input("Black and White Filter with pointers?(y/n)")

if (Pointers=='y'):
	image.convert(mode='1').save('image_blackandwhite_pointers.jpg')

else:
	print("OK.")

Blur = input("Blur Filter?(y/n)")

if (Blur=='y'):
	image.filter(ImageFilter.GaussianBlur()).save('image_blur.jpg')

else:
	print("OK.")

Unsharp = input("Unsharp Filter?(y/n)")

if (Unsharp=='y'):
	image.filter(ImageFilter.UnsharpMask()).save('image_unsharp.jpg')
	
else:
	print("OK.")



#image1=Image.open('image0.jpeg').resize((1000,700))#
#blended_image = Image.blend(image,image1,1)#
#blended_image.save('image5.jpeg')#