bycicles= ['trek', 'blek','flek','hasagui', 'sdljkhasl', 'assassins']
print(bycicles)
print(bycicles[2].title())
print(bycicles[-1]) #este devolve o ultimo item da lista
print(bycicles[-2]) #se formos decresendo, pegaremos sempre o index correspondente partir do final.
#Isto é útil para acessar os valores de uma lista muito grande.
message= "A bicicleta " + bycicles[-1].title() + " custa R$5000. Deseja comprar?"
print(message)