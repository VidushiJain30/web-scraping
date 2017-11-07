import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import json

def make_soup(url):
	headers= {}
	headers['User-Agent']= "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	req=urllib.request.Request(url, headers=headers)
	page= urllib.request.urlopen(req)
	soupdata = BeautifulSoup(page, "html.parser")
	return soupdata

print("What to search?")
term=input()
#print("https://www.google.co.in/search?q={}&source=lnms&tbm=isch".format(term))
soup = make_soup("https://www.google.co.in/search?q={}&source=lnms&tbm=isch".format(term))
t = soup.find("div", {"class": "rg_meta"})
a = t.get_text()
link, exe= json.loads(a)["ou"], json.loads(a)["ity"]
print(link, exe)
name=json.loads(a)["s"]
i=1
if(len(name)==0):
	filename=str(i)
	i=i+1
else:
	filename=json.loads(a)["s"]

imagefile= open(filename+"."+exe, 'wb')
imagefile.write(urllib.request.urlopen(link).read())
imagefile.close()
#print(a)

#j= json.loads(a)
#ap= j["ou"]

# img= t.find('img')
# source= img.find('src')
#print(a)
