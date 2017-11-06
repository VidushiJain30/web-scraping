import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
	page= urllib.request.urlopen(url)
	soupdata= BeautifulSoup(page, "html.parser")
	return soupdata

playerdatasaved=""
soup= make_soup("https://www.basketball-reference.com/players/a/")
for record in soup.findAll('tbody'):
	playerdata=""
	for data in record.findAll('tr'):
		playerdata=playerdata+"\n,"+data.text
	playerdatasaved= playerdatasaved+ "\n" +"\t"+playerdata[1:]+"\n"+"\n"
print(playerdatasaved)
