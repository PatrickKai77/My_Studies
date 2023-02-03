alien_color='red'
if alien_color == 'green':
    print("Você acertou! 5 pontos obtidos.")
#------------------------
alien_color='green'
print("Qual a cor do alien? ")
print('Red, Green, White, Blue, Yellow.')
resp=input()
if resp == alien_color:
    print("Você acertou! 5 pontos obtidos.")
else:
    print("Você errou, -3 pontos! A cor correta é " + alien_color)

print("Round 2!!")
alien_color='white'
print("Qual a cor do alien? ")
resp=input('Red, Green, White, Blue, Yellow.\n')
if resp == alien_color:
    print("Você acertou! 15 pontos obtidos.")
elif resp == 'green':
    print('Você acabou de ganhar 3 pontos.')
elif resp == 'blue':
    print('Você acabou de ganhar 7 pontos.')
elif resp == 'yellow':
    print('Você acabou de perder 100 pontos.')
else:
    print("Entendi.")