from indeed import extractIndeedJobs, extractIndeedPages

lastIndeedPage = extractIndeedPages()
indeedJobs = extractIndeedJobs(lastIndeedPage)

for i in indeedJobs:
    print(i)