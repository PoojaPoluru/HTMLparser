from bs4 import BeautifulSoup
import glob

path='C:/Users/Pooja/Desktop/lot-parser/data/2015-03-18/*.html'   #path to the folder
files=glob.glob(path)
arr=[] #initializing empty array to store the objects

for file in files:
    #links = urlopen(file).read()
    links = open(file, 'r')             #opening each file and reading it
    BS=BeautifulSoup(links,"lxml")
    artist=BS.h2.contents[0].strip()    #getting the contents of h2 tag for the artist name
    while(artist not in arr):
        arr.append(artist)
print(arr)