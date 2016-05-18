import requests
from bs4 import BeautifulSoup
import time

#fw=open("similarweb.txt")
catList = ["facebook.com","bakemycake.in","martopolis.com"]
for j in range (0,3):
	a = "http://www.siteworthtraffic.com/report/"+str(catList[j])
	b = requests.get(a).text
	b = BeautifulSoup(b,"lxml")
	trs = b.find("table", attrs={"class": "styled"}).find_all("tr")
	for tr in trs:
    		tds = tr.find_all("td")
    		if len(tds) < 5:
      			  continue
 	name = tds[1].text
 	name1 = tds[0].text
 	
 	
    	print name
    	print name1
    	
    	



	#c=b.find_all("td",{"id":"titler"})
	#d=b.find("b",{"font"})
	#e=b.find_all("span",{"class":"rankingItem-value js-countable"})

	
#f=b.find_all("tr",{"td":"rankingItem-value js-countable"})

	#print c
	

	#print d
	#print d[1]
	#print e[0].text+"global rank"
	#print e[1].text+"country rank"