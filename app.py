from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/password', methods=("GET", "POST"))
def password():
    return render_template('password.html')


def password0():
    if request.method == "POST":
        asd = request.form['valami']
        if asd == 'pass':
            print('asdasd')

@app.route('/editalas')
def edit():
    return render_template('edit.html')


if __name__ == '__main__':
    app.run()



#password
