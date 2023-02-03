#criação da classe item
class Item(object): 
    def __init__(self, nome, dano, description): 
        self.__nome = nome
        self.__dano = dano
        self.__descrição=description

    def __repr__(self): 
        return "Nome:%s \nDano:%s \nDescrição:%s" % (self.__nome, self.__dano, self.__descrição)

    def get_nome(self):   
        return self.__nome

    def get_dano(self): 
        return self.__dano
    def get_descrição(self):
        return self.__descrição


#criação da classe monstro
class monstro(object): 
    def __init__(self, nome, dano, description): 
        self.__nome = nome
        self.__dano = dano
        self.__descrição=description

    def __repr__(self): 
        return "Nome:%s \nDano:%s \nDescrição:%s" % (self.__nome, self.__dano, self.__descrição)

    def get_nome(self):   
        return self.__nome
    def get_dano(self): 
        return self.__dano
    def get_descrição(self):
        return self.__descrição


espada_sagrada=Item("Espada Sagrada",10, "Uma espada Sagrada construida em um vilarejo antigo.")
player = 'kirito'
inventario=[]
mob_orc=monstro('Dano',15,"Vida",30,'Descrição: ',"Um orc nascido nas profundezas do tataro.")

print(player +"!!")
print(player +"!!")
print('Haruna: Antes de partir em sua jornada. Pegue a espada sagrada do vilarejo. Peço que volte vivo! Prometa!')

promessa=input()
if promessa == 'yes':
    print("Haruna: Certo. Tome cuidado! Tchau!")
    inventario.append(espada_sagrada)

print("Kirito olha então para o seu inventário.")
for items in inventario:
    print(items)

#aventura 1
print("Kirito: O que?!! Um orc!")
print("Duel Start! ")