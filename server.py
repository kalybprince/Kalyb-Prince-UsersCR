from flask import Flask, render_template, request, redirect, session
from users import User

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    print("@/")
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route('/create.html')
def create():
    print('@/create.html')
    return render_template('create.html')

@app.route('/process', methods=["POST"])
def process():
    print("@/process")
    data = {
        'fname' : request.form['first_name'],
        'lname' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

# done