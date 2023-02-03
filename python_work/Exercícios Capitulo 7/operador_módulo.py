#Determinar se um numero é impar ou par
number=input("Digite um número e te direi se é impar ou par: ")
number=int(number)
if number % 2 == 0:
    print("Este número: " + str(number) + ", é par.")
else:
    print("Este número: " + str(number) + ", é ímpar.")