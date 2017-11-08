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
L=[]
#print(soup.findAll("div", {"class": "yf"}))
for t in soup.findAll("div", {"class": "rg_meta"}):
	link, exe=json.loads(t.text)["ou"], json.loads(t.text)["ity"]
	L.append((link, exe))
	i=1
for t in L:
	filename=str(i)
	i=i+1
	imagefile= open(filename+"."+exe, 'wb')
	imagefile.write(urllib.request.urlopen(link).read())
	imagefile.close()
	
