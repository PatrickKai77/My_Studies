#restaurante

print("Bem vindos ao restaurante Le Tabou.")
num_clientes=input("Você está acompanhado de quantas pessoas?\n")
num_clientes=int(num_clientes)
if num_clientes >=8 :
    print("Certo... Como vocês estão entre " + str(num_clientes) + ", terão que aguardar alguns minutos.")
else:
    print("Certo... Mesa para " + str(num_clientes) + ", por aqui por favor. ")