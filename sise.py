from bs4 import BeautifulSoup # web page analysis
import urllib.request as req

lname=['삼성전자','현대자동차','sk하이닉스']
lStock=['005930','005380','000660'] #삼성전자, 현대자동차, sk하이닉스
i=0
for x in lStock:
    url="https://finance.naver.com/item/sise.naver?code="+x
    res=req.urlopen(url).read().decode('euc-kr')
    soup=BeautifulSoup(res,"html.parser")
    selector=f'#middle > dl > dd:nth-child(5)'
    datastr=soup.select_one(selector)
    print(lname[i],',',datastr)
    i+=1