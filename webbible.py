import requests
from bs4 import BeautifulSoup
from rough import speak,engine,rate

speak("Enter the verse:")
verse=input("Enter Book Chapter:verse - ")
con_verse=verse.replace(" ","+")
url="https://www.biblestudytools.com/kjv/genesis/passage/?q="+con_verse
req=requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

box=soup.find("div",class_ ="bible-verses")
speak(verse)
print("King James Version\n")

try:
    verse=box.get_text()
except:
    print("No data found or incorrect data entered")
    speak("No data found or incorrect data entered")
else:
    verse=" ".join(verse.split())
    for ele in verse:
        if ele==".":
            pverse= verse.replace(ele,".\n")
    for ele in verse:
        if ele.isdigit():
            verse= verse.replace(ele,"")
    print(pverse)
    engine.setProperty('rate',160)
    speak(verse)

