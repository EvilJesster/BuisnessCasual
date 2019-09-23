# Pratham Rawat & Jesse Hall
# SoftDev1 pd1
# K<n> -- Jinja Tuning
# 2019-09-18   

from flask import Flask, render_template
from util import csvLoading as loader

app = Flask(__name__);

@app.route("/")
def whyTho():
    # page = open("renstart.html", "r")
    # html = page.read()
    hi = [1,3,5,6,6,7]
    return render_template('renstart.html', d = hi )

@app.route("/occupyflaskst")
def nice():
    jobsDictionary = loader.inputCSV("data/occupations.csv")
    randomJob = loader.randomValue(jobsDictionary)
    return render_template('jobs.html', randomJob = randomJob[0], dictionary = jobsDictionary)

if __name__ == "__main__":
    app.debug = True
    app.run()
