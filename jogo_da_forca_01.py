from random import choice

with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

palavra = choice(lista_de_palavras).upper()

forca = """
________
        | 
        |
        -"""
vazio = """

"""
cabeca = """
        O
"""
tronco = """
        O
        |
"""
braco_esq = """
        O
       /|
"""
braco_dir = """
        O
       /|\\ 
"""
perna_esq = """
        O
       /|\\ 
       /  
"""
perna_dir = """
        O
       /|\\
       / \\
"""

chances_do_boneco = [
    vazio,
    cabeca,
    tronco,
    braco_esq,
    braco_dir,
    perna_esq,
    perna_dir,
]


acertos = 0
erros = 0
letras_certas = ''
letras_erradas = ''

while acertos != len(palavra) and erros != 7:
    mensagem = ''
    for letra in palavra:
        if letra in letras_certas:
            mensagem += f'{letra} '
        else:
            mensagem += '_ '
    print(mensagem)
    print(forca + chances_do_boneco[erros])
    print(f'Você errou as seguintes letras: {letras_erradas}')

    letra = input('Digite uma letra: ').upper()

    if letra in letras_certas+letras_erradas:
        print('Você ja digitou essa letra')
        continue

    if letra in palavra:
        print('Voce acertou a letra')
        letras_certas += letra
        acertos += palavra.count(letra)
    else:
        print('Você errou a letra')
        letras_erradas += letra
        erros += 1

if acertos == len(palavra):
    print(f'Você ganhou o jogo!! A palavra certa é: {palavra}')
else:
    print('Você perdeu o jogo!!')
    print(f'A palavra escolhida é: {palavra}')