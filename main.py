from tkinter import *
from turtle import bgcolor
from interface import window

Label(window,text='Anonymous Activated',fg='green').grid(row=1,column=1)

from rough import speak,accdic,wishMe



    
if __name__ == '__main__':
    import os
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    my_label=Label(window,text='Enter Your PassCode',fg='red')
    my_label.grid(row=2,column=1)
    def rem(my_label):
        my_label.config(text=str(l2.cget('text')))
    while True:
        speak('Enter Your PassCode')
        pasc=input('Enter your Passcode :')
        if pasc in accdic:
            a=accdic[pasc]
            j=wishMe(a)
            l2=Label(window,text=j,fg='black')
            l2.grid(row=2,column=1)
            rem(my_label)
            window.destroy()
            window.mainloop() 
        else:
            speak('Access Denied')
            l2=Label(window,text='Access Denied',fg='red',justify='center')
            l2.grid(row=2,column=1)
            rem(my_label)
        
        if(pasc=='an01'):
            import an01
            break
        if(pasc=='an02'):
            import an02  
            break   
      
