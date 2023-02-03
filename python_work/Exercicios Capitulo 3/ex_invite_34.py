friends=['favian','dioguin','kaitiluz','kaitigroski']
message_convite =", através desta carta, venho convidá-lo para minha festa."
print('---------------')
print(friends[0].title()+ message_convite)
print(friends[1].title()+message_convite)
print(friends[2].title()+ message_convite)
print(friends[3].title()+ message_convite )
friends_off= friends.pop(0)
print('---------------')
print('Lista de Cancelamento')
print(friends_off)
print("Convidados confirmados")
print(friends[0],friends[1],friends[2])
print('---------------')
newinvite = "rumble"
print("Devido o cancelamento de "+friends_off.title()+", iremos convidar o " + newinvite.title() + ".")
friends.append('rumble')
print('---------------')
print('Lista de Cancelamento')
print(friends_off)
print("Convidados confirmados")
for convidados_confirmados in friends:
    print(convidados_confirmados.title())
for convidados in friends:
    print(convidados.title() + ", através desta carta, venho convidá-lo para minha festa.")
friends.insert(0, 'yone')
friends.insert(3, 'zed')
friends.append('irelia')
print('---------------')
print("Devido à algumas alterações, temos novos convidados.")
print('---------------')
for convidados in friends:
    print(convidados.title())
print('---------------')
print('Convites')
print('---------------')
for convidados in friends:
    print(convidados.title() + ", através desta carta, venho convidá-lo para minha festa.")
print('---------------')
#3.7 Reduzindo a lista de convidados
sedex_message = 'Senhor, devido à um infortúnio na empresa, demoraremos para realizar a entrega da mesa. Sentimos muito. Att:Sedex'
print(sedex_message)
print('---------------')
message_diminuir_lista= 'Pessoal, sinto muito, mas não receberei a mesa a tempo. Poderei oferecer os convites apenas para duas pessoas. Sinto muito!'
print(message_diminuir_lista)
message_apologize="Senhor(a), devido à um imprevisto, não teremos espaço suficiente para alocar todos convidados, logo estou revogando seu convite. Sentimos muito. Para: "
print('---------------')
for friends_off in friends:
    friends_off=friends.pop(0)
    print(message_apologize + friends_off.title())
print('---------------')
print("Convidados confirmados")
print(friends[0],friends[1])
print('---------------')
print(friends[0] + message_convite)
print(friends[1] + message_convite)
print('---------------')
del friends[0]
del friends[0]
print(friends)
