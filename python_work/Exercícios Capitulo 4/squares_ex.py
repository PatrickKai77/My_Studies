#4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os
for valor in range(1,21):
    print(valor)
#4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números. (Se a saída estiver demorando demais, interrompa pressionando CTRL-C ou feche a janela de saída.) 
#for valor in range(1,1000001):
    print(valor)
#4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min()
#e max() para garantir que sua lista realmente começa em um e termina em um
#milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é
#capaz de somar um milhão de números.
lista=[]
for valor in range(1,1000001):
    lista.append(valor)
print(lista)
minima=min(lista)
print(minima)

maxima=max(lista)
print(maxima)

soma=sum(lista)
print(soma)
#4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
#uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os números.
numeros_impar=[]
for valor in range(1,21,2):
    numeros_impar.append(valor)
print(numeros_impar)
#4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
#exibir os números de sua lista.
multiplo_3=[value**3 for value in range(3,31)]
print(multiplo_3)
#4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
#exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
#primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
#para exibir o valor de cada cubo.
cubos_10=[]
for cubo in range(1,11):
    multi=cubo**3
    cubos_10.append(multi)
print(cubos_10)
cubos_10=[valor**3 for valor in range(1,11)]
print(cubos_10)
