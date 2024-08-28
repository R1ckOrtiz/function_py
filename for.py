# lista = [2,6,9,4,0,3,12,7]
# palavra = 'Bóson'
# for letra in palavra:
#     print(letra)

# nome = input('Digite seu nome:')
# for x in range(10):
#     print(f'{x+1} {nome}')

#range(valor_inicial, valor_final, incremento)
# for x in range (2, 20, 2):
#     print(x)

pedras = ('rubi','esmeralda', 'safira', 'diamante')

for pedra in pedras:
    if pedra == 'diamante':
        continue
    print(pedra)