from flask import Flask, render_template, request,redirect,session

from user import Users
app = Flask(__name__)
app.secret_key = 'lamelo ball'
@app.route("/")
def index():
    if 'x' not in session:
        session['x'] = 0
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
    print(data)
    print(data)
    print(data)
    friends = Users.update(data)
    return redirect(f'/show.html/{num1}')



if __name__ == "__main__":
    app.run(debug=True)
