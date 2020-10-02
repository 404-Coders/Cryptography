from tkinter import *
win = Tk()
lb1 = Label(win,text="Enter You Text")
lb1.grid(row=0,column=0,columnspan=2)
value = StringVar()
en1 = Entry(win,textvariable=value)
en1.grid(row=1,columnspan=2)

quertyAlpha01 = ['`','1','2','3','4','5','6','7','8','9','0','-','=']
quertyAlpha02 = ['~','!','@','#','$','%','^','&','*','(',')','_','+']

quertyAlpha11 = ['q','w','e','r','t','y','u','i','o','p',"[",']','\\']
quertyAlpha12 = ['Q','W','E','R','T','Y','U','I','O','P',"{",'}','|']

quertyAlpha21 = ['a','s','d','f','g','h','j','k','l',';',"'"]
quertyAlpha22 = ['A','S','D','F','G','H','J','K','L',':','"']

quertyAlpha31 = ['z','x','c','v','b','n','m',',','.','/']
quertyAlpha32 = ['Z','X','C','V','B','N','M','<','>','?']




# Query - 1 Cipher 
def quertyEncrypt():
    text = value.get()
    enText = ""
    for i in range(len(text)):
        #0
        if str(text[i]) in quertyAlpha01:
            if quertyAlpha01.index(str(text[i]))!=len(quertyAlpha01)-1:
                enText+=quertyAlpha01[quertyAlpha01.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha01[0]
        elif str(text[i]) in quertyAlpha02:
            if quertyAlpha02.index(str(text[i]))!=len(quertyAlpha02)-1:
                enText+=quertyAlpha02[quertyAlpha02.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha02[0]
        #1
        if str(text[i]) in quertyAlpha11:
            if quertyAlpha11.index(str(text[i]))!=len(quertyAlpha11)-1:
                enText+=quertyAlpha11[quertyAlpha11.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha11[0]
        elif str(text[i]) in quertyAlpha12:
            if quertyAlpha12.index(str(text[i]))!=len(quertyAlpha12)-1:
                enText+=quertyAlpha12[quertyAlpha12.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha12[0]
        #2
        if str(text[i]) in quertyAlpha21:
            if quertyAlpha21.index(str(text[i]))!=len(quertyAlpha21)-1:
                enText+=quertyAlpha21[quertyAlpha21.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha21[0]
        elif str(text[i]) in quertyAlpha22:
            if quertyAlpha22.index(str(text[i]))!=len(quertyAlpha22)-1:
                enText+=quertyAlpha22[quertyAlpha22.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha22[0]
        #3
        if str(text[i]) in quertyAlpha31:
            if quertyAlpha31.index(str(text[i]))!=len(quertyAlpha31)-1:
                enText+=quertyAlpha31[quertyAlpha31.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha31[0]
        elif str(text[i]) in quertyAlpha32:
            if quertyAlpha32.index(str(text[i]))!=len(quertyAlpha32)-1:
                enText+=quertyAlpha32[quertyAlpha32.index(str(text[i]))+1]
            else:
                enText+=quertyAlpha32[0]
        if text[i] == ' ':
            enText+=' '
    value.set(enText)

# Query - 1 Cipher 
def quertyDecrypt():
    text = value.get()
    enText = ""
    for i in range(len(text)):
        #0
        if str(text[i]) in quertyAlpha01:
            if quertyAlpha01.index(str(text[i]))!=0:
                enText+=quertyAlpha01[quertyAlpha01.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha01[len(quertyAlpha01)-1]
        elif str(text[i]) in quertyAlpha02:
            if quertyAlpha02.index(str(text[i]))!=0:
                enText+=quertyAlpha02[quertyAlpha02.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha02[len(quertyAlpha02)-1]
        #1
        if str(text[i]) in quertyAlpha11:
            if quertyAlpha11.index(str(text[i]))!=0:
                enText+=quertyAlpha11[quertyAlpha11.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha11[len(quertyAlpha11)-1]
        elif str(text[i]) in quertyAlpha12:
            if quertyAlpha12.index(str(text[i]))!=0:
                enText+=quertyAlpha12[quertyAlpha12.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha12[len(quertyAlpha12)-1]
        #2
        if str(text[i]) in quertyAlpha21:
            if quertyAlpha21.index(str(text[i]))!=0:
                enText+=quertyAlpha21[quertyAlpha21.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha21[len(quertyAlpha21)-1]
        elif str(text[i]) in quertyAlpha22:
            if quertyAlpha22.index(str(text[i]))!=0:
                enText+=quertyAlpha22[quertyAlpha22.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha22[len(quertyAlpha22)-1]
        #3
        if str(text[i]) in quertyAlpha31:
            if quertyAlpha31.index(str(text[i]))!=0:
                enText+=quertyAlpha31[quertyAlpha31.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha31[len(quertyAlpha31)-1]
        elif str(text[i]) in quertyAlpha32:
            if quertyAlpha32.index(str(text[i]))!=0:
                enText+=quertyAlpha32[quertyAlpha32.index(str(text[i]))-1]
            else:
                enText+=quertyAlpha32[len(quertyAlpha32)-1]
        if text[i] == ' ':
            enText+=' '
    value.set(enText)        


btn = Button(win,text="Encrypt",command=quertyEncrypt)
btn.grid(row=2,column=0)

btn2 = Button(win,text="Decrypt",command=quertyDecrypt)
btn2.grid(row=2,column=1)
win.mainloop()

