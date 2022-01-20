from flask import Flask, render_template, request, redirect
from scrapper import getJobs

app = Flask("webScrapper", template_folder='./flask_server/templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    # 사용자 입력 formating
    if word:
        word = word.lower()
        jobs = getJobs(word)
        print(jobs)
    # word가 None일경우 처리
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word)

app.run(debug=True)