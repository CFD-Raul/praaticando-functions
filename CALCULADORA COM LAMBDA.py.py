#Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma 
# calculadora para somar, subtrair, multiplicar e dividir dois números.

#Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador 
# matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.




primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

operadores = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

operacao = input('Escolha a operação matemática (+, -, *, /): ')

if operacao not in operadores:
    print("Operação inválida!")
elif operacao == '/' and segundo_numero == 0:
    print("Erro: divisão por zero!")
else:
    resultado = operadores[operacao](primeiro_numero, segundo_numero)
    print(f'O resultado é: {resultado:.2f}')