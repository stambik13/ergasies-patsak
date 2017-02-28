import urllib
import BeautifulSoup
kwords=raw_input("dose tis lexeis kleidia: ")
kwords=kwords.split(",")	
br1=urllib.urlopen("http://www.brewerydb.com/style/88")
beer1=BeautifulSoup(br1.read(),"html.parser")
for i in beer1.find_all("class":"description"):
	d1=i.get_text()
	for j in keywords:
		if (beer1[i]==keywords[j]):
			mx1=mx1+1
br2=urllib.urlopen("http://www.brewerydb.com/style/62")
beer2=BeautifulSoup(br2.read(),"html.parser")
for i in beer2.find_all("class":"description"):
	d2=i.get_text()
	for j in keywords:
		if (beer2[i]==keywords[j]):
			mx2=mx2+1
br3=urllib.urlopen("http://www.brewerydb.com/style/119")
beer3=BeautifulSoup(br1.read(),"html.parser")
for i in beer3.find_all("class":"description"):
	d3=i.get_text()
	for j in keywords:
	    if (beer3[i]==keywords[j]):
		    mx3=mx3+1
br4=urllib.urlopen("http://www.brewerydb.com/style/15")
beer4=BeautifulSoup(br1.read(),"html.parser")
for i in beer4.find_all("class":"description"):
    d4=i.get_text()
    for j in keywords:
	    if (beer4[i]==keywords[j]):
		    mx4=mx4+1
br5=urllib.urlopen("http://www.brewerydb.com/style/47")
beer5=BeautifulSoup(br1.read(),"html.parser")
for i in beer5.find_all("class":"description"):
    d5=i.get_text()
    for j in keywords:
	    if (beer5[i]==keywords[j]):
		    mx5=mx5+1
br6=urllib.urlopen("http://www.brewerydb.com/style/149")
beer6=BeautifulSoup(br1.read(),"html.parser")
for i in beer6.find_all("class":"description"):
    d6=i.get_text()
    for j in keywords:
	    if (beer6[i]==keywords[j]):
		    mx6=mx6+1
br7=urllib.urlopen("http://www.brewerydb.com/style/38")
beer7=BeautifulSoup(br1.read(),"html.parser")
for i in beer7.find_all("class":"description"):
	d7=i.get_text()
    for j in keywords:
	    if (beer7[i]==keywords[j]):
		    mx7=mx7+1
br8=urllib.urlopen("http://www.brewerydb.com/style/97")
beer8=BeautifulSoup(br1.read(),"html.parser")
for i in beer8.find_all("class":"description"):
    d8=i.get_text()
    for j in keywords:
	    if (beer8[i]==keywords[j]):
		    mx8=mx8+1
br9=urllib.urlopen("http://www.brewerydb.com/style/106")
beer9=BeautifulSoup(br1.read(),"html.parser")
for i in beer9.find_all("class":"description"):
    d9=i.get_text()
    for j in keywords:
	    if (beer9[i]==keywords[j]):
		    mx9=mx9+1
if (mx1>mx2 and mx1>mx3 and mx1>mx4 and mx1>mx5 and mx1>mx6 and mx1>mx7 and mx1>mx8 and mx1>mx9):
	print Traditional German-Style Bock
if (mx2>mx1 and mx2>mx3 and mx2>mx4 and mx2>mx5 and mx2>mx6 and mx2>mx7 and mx2>mx8 and mx2>mx9):
	print Belgian-Style Pale Ale
if (mx3>mx1 and mx3>mx2 and mx3>mx4 and mx3>mx5 and mx3>mx6 and mx3>mx7 and mx3>mx8 and mx3>mx9):
	print Fruit Beer
if (mx4>mx1 and mx4>mx2 and mx4>mx3 and mx4>mx5 and mx4>mx6 and mx4>mx7 and mx4>mx8 and mx4>mx9):
	print Scotch Ale
if (mx5>mx1 and mx5>mx2 and mx5>mx3 and mx5>mx4 and mx5>mx6 and mx5>mx7 and mx5>mx8 and mx5>mx9):
	print Leipzig-Style Gose
if (mx6>mx1 and mx6>mx2 and mx6>mx3 and mx6>mx4 and mx6>mx5 and mx6>mx7 and mx6>mx8 and mx6>mx9):
	print Common Cider
if (mx7>mx1 and mx7>mx2 and mx7>mx3 and mx7>mx4 and mx7>mx5 and mx7>mx6 and mx7>mx8 and mx7>mx9):
	print Smoke Porter
if (mx8>mx1 and mx8>mx2 and mx8>mx3 and mx8>mx4 and mx8>mx5 and mx8>mx6 and mx8>mx7 and mx8>mx9):
	print American-Style Premium Lager
if (mx9>mx1 and mx9>mx2 and mx9>mx4 and mx9>mx5 and mx9>mx6 and mx9>mx7 and mx9>mx8 and mx9>mx3):
	print International-Syle Pilsener 
