from flask import Flask, render_template, request, redirect, send_file
from scrapper import getJobs
from exporter import saveToFile

app = Flask("webScrapper", template_folder='./flask_server/templates')

# fakeDB
db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    # 사용자 입력 formating
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = getJobs(word)
            db[word] = jobs
    # word가 None일경우 처리
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        saveToFile(jobs)
        return send_file("./flask_server/jobs.csv")
    except:
        return redirect("/")
        

app.run(debug=True)