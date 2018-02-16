from bs4 import BeautifulSoup
import glob
import json

path='C:/Users/Pooja/Desktop/lot-parser/data/2015-03-18/*.html'   #path to the folder
files=glob.glob(path)
arr=[]                                                             #initializing empty array to store the objects
new_dict={}                                                         #initializing a new dictionary

for file in files:
    #links = urlopen(file).read()
    links = open(file, 'r')             #opening each file and reading it
    BS=BeautifulSoup(links,"lxml")
    artist=BS.h2.contents[0].strip()                                  #getting the contents of h2 tag for the artist name
    title = BS.title.contents[0].strip()                              #obtainign the title
    new_dict={"artist":artist,"works":title}                           #new dictionary using json object format
    arr.append(new_dict)                                               #array full
    json_obj=json.dumps(arr)                                            #getting the json format from the array
print(json_obj)