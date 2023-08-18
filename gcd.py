from rough import speak

speak("calaculating GCD")

m=int(input("Enter m :"))
n=int(input("Enter n :"))
    
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if(m%i==0) and (n%i==0):
            mrcf=i
    return mrcf
k=gcd(m,n)
print("The GCD of",m,"and",n,"is",k)
speak("The GCD is")
speak(k)

