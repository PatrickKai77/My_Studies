import random

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#código para gerar mais aliens, para isso vamos usar o range

aliens_x=[]

speed="slow",'medium','fast'
color='red','green','yellow'
points='5','10','15'

for alien_num in range(30):
    new_alien={'color':[random.choice(color)],'points':[random.choice(points)],'speed':[random.choice(speed)],}
    aliens_x.append(new_alien)
for alien in aliens_x[:5]:
    print(alien)
print("...")
print("O número total de aliens são: " + str(len(aliens_x)))