#Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. 
# Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.


 

def calcular_idade(ano_nascimento, ano_atual): 
    return ano_atual - ano_nascimento 
 
nascimento = int(input("Digite o ano de nascimento: ")) 
atual = int(input("Digite o ano atual: ")) 
idade = calcular_idade(nascimento, atual) 
print(f"A idade é {idade} anos.") 




 # FIZ DESSE JEITO: 
 # def calculadora_etaria():
    #ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
    #ano_atual = int(input('Digite o ano atual: '))

    #idade_do_aluno = ano_atual - ano_de_nascimento
   # mensagem = f'A idade do aluno é {idade_do_aluno} anos.'
  #  return mensagem

#print(calculadora_etaria()) 
# MAS DESSA FORMA A FUNÇÃO ESTÁ ESTÁTICA, O GABARITO PROPOS UMA SOLUÇÃO MAIS REUTILIZÁVEL E DINÂMICA: ver acima!



