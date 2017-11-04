import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
	page= urllib.request.urlopen(url)
	soupdata= BeautifulSoup(page, "html.parser")
	return soupdata

playerdatasaved=""
soup= make_soup("https://www.basketball-reference.com/players/a/")
for record in soup.findAll('tr'):
	playerdata=""
	for data in record.findAll('td'):
		playerdata=playerdata+","+data.text
	playerdatasaved= playerdatasaved+ "\n" +playerdata[1:]
print(playerdatasaved)