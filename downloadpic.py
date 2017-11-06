import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
	page= urllib.request.urlopen(url)
	soupdata = BeautifulSoup(page, "html.parser")
	return soupdata
"""
print("Enter the term to be searched")
term= input()
"""

soup = make_soup("https://www.google.co.in/search?tbm=isch&source=hp&biw=811&bih=637&ei=iZUAWvW1Fo60vwTPj4-4Dg&&q=cars&oq=cars")
for img in soup.findAll('img'):
	temp=img.get('src')
	if(temp[:1]=="/"):
		image= "https://uwaterloo.co"+temp
	else:
		image= temp

	nametemp= img.get('alt')
	if len(nametemp)==0:
		filename=str(i)
		i=i+1
	else:
		filename= nametemp

	imagefile= open(filename+".jpeg", 'wb')
	imagefile.write(urllib.request.urlopen(image).read())
	imagefile.close()
