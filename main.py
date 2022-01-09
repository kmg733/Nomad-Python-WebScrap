# requests 라이브러리는 파이썬에서 요청을 만드는 기능을 모아 놓은 라이브러리
import requests
# html에서 데이터를 추출하는 라이브러리
from bs4 import BeautifulSoup

pg_resul = requests.get('https://www.saramin.co.kr/zf_user/search?loc_mcd=101000%2C105000&cat_kewd=84&loc_bcd=&search_optional_item=y&panel_count=y&recruitPage=1&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&searchword=&show_applied=&quick_apply=&except_read=&mainSearch=n')
pg_soup = BeautifulSoup(pg_resul.text, 'html.parser')

# 최대 페이지 찾기
pagination = pg_soup.find("div", {"class":"pagination"})
links = pagination.find_all('a')

# 페이지들을 리스트에 저장
# 마지막에 필요없는 문자열값이 들어가므로 빼고 실행
pages = []
for link in links[:-1]:
    pages.append(int(link.string))

maxPage = pages[-1]


# request github : https://github.com/psf/requests
# beautifulsoup guide : https://www.crummy.com/software/BeautifulSoup/bs4/doc/