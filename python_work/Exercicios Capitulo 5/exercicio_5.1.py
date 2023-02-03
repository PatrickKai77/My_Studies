car = ['subaru']
if 'subaru' in car:
    print("Is'subaru' in car? I predict True.") 
    print('subaru' in car)
    car.append('audi')
if 'audi' in car:
    print("\nAudi está na lista carro? I predict False.") 
    print('audi' in car)
cars_off=car.pop(1)
print('\nAinda está disponivel para venda o Audi?')
if 'audi' in car:
    print("Gostaria de comprar. Tenho uma oferta.")
    print('audi' in car)
else:
    print('É uma pena, estava interessado neste.')
print('Vou levar o Subaru')
cars_sold=car.pop(0)
print(car)