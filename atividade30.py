# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

media = 0
soma = 0
nomeHomemMaisVelho = ''
maiorIdadeHomem = 0
mulheresMenorQue20 = 0

for i in range(1,5):
    nome = str(input(f"digite o nome da {i}ª pessoa: "))
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("digite M para MASCULINO \n F para FEMININO: \n "))
    sexo = sexo.upper()
    
    soma += idade

    if sexo == "M" and idade >= maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo == "F" and idade < 20:
        mulheresMenorQue20 += 1

print('Media das idades é de {:.2f} '.format(media))
print('Nome do mais velho é {}'.format(nomeHomemMaisVelho))

if mulheresMenorQue20 == 0:
    print('Não temos mulheres no grupo !')

else:
    print('A todo temos {} mulheres com menor de 20 anos'.format(mulheresMenorQue20))