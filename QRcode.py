import pyzbar.pyzbar as zbar
#from PIL import Image
#im = Image.open("test.png")
#result = zbar.decode(im)

def Decode(img):
    return zbar.decode(img)
