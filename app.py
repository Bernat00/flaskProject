from flask import Flask, render_template, request, url_for
import foods

app = Flask(__name__)


@app.route('/')
def etlap():
    etelek = foods.load('templates/foods.csv')

    return render_template('home.html', etelek=etelek)

@app.route('/add', methods={'GET', 'POST'})
def uj_etel():
    if request.method == "POST":
        nev = request.form["name"]
        leiras = request.form["leiras"]
        allergen = request.form["allergen"]
        valami = [nev, leiras, allergen]
        foods.add('templates/foods.csv', valami)
    return render_template('add.html')




#password,urlrandomization

if __name__ == '__main__':
    app.run()
