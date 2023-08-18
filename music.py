import os
import random
from re import T

#n=random.randint(0,321)

directory="D:\HARSHA\MUSIC"
song=os.listdir(directory)
items=len(song)

n=random.randint(0,items)

if '.mp3' in song[n]:
    os.startfile(os.path.join(directory,song[n]))




