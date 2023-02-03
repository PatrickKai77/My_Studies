patrick_database={
    'first-name':'Patrick',
    'last-name':'Furtado dos Santos',
    'cpf':'027.2460.790-54',
    'idade':21,
    'city':'Tubarão',
}
print(patrick_database['first-name'])




num_fav={
    'gustavo':8,
    'aatrox':7,
    'brendon':3,
    'patrick':5,
    'favix':1,
    'kai':4
}
for nome,numero in num_fav.items():
    print('O número de ' + nome.title() + ' é: ' + str(numero) + ".")



glossario={
    'laço-for':'É um comando para realizar alguma tarefa, em cada valor contido em uma variável.\n',
    'if':'É um teste de verifição, se for algo TRUE, fazer tal ação.\n',
    'append':'É um comando para adicionar dados à uma lista ou dicionário.\n',
    'title':' É um comando que deve ser usado após o nome da variável pois ele permite que a variável mostre sua primeira letra em maiúsculo.\n',
    'print':'Exibe uma mensagem na tela.',
}

for comando,significado in glossario.items():
    print("➤ " + comando.title() + ": " + significado)

rios={
    'amazonas':'brasil',
    'nilo':'egito',
    'volga':'russia'
}
for rio,local in rios.items():
    print(rio +" "+ local)
    if rio == 'nilo':
        print('O ' + rio.title()+ " fica localizado no " + local.title()+".\n")
    elif rio == 'amazonas':
        print('O ' + rio.title()+ " fica localizado no " + local.title()+".\n")
    elif rio == 'volga':
        print('O ' + rio.title()+ " fica localizado na " + local.title()+".\n")