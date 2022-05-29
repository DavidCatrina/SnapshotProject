# Importing Image and ImageGrab module from PIL package
from PIL import Image, ImageGrab
# Import webbrowser
import webbrowser

# using the grab method
im2 = ImageGrab.grab(bbox =(200, 400, 800, 900))

#show the image
im2.show()

#crete a list with pixels RGB
p=im2.getcolors(maxcolors=100000)

#print the list of the 300 000 pixels
#print(p)
#Print how many different pixels are there
#print(len(p))

if len(p) == 1:
    print ("Sleep well!")
elif len(p) > 1:
    print("Case available!")
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ')  # Go to example.com




def autoClicker(x,y):
    mouse.move(100, 100, absolute=False, duration=0.2)

























# if (p == checker)
#     print ("Sleep well baby!")
# else
#     print ("Case available!")
    







 