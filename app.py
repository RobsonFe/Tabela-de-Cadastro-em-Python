#Projeto Feito por Robson Ferreira

#Aluno: Robson Ferreira da Silva 
#Curso de Analise e Desenvolvimento de Sistemas
#1º Periodo

print("\t\tTabela de Cadastro\n")

lista = []

while True:
    
    nome = input("Nome completo: ")
    lista.append(nome)
    idade = int (input("Qual a sua idade ? "))
    lista.append(idade)
    profissao = input("Qual a sua profissão ? ")
    lista.append(profissao)
    sexo = input ("Qual o sexo ? (F/M) ")
    lista.append(sexo)
    salario = float(input("Qual o seu salario ? "))
    lista.append(salario)
    resp = input("Deseja fazer outro cadastro ? SIM ou NAO ? ")

    if resp.upper() == "NAO": 
        break 

print ("\t\tPessoas Cadastradas\n")
print()

for lista in lista:
      print (lista)
