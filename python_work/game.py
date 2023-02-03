import random
#Dicionário Database

inventario={
    'item':[],
    'quantidade':[],
}

#-----------------------

print('-----------')
print('W\n  e\n     l\n     c\n  o\n   m\ne')
print('-----------')

#Login area
print("Area de Registro")
player_nick = input('Player name:')
senha = input('Senha: ')
dados_user_login={'user':player_nick,'pass':senha}

#Confirmação de login
print("Por favor confirme sua senha:")
senha_confirma=input()
if senha_confirma == dados_user_login['pass']:
    print("Bem vindo ao Sistema " + player_nick + ".")
else:
    print("Senha incorreta! Encerrando sistema...")
    exit()
#------------------------
valor=10
dano=random.randint(0,valor)
print(dano)
#Começo da história
item_1=['drake sword',1]
item_2=['dente de vampiro',1]
resp=input()
if resp == 'grab':
    inventario['item'].append(item_1[0])
    inventario['quantidade'].append (item_1[1])
print(inventario)

vampiro={'vida':30, 'dano':10,}
if vampiro['vida'] == 0:
    print("Voce acabou de matar um vampiro.")
    print