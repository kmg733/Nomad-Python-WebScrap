import csv

def saveToFile(jobs):
    # 파일 깨짐 방지를 위해 인코딩을 utf-8로 실행
    # mode="w" 는파일이 이미 존재하고 내용이 있을때 새로운 내용으로 덮어쓴다.
    file = open("./flask_server/jobs.csv", mode="w", newline="", encoding="utf-8-sig")
    # csv를 작성하기 위해 writer설정
    writer = csv.writer(file)
    writer.writerow(['title', 'location', 'condition', 'sector', 'company'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return