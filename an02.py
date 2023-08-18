import webbrowser
from rough import speak,takeCommand,accdic


def wake():
    while True :
        a=accdic['an02']
        query = takeCommand().lower()
        if 'what is my name' in query:
            speak(a)
            print(a)
        elif 'update my name' in query:
            speak('please enter your name')
            a=input("enter your name :")
            up={'an02':a}
            accdic.update(up)
            speak('your name is updated')
            speak('hello!')
            speak(a)
        elif ('who are you'or'your name') in query:
            speak('i am anonymous! i am here to help you')
        elif 'enter some text' in query:
            speak('talk')
            query = takeCommand().upper()
            speak(query)
        elif 'gcd' in query:
            import gcd
        elif 'bmi' in query:
            import BMI
        elif 'close'in query:
            speak('If you want to shutdown!press 1 1 1')
            print('If you want to shutdown!press 111')
            break
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('https://youtube.com')
            break
        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('https://gmail.com')
            break
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('https://google.com')
            break
        elif 'open files' in query:
            path = "D:/HARSHA/"
            speak('opening files')
            webbrowser.open(path)
            break
        elif 'sleep'in query:
            break
        else:
            speak('Command Something')

while True:
    wa=input()
    if(wa!='111'):
        wake()
    else:
        speak('shuttingdown')
        speak('bye!have a nice day')
        print('bye!have a nice day')
        break
