### DESAFIO CODE ONE
## JOGO DA FORCA

from random import choice

print('JOGO DA FORCA!')
nome = input('Qual o nome do jogador: ')
#print('Qual o nome do jogador: Thomas')
#nome = 'Thomas'
print(f'{nome} bem vindo ao jogo!')
print('O jogo acaba quando o jogador erra a letra pela sexta vez.')
print('Ou quando acertar todas as letras')
print('')

lista_palavras = ['abacaxi', 'lego', 'xadrez', 'banana', 'python', 'pera', 'azul', 'popes']
#lista_palavras = ['banana','banana']
pal = choice(lista_palavras)
palavra = list(pal)
#print(palavra)
print(f'A palavra sorteada tem {len(palavra)} letras.')
forca = len(palavra)*['_']
print(forca)
print('')

erros = 0
while erros < 6 and '_' in forca:
    letra = input('Digite uma letra: ')
    if letra in palavra:
        quantidade = palavra.count(letra)
        posicao = palavra.index(letra)
        for i in range(quantidade):
            posicao = palavra.index(letra, posicao)
            forca[posicao] = letra
            posicao +=1
    else:
        erros += 1
    print(forca)
    print('Número de erros: ', erros)
    print('')

if erros == 6:
    print('Você perdeu!')
    print('A palavra sorteada era:')
    print(pal)
else:
    print('Voce ganhou')


