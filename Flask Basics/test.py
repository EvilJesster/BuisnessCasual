# Pratham Rawat
# SoftDev1 pd1
# K<n> -- <Title/Topic/Summary>
# 2019-09-18   

from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def whyTho():
    # page = open("renstart.html", "r")
    # html = page.read()
    hi = [1,3,5,6,6,7]
    return render_template('renstart.html', d = hi )

@app.route("/thisissosad")
def bruh():
    print(__name__ + "bruh")
    return "this is so sad"

@app.route("/thisissosad/okthisisepic")
def epic():
    print(__name__ + "nice")
    return "ok"


if __name__ == "__main__":
    app.debug = True
    app.run()
