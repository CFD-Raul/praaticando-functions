#Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. 
# Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
#Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

def soma_recursiva(numero_do_ususario):
    if numero_do_ususario == 1:
        return 1
    return numero_do_ususario + soma_recursiva(numero_do_ususario - 1)

numero_do_usuario = int(input('Digite um número para realizar a soma: '))
resultado = soma_recursiva(numero_do_usuario)
print(f' A soma dos números inteiros de 1 a {numero_do_usuario} é: {resultado}')