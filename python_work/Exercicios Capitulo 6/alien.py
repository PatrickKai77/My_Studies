
alien_0 = {'color':'green','points':5}
print(alien_0['points'])
print(alien_0['color'])
new_points= alien_0['points']
print("You just earned " + str(new_points) + " points!") 
print("Score:"+ str(new_points))
new_points=new_points + alien_0['points']
print("Score:"+ str(new_points))
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
orc={}
orc['vida'] = 70
orc['dano'] = 15
orc['x_position'] = 7
orc['y_position'] = 20
orc['speed'] = 'medium'
print(orc)
if orc['speed'] == 'fast':
    x_increment=3
elif orc['speed'] == 'medium':
    x_increment=2
else:
    x_increment=1
print("Original x-position: " + str(orc['x_position']))

orc['x_position'] = orc['x_position'] + x_increment
print("New x-position: " + str(orc['x_position']))

if orc['vida'] >= 100:
    print('O orc tem muita vida!')
else:
    print('Podemos derrotar o orc!')