# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.


#ESSA FOI A MINHA SOLUÇÃO:

# def contador_de_caracteres():
#    return f'A palavra {palavra_digitada} tem {numero_de_caracteres} caracteres.'

#palavra_digitada = input('Insira a palavra a ser contada: ')
#numero_de_caracteres = len(palavra_digitada)

#print(contador_de_caracteres())

# O PROBLEMA AQUI É QUE A FUNÇÃO SEM PARAMETRO É MENOS INDEPENDENTE E REUTILIZAVEL, POR DEPENDER DE VARIAVEIS EXTERNAS;
# ESTÁ LIMITADA COM UMA MENSAGEM PRE DEFINIDA QUE SE REDUZ A UM UNICO USO;
# SERIA DIFICIL UTILIZAR EM UM EXERCICIO ONDE FOSSE NECESSARIO CONTAR OS CARACTERES DE MAIS DE UMA PALAVRA POR VEZ

#MENOS É MAAAAAIS!!!


def contar_caracteres(palavra):
    return len(palavra)

texto = input('Digite uma palavra a ser contada: ')
print(f'A palavra {texto} possui {contar_caracteres(texto)} caracteres.')