# planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas:
#     print(planeta)

bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)

bebida.sort()

print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'\nSaúde!')
