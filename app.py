from flask import Flask, render_template, request, url_for
import foods

app = Flask(__name__)

foods_path = 'templates/foods.csv'


@app.route('/')
def etlap():
    etelek = foods.load(foods_path)

    return render_template('home.html', etelek=etelek)


@app.route('/add', methods={'GET', 'POST'})
def uj_etel():
    if request.method == "POST":
        nev = request.form["name"]
        leiras = request.form["leiras"]
        allergen = request.form["allergen"]
        valami = [nev, leiras, allergen]
        foods.add(foods_path, valami)
    return render_template('add.html')


@app.route('/edit', methods={'GET', 'POST'})
def edit_etel():
    etelek = foods.edit(foods_path)

    if request.method == "POST":
        for key in request.form:
            if key == 'edit.change':
                for etel in etelek:
                    if etel['id'] == int(request.form["edit.change"]):
                        etel['is_edit'] = True

        for a in request.form:
            if a == 'edit.del':
                for etel in etelek:
                    if etel['id'] == int(request.form["edit.del"]):
                        foods.delete(foods_path, etel['nev'])


        if "save" in request.form:     # ez nem mükszik
            nev = request.form["name"]
            leiras = request.form["leiras"]
            allergen = request.form["allergen"]
            valami = [nev, leiras, allergen]
            print(valami)
            print('asdasd')


            # ez epikk
    #  for key in request.form:
    #      if key.startswith('edit.'):
    #          request_id = request.form[key]

    return render_template('edit.html', etelek=etelek)


# password,urlrandomization

if __name__ == '__main__':
    app.run()
