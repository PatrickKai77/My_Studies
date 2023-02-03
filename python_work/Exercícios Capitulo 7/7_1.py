carros = ['subaru', 'toyota','gol']
print("olá qual carro você gostaria de comprar?")
for car in carros:
    print(car.title())
escolha=input()
if escolha in carros:
    print("Ótima escolha, o " + escolha.title() + " é um ótimo carro.")
