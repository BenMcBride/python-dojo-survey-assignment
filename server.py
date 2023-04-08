from flask import Flask, render_template, request, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "pineapple juice"
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def post():
    print(request.form)
    session.permanent = True
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['textarea'] 
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")


if __name__=="__main__":
    app.run(debug=True)
