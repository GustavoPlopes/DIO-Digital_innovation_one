nome = "Gustavo"
idade = 25
profissao = "programador"
linguagem = "python"
saldo = 50.255

dados = {"nome": "Gustavo", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}" .format(nome, idade))

print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))

print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}")

print(f"Meu nome é {nome}, tenho {idade}, sou {profissao} e codifico na linguagem {linguagem}" + "\n" + f"Meu saldo é de: {saldo}")