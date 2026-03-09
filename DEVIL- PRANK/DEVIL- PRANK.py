import tkinter 
from PIL import Image, ImageTk
import random 

root = tkinter.Tk() # create main window
root.attributes('-fullscreen', True)  # set fullscreen mode
root.attributes('-topmost', True) # keep window on top stricly
root.attributes('-transparentcolor', 'black') # set transparent color
widht = root.winfo_screenwidth() # get screen width
height = root.winfo_screenheight() # get screen height
canvas = tkinter.Canvas(root, width=widht, height=height, bg='black',
                        highlightbackground='black') # create canvas for set image
canvas.pack() # add canvas to the window
img = Image.open('pngimg.com - devil_PNG17.png.') # devil image stored in img variable
img2 = Image.open('pngegg.png') # pyramid image stored in in img2 variable
spiger_img = ImageTk.PhotoImage(img) # load image
# add image to canvas
def add_spider():
    x = random.randint(0, widht) # random x position
    y = random.randint(0, height) # random y position
    canvas.create_image(x, y, image = spiger_img) 
    root.after(500, add_spider) # call this function again after 500 ms

root.protocol('WM_DELETE_WINDOW', lambda: None) # disable window close button
add_spider()
root.mainloop() # start the GUI event loop

