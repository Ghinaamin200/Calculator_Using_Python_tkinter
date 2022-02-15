from tkinter import *
from tkinter import font

def click(event):
    global calculation
    text = event.widget.cget("text")
    if text == "=":
        if calculation.get().isdigit():
            value = int(calculation.get())
        else:
            value= eval(outputs.get())

        calculation.set(value)
        outputs.update()
    elif text == "C":
        calculation.set("")
        outputs.update()
    else:
        calculation.set(calculation.get()+ text)
        outputs.update()
root = Tk()
root.title("Calculator")
root.wm_iconbitmap("C:\\Users\\ghina\\Desktop\\python\\calculator\\calculator.ico")
root.geometry("450x480")
root.maxsize(450,480)
root.minsize(450,480)

calculation = StringVar()
f1 = Frame(root,bg ="grey")
b1 = Button(f1,text = "C",font= "lucida 27 bold",bg = "black",fg = "white")
b1.bind("<Button-1>",click)
b1.pack(side = LEFT,padx=5,pady =10,ipadx=5)
outputs = Entry(f1, textvar=calculation, font="lucida 45 bold")
outputs .pack(fill=X, ipadx=10, pady=10, padx=5)
f1.pack(fill = X,padx=20)
operators = ["/","*","+","-"]
number = ["9","8","7","6","5","4","3","2","1","0",".","="]
x=0
f = Frame(root,bg ="grey",relief =RIDGE)
for i in range (0,4,1):
    if i%3==0 and i !=0:
        b =Button(f,text= f"{operators[0]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=10,pady =10,ipadx=15,fill = X)
    else:
        b =Button(f,text= f"{number[x]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=15,ipadx=15,fill = X)
        x=x+1
f.pack(anchor = "w",padx=10 ,fill=X)

f = Frame(root,bg ="grey",relief =RIDGE)
for i in range (0,4,1):
    if i%3==0 and i !=0:
        b =Button(f,text= f"{operators[1]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=10,pady =10,ipadx=15,fill = X)
    else:
        b =Button(f,text= f"{number[x]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=15,ipadx=15,fill = X)
        x=x+1
f.pack(anchor = "w",padx=10 ,fill=X)

f = Frame(root,bg ="grey",relief =RIDGE)
for i in range (0,4,1):
    if i%3==0 and i !=0:
        b =Button(f,text= f"{operators[2]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=10,pady =10,ipadx=15,fill = X)
    else:
        b =Button(f,text= f"{number[x]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=15,ipadx=15,fill = X)
        x=x+1
f.pack(anchor = "w",padx=10 ,fill=X)

f = Frame(root,bg ="grey",relief =RIDGE)
for i in range (0,4,1):
    if i%3==0 and i !=0:
        b =Button(f,text= f"{operators[3]}",font= "lucida 26 bold",bg = "black",fg = "white")
        b.bind("<Button-1>",click)
        b.pack(side = LEFT,padx=10,pady =10,ipadx=15,fill = X)
    else:
        if number[x] == ".":
            b =Button(f,text= f"{number[x]}",font= "lucida 26 bold",bg = "black",fg = "white")
            b.bind("<Button-1>",click)
            b.pack(side = LEFT,padx=15,ipadx=19,fill = X)
            x=x+1
        else:
            b =Button(f,text= f"{number[x]}",font= "lucida 26 bold",bg = "black",fg = "white")
            b.bind("<Button-1>",click)
            b.pack(side = LEFT,padx=15,ipadx=15,fill = X)
            x=x+1
f.pack(anchor = "w",padx=10 ,fill=X)


root.configure(background="grey")
root.mainloop()