import requests
from bs4 import BeautifulSoup
import time


catList = ["facebook.com","google.com","martopolis.com"]
for j in range (0,3):
	a = "https://www.similarweb.com/website/"+str(catList[j])+"#overview"
	b = requests.get(a).text
	b = BeautifulSoup(b,"lxml")
	c=b.find("span",{"class":"engagementInfo-value engagementInfo-value--large u-text-ellipsis"})
	d=b.find_all("span",{"class":"engagementInfo-value u-text-ellipsis"})
	e=b.find_all("span",{"class":"rankingItem-value js-countable"})

	
#f=b.find_all("span",{"class":"rankingItem-value js-countable"})

	print c.text+"visitors"

	print d[0].text+"bounce rate"
	print d[1].text
	print e[0].text+"global rank"
	print e[1].text+"country rank"
	print "************************"