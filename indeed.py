# requests 라이브러리는 파이썬에서 요청을 만드는 기능을 모아 놓은 라이브러리
import requests
# html에서 데이터를 추출하는 라이브러리
from bs4 import BeautifulSoup

PAGE = 1
LIMIT = 100
URL = f"https://www.saramin.co.kr/zf_user/search?loc_mcd=101000%2C105000&cat_kewd=84&loc_bcd=&search_optional_item=y&panel_count=y&recruitPage={PAGE}&recruitSort=relation&recruitPageCount={LIMIT}&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&searchword=&show_applied=&quick_apply=&except_read=&mainSearch=n"

def extractIndeedPages():
    resul = requests.get(URL)
    soup = BeautifulSoup(resul.text, 'html.parser')

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

def extractIndeedJobs(lastPage):
    jobs = []
    for page in range(lastPage):
        PAGE = page + 1
        result = requests.get(f"{URL}")
        print(result.status_code)
    return jobs
        
# request github : https://github.com/psf/requests
# beautifulsoup guide : https://www.crummy.com/software/BeautifulSoup/bs4/doc/