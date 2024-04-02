from flask import Flask, render_template
import requests

articles = requests.get("https://api.npoint.io/77eca90acb6650e93f74").json()



app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_articles = articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:id>")
def post(id):
    return render_template("post.html", all_articles=articles, id=id)


if __name__ == "__main__":
    app.run(debug=True)