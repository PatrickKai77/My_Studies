import random

squares=[]
for value in range(1,12):
    squares.append(value**2)
print(squares)
#randomizando valores e adicionando na lista com o laço for
lista =[]
for valores in range(10):
    lista.append(random.randrange(1,100))
print(lista)
#list comprehension
squares=[value**2 for value in range(1,100,4)]
print(squares)
#dice -- random 
resultado= random.randrange(1, 7)
print(resultado)
for value in range(5):
    print(" Escolhendo um número aleatório..." +str(random.randrange(1,7)) )
#espada dano 
vida_player=[]
for vida in range(1):
    vida_player.append(random.randrange(1,9) + random.randrange(2,8))
    print(vida_player)