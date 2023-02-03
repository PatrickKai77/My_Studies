name='ada wong'
print(name.title())
#um método é uma ação que o python pode executar em um dado, por exemplo o title.
#Métodos tendem a acompanhar parenteses vazios após seu nome, 
print(name.lower( ))
print(name.upper())

user="kailuz"
id = str("2381236754")
message = 'Bem vindo, ' + user.title() + " " + 'o seu  número de registro é: ' + id
print(message)
print("Linguagens de programação:\tHasagi\nZoreaguedon\nHackerman")
#remoção de espaços em branco, métodos, rstrip(),lstrip() ou remover dos dois  lados com strip()
teste= "   testando uso do método rstrip "
print(teste)
teste = teste.strip()
print(teste)