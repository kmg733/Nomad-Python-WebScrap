# 알바천국 웹 크롤링
import os
import csv
import time
# requests 라이브러리는 파이썬에서 요청을 만드는 기능을 모아 놓은 라이브러리
import requests
# html에서 데이터를 추출하는 라이브러리
from bs4 import BeautifulSoup

os.system("cls")
alba_url = "http://www.alba.co.kr"

# 알바천국의 슈퍼브랜드 채용정보 링크를 긁어온다.
def getSuperBrandHrefs():
    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text, "html.parser") 
    
    superBrand = soup.find("div", {"id": "MainSuperBrand"})
    snUl = superBrand.find("ul", {"class": "goodsBox"})
    snAnchor = snUl.find_all("a", {"class": "goodsBox-info"})

    hrefs = []
    companys = []
    for href in snAnchor:
        hrefs.append(href.get("href"))
        companys.append(href.find("span", {"class": "company"}).get_text())
    return companys, hrefs

def extractInfo(url):
    # place
    tdPlace = url.find("td", {"class": "local"}).get_text()
    # \xa0 제거
    tdPlace = tdPlace.replace(u'\xa0', u' ')      

    # title
    tdTitle = url.find("span", {"class": "title"}).get_text()

    # time
    tdTime = url.find("td", {"class": "data"}).get_text()

    # pay
    tdPay = url.find("td", {"class": "pay"})
    payHangul = tdPay.find("span", {"class": "payIcon"}).get_text()
    payInt = tdPay.find("span", {"class": "number"}).get_text()
    payResult = ",".join([payHangul, payInt])

    # date
    tdDate = url.find("td", {"class": "regDate last"}).get_text() 

    return {
        "place": tdPlace,
        "title": tdTitle,
        "time": tdTime,
        "pay": payResult,
        "date": tdDate
    }

def extractInfos(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    # 일반 채용정보
    normalInfo = soup.find("div", {"id": "NormalInfo"})
    table = normalInfo.find("table")
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")

    jobs = []
    for i in range(len(trs)):
        # 채용 공고가 없는 회사 건너뜀
        if trs[i].find("td").get_text() == "채용공고가 없습니다.":
            continue
        # 필요없는 값 건너뜀(summaryView)        
        if i % 2 == 0:
            job = extractInfo(trs[i])            
            jobs.append(job)
    
    return jobs

def saveToFile(company, jobs):
    time.sleep(1)
    # 파일 깨짐 방지를 위해 인코딩을 utf-8로 실행
    # mode="w" 는파일이 이미 존재하고 내용이 있을때 새로운 내용으로 덮어쓴다.
    file = open(f"{company}.csv", mode="w", newline="", encoding="utf-8")
    # csv를 작성하기 위해 writer설정
    writer = csv.writer(file)
    writer.writerow(['place', 'title', 'time', 'pay', 'date'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

companys, hrefs = getSuperBrandHrefs()
for i in range(len(hrefs)):
    print(companys[i])
    saveToFile(companys[i], extractInfos(hrefs[i]))
    
