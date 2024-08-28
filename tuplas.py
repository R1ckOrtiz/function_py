#São imutáveis

halogenios = ('F', 'C1', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
print(halogenios[-1])
# t1 = (5,2,6,4,4,6,5,1,13,3,1,5)
print('Fe' in halogenios)

#Operações não disponiveis em tuplas: . sort(), . append(), .reverse(), .pop()...

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# #print(grupo17)

grupo1 = ['L1', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

print(sorted(alcalinos))
print(alcalinos.sort())


