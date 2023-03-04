from flask import Flask
<<<<<<< HEAD

=======
from flask import render_template
>>>>>>> 8bff3c5 (base)
app = Flask(__name__)


@app.route('/')
<<<<<<< HEAD
def hello_world():  # put application's code here
    return 'valami!'
=======
def hello_world():
    return render_template('home.html')
>>>>>>> 8bff3c5 (base)


if __name__ == '__main__':
    app.run()
