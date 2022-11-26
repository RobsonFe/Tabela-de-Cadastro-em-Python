#Projeto Feito por Robson Ferreira

#Aluno: Robson Ferreira da Silva 
#Curso de Analise e Desenvolvimento de Sistemas
#1º Periodo

print("\t\tTabela de Cadastro\n")

n = int(input("Quantas pessoas serão cadastradas ? "))

lista = [0 for x in range (n)]

for i in range(0,n):
    
    nome = input("Nome completo: ")
    lista[i] = nome
    idade = int (input("Qual a sua idade ? "))
    lista[i] = idade
    profissao = input("Qual a sua profissão ? ")
    lista[i] = profissao
    sexo = input ("Qual o sexo ? (F/M) ")
    lista[i] = sexo
    salario = float(input("Qual o seu salario ? "))
    lista[i] = salario 

print()

print("\t\tPessoas Cadastradas \n")
for i in range(0,n):
    print (lista[i])
