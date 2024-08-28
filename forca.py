import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'inteligencia', 'programacao', 'computador']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return ''.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas_restantes = 6

    while tentativas_restantes > 0:
        print(f'Palavra: {exibir_palavra(palavra, letras_corretas)}')
        print(f'Tentativas restantes: {tentativas_restantes}')
        letra = input('Digite uma letra: ').lower()

        if letra in letras_corretas:
            print('Você já tentou essa letra.')
        elif letra in palavra:
            letras_corretas.add(letra)
            print('Boa! Você acertou uma letra.')
        else:
            tentativas_restantes -= 1
            print('Letra incorreta.')

        if all([letra in letras_corretas for letra in palavra]):
            print(f'Parabéns! Você adivinhou a palavra: {palavra}')
            break
    else:
        print(f'Você perdeu! A palavra era: {palavra}')

jogar_forca()
