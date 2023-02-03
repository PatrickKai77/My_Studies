user_0 = {
'username': 'efermi',
'first': 'enrico',
 'last': 'fermi', }

for k, v in user_0.items():
    print("\nKey:" + k)
    print("Value: " + v) 

favorite_languages = {
'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}

for name,language in favorite_languages.items():
     print(name.title() +"'s favorite language is " + language.title() + ".")

#pegarmos somente os valores
for language in favorite_languages.values():
    print(language.title())

#pegarmos somente as chaves
for name in favorite_languages.keys():
    print(name.title())

#laço for para conferir se algum amigo esta no dicionario e exibir uma mensagem caso tiver
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Olá " + name.title() + ", pelo que vejo aqui sua linguagem favorita é " + favorite_languages[name].title() + ".")


#Podemos usar o método key, para descobrir se uma pessoa em particular partciipou de uma enquente ou evento
if 'erin' not in favorite_languages.keys():
    print("Por favor Erin, realize nossa enquete.")


#Percorrendo as chaves de um dicionário em ordem usando sorted em um laço
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", obrigado por realizar nossa enquete.")

#extração de todos valores contidos, porém para dicionarios grandes pode ser um problema.
print("As linguagens a seguir foram mencionadas:")
for language in favorite_languages.values():
    print(language.title())


#Para ver cada linguagem escolhida sem repetições, podemos usar um conjunto (set)
for language in set(favorite_languages.values()):
    print(language.title())