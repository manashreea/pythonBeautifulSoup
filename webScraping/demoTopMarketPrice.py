import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html")
soup = BeautifulSoup(page.content,'html.parser')

'''print(soup.prettify())'''

pTop100 = soup.find('p',class_='gL_18 PT15 CTR')

tableMarket = soup.find_all('table',class_='tbldata14')
tableHeadMarket = soup.find_all('th',class_='brdrgtgry')
companyNames = soup.find_all('a',class_='bl_12')
tableRowsMarket = soup.find_all('tr',class_='bggry')

tableHeadings = [hdTable.get_text() for hdTable in tableHeadMarket]
listCompanyName = [compName.get_text() for compName in companyNames]
listCompanyName.pop(0)
listCompanyName.pop(0)
strHeader=''
strDetails=''

fileMarketTop = open("TopCompanyInMarket.txt","w")

for headText in tableHeadings:
    if(strHeader!=''):
        strHeader = strHeader+headText+"|"
    else:
        strHeader = headText+"|"
    
#print(strHeader)
fileMarketTop.write(strHeader+"\n")

for rowData in tableRowsMarket:
    compName = rowData.select('.bl_12')
    otherData = rowData.select('td',attrs={'align':'right'})
    
    compNameData = [data1.get_text() for data1 in compName]
    #print(compNameData)
    
    for data2 in otherData:
        #otherDetails = [data2.get_text() for data2 in otherData]
        if(data2.select('.bl_12')):
            strDetails=strDetails.join(compNameData)+"|"
        else:
            strDataValue=data2.get_text()
            strDetails=strDetails+strDataValue+"|"

    strDetails=strDetails+"\n"
    print(strDetails)
    fileMarketTop.write(strDetails)

fileMarketTop.close()
print("File created successfully >> TopCompanyInMarket.txt")
