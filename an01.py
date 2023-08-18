from datetime import datetime
from logging import exception
import os
from time import strftime
from tkinter import *
import webbrowser,pyttsx3,wikipedia
import pywhatkit
from googlesearch import search
from rough import speak,takeCommand,accdic
from ui import tk,win

a=accdic['an01']


l1=tk.Label(win,text='',fg='darkgreen')
l1.grid(row=2,column=4)

def sw(l1,l2):
    l1.config(text=str(l2.cget('text')))
    l1.place(anchor='center', relx=0.5, rely=0.5)
def wake(a):
    
    while True:
        query = takeCommand().lower()
        if 'what is my name' in query:
            speak(a)
            print(a)
            l2=tk.Label(win,text=a,fg='blue')
            sw(l1,l2)
            break
        elif 'update my name' in query:
            speak('please enter your name')
            a=input("enter your name :")
            up={'an01':a}
            accdic.update(up)
            speak('your name is updated')
            l2=Label(win,text=a,fg='blue')
            sw(l1,l2)
            speak('hello!')
            speak(a)
            break
        elif ('who are you') in query:
            bun='i am anonymous! i am here to help you'
            speak(bun)
            l2=tk.Label(win,text=bun,fg='blue')
            sw(l1,l2)
            break
        elif 'speech to text' in query:
            speak('talk')
            query = takeCommand().lower()
            speak(query)
            print(query)
            l2=tk.Label(win,text=query,fg='blue')
            sw(l1,l2)
            break
        elif 'gcd' in query:
            import gcd
        elif 'bmi' in query:
            import BMI
        elif 'turn off' in query :
            speak('If you want to shutdown the computer press 000')
            l2=Label(win,text='press 000 to Turnoff PC',fg='blue')
            sw(l1,l2)
            break
        elif 'bible' in query :
            import webbible
            break
        elif 'time' in query:
            cmd=datetime.now().strftime('%I:%M  %p')
            print(cmd)
            speak('Current time is' + cmd)
            l2=tk.Label(win,text=cmd,fg='blue')
            sw(l1,l2)
            break
        elif 'change voice' in query:
            engine=pyttsx3.init()
            voices = engine.getProperty('voices')
            speak('0 for male!1 for female')
            cv=int(input('0 for male, 1 for female :'))
            if(cv==0):
                engine.setProperty('voice',voices[0].id)
            elif(cv==1):
                engine.setProperty('voice',voices[1].id)
            speak('hi! i am anonymous')       
        elif 'close'in query:
            bun='If you want to abort, press 111'
            speak('If you want to abort!press 1 1 1')
            print('If you want to abort, press 111')
            l2=tk.Label(win,text=bun,fg='blue')
            sw(l1,l2)
            break
        elif 'playlist' in query:
            speak('Playing your playlist')
            print('Playing your playlist')
            l2=Label(win,text='Playing your playlist',fg='blue')
            sw(l1,l2)
            import music
            break
        elif 'play' in query:
            song=query.replace('play','')
            speak('playing'+ song)
            l2=tk.Label(win,text='playing'+song,fg='blue')
            sw(l1,l2)
            pywhatkit.playonyt(song)
            break
        elif 'send message' in query:

            contact={"sathwik":'"+917032684989"',"keerthi":'"+917013845006"',"sandeep":'"+918179331245"',"praveen":"'+919391485863'","phani":"'+917842881666'"}
            
            speak("Here is your contact list:")
            print(contact.keys())
            speak("Choose contact")
            person=input("Choose Contact:")
            if person.lower() in contact :
                speak("Enter message")
                msg=takeCommand().lower()
                
                if msg!="" and msg!="none":
                    speak('sending message to'+ person.lower())
                    l2=tk.Label(win,text='sending message to '+person.lower(),fg='blue')
                    sw(l1,l2)
                    pywhatkit.sendwhatmsg_instantly(contact[person.lower()],msg,10,True, 4)
                else:
                    speak("Message not sent.Message is empty")
                    print("Message not sent.Message is empty")
                break
            else:
                speak("Contact not found")
                print("Contact not found")
                l2=tk.Label(win,text="Contact not found",fg='blue')
            break
        
        elif 'spotify' in query:
            speak('opening spotify')
            l2=tk.Label(win,text='opening spotify',fg='blue')
            sw(l1,l2)
            os.system('spotify.exe')
            break
        elif 'open whatsapp' in query:
            speak('opening whatsapp')
            l2=tk.Label(win,text='opening whatsapp',fg='blue')
            sw(l1,l2)
            webbrowser.open('https://web.whatsapp.com/')
            break
        elif 'open files' in query:
            path = "D:/HARSHA/"
            speak('opening files')
            l2=tk.Label(win,text='opening files',fg='blue')
            sw(l1,l2)
            webbrowser.open(path)
            break
        elif 'open' in query:
            app=query.replace('open ','')
            speak('opening'+app)
            l2=tk.Label(win,text='opening'+app,fg='blue')
            sw(l1,l2)
            app="https://"+app+'.com'
            webbrowser.open(app)
            break
        elif 'open google' in query:
            speak('opening google')
            l2=tk.Label(win,text='opening Google',fg='blue')
            sw(l1,l2)
            webbrowser.open('https://google.com')
            break
        elif ('silent'or 'calm'or 'sleep') in query:
            speak('sleeping')

            l2=tk.Label(win,text='Sleeping',fg='blue')
            sw(l1,l2)
            speak('Press enter to wakeup')
            break
        elif ('who'or'what'or'how'or'why') in query:
            query=query.replace('anonymous ','')
            info=wikipedia.summary(query,1)
            l2=tk.Label(win,text=info,fg='blue')
            sw(l1,l2)
            print(info)
            speak(info) 
            break       
        else:
            speak('speak something')
            print('.......')
                

while True:
    wa=input()
    if(wa=='000'):
        speak('turning off the computer')
        os.system("shutdown /s /t 30")
        win.destroy()
        break
    elif(wa!='111' and wa!='000'):
         wake(a)
    else:
        speak('Program Aborted')
        speak('bye!have a nice day')
        print('bye!have a nice day')
        win.destroy()
        break
win.mainloop()  
  
