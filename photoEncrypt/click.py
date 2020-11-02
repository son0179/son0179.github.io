from tkinter import *
from tkinter import messagebox
 
root = Tk()
 
# 버튼 클릭 이벤트 핸들러
def okClick():
    name = txt.get()
    messagebox.showinfo("이름", name)
    print("hello")
 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
 
# 버튼 클릭 이벤트와 핸들러 정의
btn = Button(root, text="OK", command=okClick)
 
btn.grid(row=1, column=1)
 
root.mainloop()
