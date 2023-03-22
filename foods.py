def load(path):
    with open(path, 'r', encoding="UTF-8") as file:
        etelek= []
        file = file.read()
        file = file.strip()
        file = file.split('\n')
        del file[0]
        for i in file:
            i = i.split(';')

            etel = {
                'nev': i[0],
                'leiras': i[1],
                'allergen': i[2]
            }
            etelek.append(etel)


        return etelek


def add(path, kaja):
    with open(path, 'a',encoding='UTF-8') as file:
        kaja = kaja[0]+';'+kaja[1]+';'+kaja[2]+'\n'
        file.write(kaja)

