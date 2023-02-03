#fatiando a lista
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
print(players[:3])
print(players[3:])
print(players[-3:])
#percorrendo uma fatia da lista com for
print("Top 3 melhores jogadores:\n")
for player_best in players[0:3]:
    print(player_best.title())
print("Top 3 piores jogadores:\n")
for player_bad in players[-3:]:
    print(player_bad.title())

