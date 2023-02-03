motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
#para adicionarmos um item no final da lista, usaremos o nome da lista.append('')
motorcycles.append('biz')
print (motorcycles)
#podemos criar uma lista vazia e ir preenchendo conforme a necessidade do usuário
aliens=[]
aliens.append('okin'),aliens.append('brovik')
print(aliens)
#podemos inserir um novo elemento na posição x, para isso usamos o insert
aliens.insert(0,'olavik')
print(aliens)
#por vezes, vamos querer deletar um elemento da lista
del aliens[0]
print(aliens)

boss = ['havon','\nvida:',"300"]
print(boss[0].title(),boss[1],boss[2])
#removendo um item com pop() // Diferença de usar pop é que o valor é deletado para o usuário, mas ainda fica disponivel
#para nós devs... por exemplo, removemos da lista de ativos e movemos para inativos
boss_inativo= boss.pop(0)
print("O ultimo boss derrotado foi o " + boss_inativo.title() + ", ele tinha "+ boss[1] + " pontos de vida.")

enemy_race = ['ork','Alien', 'mage', 'swordsman','troll']
tier_1 ='ork'
tier_2 = 'mage'
tier_3 = 'troll'
enemy_race.remove(tier_3)
print(enemy_race)