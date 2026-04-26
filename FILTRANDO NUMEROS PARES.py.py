#Lucas está desenvolvendo um sistema para gerar relatórios financeiros 
# e precisa filtrar apenas os valores pares de uma lista de números 
# informada pelo usuário.

#Crie um programa que receba uma lista de números 
# e exiba apenas os pares usando a função filter().


numeros_do_usuario = input('Digite os números separados por espaço: ').split()
pares = filter(lambda x: int(x) % 2 == 0, numeros_do_usuario) 
print("Números pares:", " ".join(pares)) 