carros_marca = ['CHEVROLET','VOLKSWAGEN','FIAT','MERCEDES-BENZ','CITROEN','CHANA','SUBARU','FORD','DODGE','RENAULT','LAMBORGUINI']
#---Mensagens-padrão----
welcome = "Bem vindo à revendedora Stark!"
offer = "O que você deseja? Temos desde veiculos da marca " + carros_marca[0] + " até " + carros_marca[10] + "."
catalogo_show = "Aqui está nosso catálogo..."
message_change_list = "Aguarde só um segundo, estamos sofrendo algumas alterações no catálogo."
#-----------------------
print(welcome)
print(offer)
carros_marca.sort()
print('----------')
print(catalogo_show)
print(carros_marca)
print(message_change_list)
outsale = carros_marca.pop(0), carros_marca.pop(3), carros_marca.pop(3)
change_list = carros_marca.append('AUDI')
print('-------------')
print("Outsale List")
print(outsale)
print('-------------')
print("Avaliable")
carros_marca.sort()
print(carros_marca)
print('-------------')