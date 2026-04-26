# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia.
# As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, 
# converta os valores para números e exiba o total.

def conversor_de_valores(lista):
    return [float(valores) for valores in lista]

valores = input('Digite os valores das vendas: ').split()
valores_convertidos = conversor_de_valores(valores)
total = sum(valores_convertidos)
print(f'O total das vendas foi: R${total:.2f}')