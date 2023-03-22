# jobb lenne class-al
class foods:
    def __init__(self, path, kaja):
        self.kaja = kaja
        self.path = path

    def load(self):
        with open(self.path, 'r', encoding="UTF-8") as file:
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
                    'allergen': i[2]
                }
                etelek.append(etel)

        return etelek

    def add(self):
        with open(self.path, 'a', encoding='UTF-8') as file:
            kaja = '\n' + self.kaja[0] + ';' + self.kaja[1] + ';' + self.kaja[2]
            file.write(kaja)
