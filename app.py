"""
Name: Bryant Hanks
Assignment: CS336 Assignment #10
Created:12/11/2022
Description: main app that runs the website
"""

from flask import Flask, render_template, request, session
from database_code import registrationtable, userstable
from datetime import date
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretsuperlongnoonewillguesskey'
today = date.today()

"""
Decorator to confirm the user is logged into the session
"""
def status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return "You are not logged in"
    return wrapper

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin')
@status
def admin():
    return render_template("admin.html")

@app.route('/login', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        userstable.create()
        user = userstable.validate(username, password,)
        if user == None:
            return render_template('login.html', msg='Invalid Username or Password')
        else:
            session['logged_in'] = True
            return render_template('admin.html')
    else:
        return render_template("login.html")

@app.route('/nametags10gen')
def nametags10gen():
    return render_template("nametags10gen.html")

@app.route('/activities')
def activities():
    return render_template("activities.html")

@app.route('/awards', methods=['GET', 'POST'])
def awards():
    if request.method == 'POST':
        vote = "Thank you for voting!"
        return render_template("awards.html", vr=vote)
    else:
        vote = ""
        return render_template("awards.html", vr=vote)

@app.route('/keynote')
def keynote():
    return render_template("keynote.html")

@app.route('/meals')
def meals():
    return render_template("meals.html")

@app.route('/poll')
def poll():
    return render_template("poll.html")

@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        dictionary = request.form
        dictionaryList = inputlist(dictionary)
        registrationtable.insert_registrants(dictionaryList)
        return render_template("thankyou.html",
                               regdte = dictionaryList[0],
                               title = dictionaryList[1],
                               firstname = dictionaryList[2],
                               lastname = dictionaryList[3],
                               addy1 = dictionaryList[4],
                               addy2 = dictionaryList[5],
                               city = dictionaryList[6],
                               state = dictionaryList[7],
                               zip = dictionaryList[8],
                               telephone = dictionaryList[9],
                               email = dictionaryList[10],
                               position = dictionaryList[11],
                               company = dictionaryList[12],
                               day1 = dictionaryList[13],
                               day2 = dictionaryList[14],
                               day3 = dictionaryList[15],)
    else:
        return render_template("registration.html")

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

@app.route('/workshopschedule')
def workshopschedule():
    return render_template("workshopschedule.html")

"""
converts the coded session names into their actual names while adding registration date and removing 
unnecessary form information
@inputlist - Dictionary to be changed to list with updated info
"""
def inputlist(inputlist):
    dictionaryList = list(inputlist.values())
    dictionaryList[0] = today.strftime("%Y-%m-%d")
    if dictionaryList[13] == 'a1':
        dictionaryList[13] = 'Effective Listener'
    elif dictionaryList[13] == 'a2':
        dictionaryList[13] = 'Difficult Conversations'
    else:
        dictionaryList[13] = 'Different Personalities'

    if dictionaryList[14] == 'b1':
        dictionaryList[14] = 'Effective Tools'
    elif dictionaryList[14] == 'b2':
        dictionaryList[14] = 'Proper Planning'
    else:
        dictionaryList[14] = 'Value of Project Management'

    if dictionaryList[15] == 'c1':
        dictionaryList[15] = 'Benefits of a Balanced Life'
    elif dictionaryList[15] == 'c2':
        dictionaryList[15] = 'Techniques to Balance Life'
    else:
        dictionaryList[15] = 'Personal Life Management'
    dictionaryList.pop(16)
    
    return dictionaryList

if __name__ == '__main__':
    app.run()