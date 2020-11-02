from PIL import Image as image
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
Password = 0

root = Tk()

def __name():
    a=3;
    

def PhotoBinarization(photoDir):
    im = image.open(photoDir)
    pixel = im.load()
    x,y = im.size

    for i in range(x):
        for j in range(y):
            tmp=0
            R,G,B = pixel[i,j]
            tmp |= R << (8 * 2)
            tmp |= G << (8 * 1)
            tmp |= B << (8 * 0)
            tmp ^= Password
            tmp ^= Password 
            encryptedR = 255 & (tmp >> (8 * 2))
            encryptedG = 255 & (tmp >> 8 )
            encryptedB = 255 & tmp
            pixel[i,j] = (encryptedR , encryptedG , encryptedB)
    im.save(photoDir[:-4]+"_encryped.png")
    
          


def IsPSBClicked():
    name = txt.get()
    photoDir = filedialog.askopenfile(initialdir='path', title='사진을 선택하세요', filetypes=(('JPEG files', '*.jpg') , ('PNG files', '*.png'), ('ALL files', '*.*')))

    if photoDir !="None" :
        name = txt.get()
        messagebox.showinfo("", "사진을 로드했습니다.")
        PhotoBinarization(photoDir.name)
    
    


lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)

txt = Entry(root)
txt.grid(row=0, column=1)

PhotoSelctButton = Button(root, text = "사진을 선택하세요" , command = IsPSBClicked)
print(type(PhotoSelctButton.command))
PhotoSelctButton.grid(row=1, column=1)

root.mainloop()
