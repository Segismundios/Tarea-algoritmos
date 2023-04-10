def power_of_two (n):
    return n > 0 and n & (n-1) == 0

n = int(input('Ingrese un numero: '))

if power_of_two(n):
    print(f'{n} es una potencia de 2')
else:
    print(f'{n} no es una potencia de 2')