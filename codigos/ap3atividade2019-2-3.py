def converter(num):
    if num != 0:
        if num % 2 == 0:
            print(num)
            return converter(num // 2) + '0'
        else:
            print(num)
            return converter(num // 2) + '1'
    return ''

resultado = converter(10)
print(resultado)