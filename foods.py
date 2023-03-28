def load(path):
    with open(path, 'r', encoding="UTF-8") as file:
        etelek = []
        file = file.read()
        file = file.strip()
        file = file.split('\n')
        del file[0]

        for i in file:
            i = i.split(';')

            etel = {
                'nev': i[0],
                'leiras': i[1],
                'allergen': i[2],
                'id': int(i[3])
            }
            etelek.append(etel)

        return etelek


def write(path, data):
    kajak = 'nev;leiras;allergenek'
    counter = 1
    for i in data:
        kaja = '\n' + i['nev'] + ';' + i['leiras'] + ';' + i['allergen'] + ';' + str(counter)
        kajak = kajak + kaja
        counter += 1

    with open(path, 'w', encoding='UTF-8') as file:
        file.write(kajak)


def add(path, kaja):
    kelid = load(path)
    kelid = kelid[-1]
    try:
        kelid = kelid["id"]
    except:
        kelid = 0

    with open(path, 'a', encoding='UTF-8') as file:
        kaja = '\n' + kaja[0] + ';' + kaja[1] + ';' + kaja[2] + ';' + str(kelid + 1)
        file.write(kaja)


def edit(path):
    data = load(path)
    asdasd = []
    for i in data:
        etel = {
            'nev': i['nev'],
            'leiras': i['leiras'],
            'allergen': i['allergen'],
            'id': i['id'],
            'is_edit': False
        }
        asdasd.append(etel)

    return asdasd


def delete(path, nev):
    data_new = []
    data = load(path)
    for line in data:
        if line["nev"] != nev:
            data_new.append(line)

    write(path, data_new)
