def button():
    mylabel = Label(myGui, text = "hi").grid(row = 0, column = 0)
    A = B.get()
    return A

B = StringVar()
C = ""
myentry = Entry(myGui, textvariable = B).grid(row = 1, column = 0)
Submit = Button(myGui, text = "Submit", command = lambda: C=button()).grid(row = 1, column = 1)
