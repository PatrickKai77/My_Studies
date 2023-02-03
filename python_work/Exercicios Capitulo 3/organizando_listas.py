cars = ['bmw', 'audi', 'toyota', 'subaru']
#Ao usarmos o sort, a lista mudará pernamentemente.
cars.sort() #organizamos a lista em ordem alfabetica, podemos fazer o inverso também.
print(cars)
cars.sort(reverse=True)#aqui passamos para o sort fazer o contrário.
print(cars)
#Ordenando uma lista temporariamente com a função sorted()
print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)
print('---------------')
#Exibindo uma lista em ordem inversa
print(cars)
cars.reverse() 
print(cars)
len(cars)