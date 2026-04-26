#Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. 
# Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.

#Crie um programa que junte as listas e exiba o resultado no formato produto: preço

produtos_a_venda = input('Digite os nomes dos produtos separados por virgula: ').split(',')
precos_dos_produtos = input('Digite os preços dos produtos separados por virgula: ').split(',')
produtos_precificados = '\n'.join(f'{n.strip()} : {p.strip()}' for n, p in zip(produtos_a_venda, precos_dos_produtos))
print(produtos_precificados)