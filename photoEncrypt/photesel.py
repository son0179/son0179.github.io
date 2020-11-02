from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.dirName=filedialog.askopenfile(initialdir='path', title='사진을 선택하세요', filetypes=(('JPEG files', '*.jpg') , ('PNG files', '*.png'), ('ALL files', '*.*')))
 
print (root.dirName);

