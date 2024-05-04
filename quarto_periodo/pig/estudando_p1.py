
"""
def suduku_principal():
        lista=[[],[],[],[],[],[],[],[],[]]
        for c in range(0,9):
            for c2 in range(0,9):
                lista[c].append(".")
        return lista
listas = suduku_principal()

horinzontal = ['0','1','2','3','4','5','6','7','8']
vertical = [0,1,2,3,4,5,6,7,8]

horizontal_visual = ' '.join(horinzontal)
print(f'   {horizontal_visual}')
print('  ------------------')
for c in range(0,9):
    hozontal_ventical = ' '.join(horinzontal)
    lista_visual = ' '.join(listas[c])
    print(f'{vertical[c]}| {lista_visual}')
"""

lista=[0,1,2,3,4,5]
print(len(lista))