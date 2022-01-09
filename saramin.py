# requests 라이브러리는 파이썬에서 요청을 만드는 기능을 모아 놓은 라이브러리
import requests
# html에서 데이터를 추출하는 라이브러리
from bs4 import BeautifulSoup

URL_A = f"https://www.saramin.co.kr/zf_user/search?loc_mcd=101000%2C105000&cat_kewd=84&loc_bcd=&search_optional_item=y&panel_count=y&recruitPage="
URL_B = "&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&searchword=&show_applied=&quick_apply=&except_read=&mainSearch=n"
def getLastPage():
    result = requests.get(URL_A +'1'+URL_B)
    soup = BeautifulSoup(result.text, 'html.parser')

    # 최대 페이지 찾기
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')

    # 페이지들을 리스트에 저장
    # 마지막에 필요없는 문자열값이 들어가므로 빼고 실행
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    maxPage = pages[-1]
    return maxPage

def extractJob(html):
    # 채용공고의 제목
    areaJob = html.find("div", {"class": "area_job"})
    ajAnchor = areaJob.find("a")["title"]
    

    # 채용공고의 내용(경력, 학력 등)
    jobCondition = areaJob.find("div", {"class": "job_condition"})
    jcSpans = jobCondition.find_all("span")

    joc = []
    jocLocation = []
    for jcSpan in jcSpans:
        # 회사주소가 a태그로 묶여있어서 beautifulSoup에서 None으로 인식함
        if jcSpan.string == None:
            location = ''
            jcSpanAnchors = jcSpan.find_all("a")
            # 사람인 사이트에서 주소를 말할때 a태그로 한번더 묶여있는 경우도 있음
            for jcSpanAnchor in jcSpanAnchors:
                location += jcSpanAnchor.string + ' '                            
            jocLocation.append(location.strip())
            
        # 나머지 경력, 학력, 계약직 등의 정보
        else:
            joc.append(jcSpan.string)

    # 채용공고의 내용2(채용 분야)
    jobSector = areaJob.find("div", {"class": "job_sector"})
    jsAnchors = jobSector.find_all("a")

    # 채용분야 (백엔드/서버개발, 웹개발, 프론트엔드, API 등)
    jsa = []
    for jsAnchor in jsAnchors:
        jsa.append(jsAnchor.string)

    # 채용하는 회사
    corpName = html.find("strong", {"class": "corp_name"})
    cnAnchor = corpName.find("a")["title"]

    return {'title': ajAnchor, 'location': jocLocation, 'condition': joc, 'sector': jsa, 'company': cnAnchor}


def extractJobs(lastPage):
    jobs = []
    for page in range(lastPage):
        print(f"Scrapping page {page}")
        PAGE = page + 1
        result = requests.get(f"{URL_A}{PAGE}{URL_B}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "item_recruit"})

        # 채용공고 정보 가져오기
        for result in results:
            job = extractJob(result)
            jobs.append(job)
    
    return jobs
        

def getJobs():        
    lastPage = getLastPage()
    jobs = extractJobs(lastPage)
    return jobs

# request github : https://github.com/psf/requests
# beautifulsoup guide : https://www.crummy.com/software/BeautifulSoup/bs4/doc/