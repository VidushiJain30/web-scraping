import urllib
import urllib.request
from bs4 import BeautifulSoup

url= "https://twitter.com/BarackObama"
page= urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

print(soup.title.text)
"""
print(soup.findAll('a'))
"""

print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)
i=1
for tweets in soup.findAll('div',{"class":"content"}):
	print(i)
	print(tweets.find('p').text)
	i+=1
