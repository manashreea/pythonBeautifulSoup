from bs4 import BeautifulSoup

with open("E:\Manashree_Projects\BeautifulSoup\stylecraft.html") as fp:
    soup = BeautifulSoup(fp,'lxml')
    craftTitle = soup.title
    bodyCraft = soup.body
    paraCrafts = bodyCraft.find_all('p')
    spanCrafts = bodyCraft.find_all('span',class_="views-label views-label-field-brand")
    print(paraCrafts)
    print(spanCrafts,spanCrafts)

