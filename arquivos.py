#Manipulação de arquivos de texto.


# print(f'\nMétodo readline():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'\nMétodo readlines():\n')
# print(manipulador.readlines())
# texto = input('Qual termo deseja procurar no arquivo?')
# try:
#     manipulador = open('arquivo.txt', 'r', encoding='utf - 8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'A string foi encontrada!')
#             print(linha)
#         else:
#             print(f'String não encontrada!')
# except IOError:
#     print(f'Não foi possivel abrir o arquivo')
# else:
#     manipulador.close()

#Escrever em arquivos de texto

try:
     manipulador = open('arquivo.txt', 'w', encoding='utf - 8')
     manipulador.write('Bóson Treinamentos\n')
     manipulador.write('Como criar um arquivo de texto com Python.')
except IOError:
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()

