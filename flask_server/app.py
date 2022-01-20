from flask import Flask

app = Flask("webScrapper")

@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"

@app.route("/<username>")
def contact(username):
    return f"Hello your name is {username}"

app.run(debug=True)