from flask_app import app
from flask import render_template, redirect,request, session, flash
from flask_app.models.user import Users

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/create_friend', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    } 
    Users.save(data)
    print(data)
    return redirect('/info.html')
@app.route('/info.html')
def final():
    friends = Users.get_all()
    print(friends)
    session['x'] = len(friends)
    return render_template('info.html', all_users = friends)
@app.route('/show.html/<int:num>')
def showinfo(num):
    friends = Users.get_all()
    print(friends)
    return render_template('show.html', all_users= friends, num = num)
@app.route('/delete/<int:num>')
def getrid(num):
    friends = Users.remove(num)
    return redirect('/info.html')

@app.route('/update.html/<int:num>')
def update(num):
    num1 = num
    friends = Users.get_all()
    return render_template('update.html', all_users = friends, num1 =num1)

@app.route('/change/<int:num1>',methods=['POST'])
def change(num1):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : request.form['id']
    }
    print(data)
    friends = Users.update(data)
    return redirect(f'/show.html/{num1}')
