#Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
#Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

def desconto(porcentagem_do_desconto):
    def valor_final(valor_da_compra):
        return valor_da_compra - (valor_da_compra * (porcentagem_do_desconto / 100))
    return valor_final

valor_da_compra = float(input('Digite o preço bruto do produto: '))
porcentagem_do_desconto = float(input('Digite a porcentagem de desconto desejada (de 1 a 100): '))
calcular_desconto = desconto(porcentagem_do_desconto)
preco_final = calcular_desconto(valor_da_compra)
print(f'O preço final com desconto é de: R${preco_final}')
