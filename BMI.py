from rough import speak,accdic


print("BMI : Body Mass Index\n")
print("Press 1 : Height in feet and inches")
print("press 2 : Height in meters")
print("press 3 : Height in centimeters\n")

def bmi(w,m):
    BMI=(w/(m*m))
    print('\nBMI =',BMI)
    if(BMI<18.5):
        g=21.8-BMI
        we=g*m*m
        print('\nUnderweight\n','you should gain',we,'kgs to maintain normal weight')
        speak('Underweight! you should gain')
        speak(we)
        speak('kilograms to maintain normal weight')
    elif(BMI>=18.5 and BMI<=24.9):
        print('Normal Weight')
        speak('normal weight')
    elif(BMI>=25.0 and BMI<=29.9):
        l=BMI-24.9
        we=l*m*m
        print('\nOverweight\n','you should loss',we,'kgs to maintain normal weight')
        speak('Overweight! you should loss')
        speak(we)
        speak('kilograms to maintain normal weight')
    else:
        l=BMI-24.9
        we=l*m*m
        print('\nObesity\n','you should loss',we,'kgs to maintain normal weight')
        speak('Obesity! you should loss')
        speak(we)
        speak('kilograms to maintain normal weight')
z=int(input('Enter choice:'))
if z==1:
    f=float(input('\nEnter Feet:'))
    if(f>=1.5 and f<=9.0):
        i=int(input('Enter Inches:'))
        if i<=12:
            w=int(input('Enter Weight in kgs:'))
            if(w>=2.5 and w<=635):
                m=(f*0.305)+(i*0.0254)
                bmi(w,m)
            else:
                print("Invalid weight entered")
        else:
            print("Invalid inches entered")
    else:
        print("Invalid feet entered")
elif z==2:
    m=float(input('\nEnter height in meters:'))
    if(m>=0.457 and m<=2.7432):
         w=int(input('Enter Weight in kgs:'))
         if(w>=2.5 and w<=635):
             bmi(w,m)
         else:
             print("Invalid weight entered")
    else:
        print("Invalid height entered")
   
elif z==3:
    cm=float(input('\nEnter height in centimeters:'))
    if(cm>=45.72 and cm<=274.32):
            w=int(input('Enter Weight in kgs:'))
            if(w>=2.5 and w<=635):
                m=cm*0.01
                bmi(w,m)
            else:
                print("Invalid weight entered")
    else:
        print("Invalid height entered")
                

else:
    print('\n\t\tWRONG ENTRY...')

