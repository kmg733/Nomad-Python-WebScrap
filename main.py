from saramin import getJobs as getSaraminJobs
from save import saveToFile

# 웹크롤러 실행
saraminJobs = getSaraminJobs()
# csv파일로 저장
saveToFile(saraminJobs)
