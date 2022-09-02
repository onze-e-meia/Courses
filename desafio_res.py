### DESAFIO CODE ONE / RESOLUÇÃO
## JOGO DA FORCA

import os
from random import choice

os.system('cls')
nome = input('Digite seu nome:' )
print(f'Olá seja bem vindo {nome}! Vamos começar a jogar?')
input('\nPrecione enter para iniciar o jogo...')
os.system('cls')

lista_palavras = ['banana', 'laranja', 'abacaxi', 'limao', 'uva'] 
palavra = choice(lista_palavras).upper()
tamanho = len(palavra)
forca = ['_']*tamanho
qtd_erros = 0

while '_' in forca and qtd_erros < 6:
    print(f'\nSua palavra tem {tamanho} letras.')
    print(f'Quantidade de erros: {qtd_erros}/6!')
    for letra in forca:
        print(letra, end = ' ')
    print()

    letra = input('Digite uma letra: ').upper()
    acertou = False
    for i in range(tamanho):
        if letra == palavra[i]:
            forca[i] = letra
            acertou = True
    
    if acertou == True:
        print('Acertou a letra!')
    else:
        print('Errou, não exite essa letra!')
        qtd_erros += 1

if qtd_erros == 6:
    print('\nVocê perdeu!')
else:
    print('\nVocê ganhou, parabéns!')

print(f'A palavra era: {palavra}')