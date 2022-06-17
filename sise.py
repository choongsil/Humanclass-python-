from bs4 import BeautifulSoup # web page analysis
import urllib.request as req

lname=['삼성전자','현대자동차','sk하이닉스','엘지에너지솔루션','엘지화학','네이버','삼성SDI']
lStock=['005930','005380','000660', '373220', '051910', '035420', '006400'] #삼성전자, 현대자동차, sk하이닉스
i=0
for x in lStock:
    url="https://finance.naver.com/item/sise.naver?code="+x
    res=req.urlopen(url).read().decode('euc-kr')
    soup=BeautifulSoup(res,"html.parser")
    selector=f'#middle > dl > dd:nth-child(5)'
    datastr=soup.select_one(selector)
    txtstr=datastr.text.split(' ')
    print(lname[i],',',txtstr[1])
    i+=1