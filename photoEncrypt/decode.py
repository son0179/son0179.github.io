from PIL import Image as image
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
password = 0

root = Tk()                         # GUI 생성
root.title("Photo En/Decrypter")    # 창의 제목 옵션
root.geometry("320x200")            # 창의 크기


def PhotoBinarization(photoDir, password): # 핵심함수 시프트연산
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
            tmp ^= int(password) 
            encryptedR = 255 & (tmp >> (8 * 2))
            encryptedG = 255 & (tmp >> 8 )
            encryptedB = 255 & tmp
            pixel[i,j] = (encryptedR , encryptedG , encryptedB)
    im.save(photoDir[:-4]+"_encryped.png")
    messagebox.showinfo("", "선택한 사진이 암호/복호화 되었습니다.")

def GetPassword(event):
    messagebox.showinfo("", "비밀번호가 등록됬습니다.")
    global password
    password = Entry.get(inputPassword)


def IsPSBClicked():
    
    photoData = filedialog.askopenfile(initialdir='path', title='사진을 선택하세요', filetypes=(('JPEG files', '*.jpg') , ('PNG files', '*.png'), ('ALL files', '*.*')))

    if photoData !=None :
            
        messagebox.showinfo("", "사진을 로드했습니다.")
        global photoDir
        photoDir = photoData.name
        



PhotoSelctButton = Button(root, text = "1.사진을 선택하세요" , command = IsPSBClicked)   # 버튼생성 버튼 클릭시 IsPSBClicked 함수 실행
PhotoSelctButton.grid(column=0, row=0, ipadx=5, pady=5,)                                 # 버튼을 화면 0,0에 배치

notice = Label(root , text ="↓ input password and Press Enter ")                        # 라벨(단순 txt) 생성
notice.grid(column=0,row=1,ipadx=20, pady=5 )                                            # 라벨을 0,0 에 배치

inputPassword = Entry(root,width=24)                                                     # 엔트리(입력칸) 생성
inputPassword.grid(column=0, row=2, ipadx=5, pady=5 )                                    
inputPassword.bind('<Return>', GetPassword)                                              # enterket 가 트리거로 GetPassword 함수 실행

photoDir="C:/"

EncryptButton = Button(root, text = "2.위 칸에 암호(24 자리 이진수 행렬)를 입력하세요" , command =lambda :PhotoBinarization(photoDir, password))
EncryptButton.grid(column=0, row=3, ipadx=5, pady=5)


root.mainloop()
