a = list()
dados = list()
media2 = media1 = 0

b = [1,2,3,4,5]
def media(a):
    for c in range(0,len(a)):
        media1= media1 + a[c]
        media2 = media1/len(a)
    return media2

print(f'{media(b)}')
