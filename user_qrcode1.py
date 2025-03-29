import qrcode
from PIL import Image 

logo_filename = input("Enter your logo file_name/link here: ")
#Resizing logo to fit in the qr code
mylogo = Image.open(logo_filename)
basewidth = int(input('Enter basewidth: '))  #gives the image base width size. By default it is set to 75.
wpercent = (basewidth / float(mylogo.size[0]))
heightsize = int((float(mylogo.size[1])*float(wpercent)))
mylogo = mylogo.resize((basewidth, heightsize), Image. ANTIALIAS)

#from pypi.org to create a qr code 
qr = qrcode.QRCode(                                          
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=10,
)

#adding link for my qr code 
qr.add_data("https://www.linkedin.com/in/mercy-joshan-58013123b/")
qr.make(fit=True)

img = qr.make_image(fill_color="#0b4e39", back_color="white").convert('RGB')
img_width, img_height = img.size
logo_width, logo_height = mylogo.size 

logo_position = ((img_width - logo_width) // 2, (img_height - logo_height) //2 )

#placing logo at the centre of the qr code 

img.paste(mylogo, logo_position)
img.save("updateimglinkd.png")
img.show()