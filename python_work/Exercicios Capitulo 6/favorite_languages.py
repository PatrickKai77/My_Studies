import random

participantes={
    'clara':[],
    'clark':[],
    'mark':[],
    'ronald':[],
}
ling=('ruby','java','python')

print("Bem vindos à enquete! De antemão agradecemos a presença de vocês.")

def random_select():
        for name in participantes.keys():
            participantes[name].append(random.choice(list(ling)))
        name=list(participantes.keys())
        print(name)
        for names in name:
            print("Obrigado por realizar nossa enquete, " + names.title() + ".")


random_select()