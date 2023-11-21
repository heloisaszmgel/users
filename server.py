from flask import Flask, render_template, request, redirect
from users import Users
app = Flask(__name__)

@app.route('/')
def read():
    users = Users.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
        Users.save(data)
        return redirect('/')
    else:
        
        return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)