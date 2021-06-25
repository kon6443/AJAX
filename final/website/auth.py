from flask import Blueprint, render_template, request
import sqlite3

auth = Blueprint('auth', __name__)

headings = ("Country", "State/Province", "County", "University", "Program", "Requirements")

conn = sqlite3.connect('database.db')


def look(uni):

    c = conn.cursor()
    c.execute("SELECT Requirements FROM Uni_Programs_Requ WHERE University = (?)", (uni,))
    rows = c.fetchall()

    for row in rows:
        print(row)


@auth.route('/home')
def home():
    return render_template("home.html")


@auth.route('/manual')
def manual():
    return render_template("manual.html")


@auth.route('/search')
def search():
    return render_template("search.html")


@auth.route('/requirements')
def requirements():
    return render_template("requirements.html", headings=headings, data=data)


@auth.route('/requirements', methods=['POST'])
def getvalue():
    country = request.form['Country']
    state = request.form['State/Province']
    county = request.form['County']
    university = request.form['University']
    return render_template('requirements.html', C=country, s=state, c=county, u=university)


