from flask import Flask, render_template, request,redirect

from user import Users
app = Flask(__name__)
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
    return render_template('info.html', all_users = friends)
    

if __name__ == "__main__":
    app.run(debug=True)