'''
entrada de dados
        
podemos obter as informacoes do usuario atraves da funcao input()

'''
nome = input("Digite o seu nome: ")
print(nome)

#Type casting - convertebdo os tipos de dados em tempo de execucao
idade = int(input("Digite sua idade: "))
print(type(idade))
ano_nascimento = 2022 - idade
print(ano_nascimento)

#others casts
a = str(3) #'3'
b = int("3") # 3
c = float("3") # 3.0

