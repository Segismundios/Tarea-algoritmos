def power_of_two (n):
    return n > 0 and n & (n-1) == 0

n = int(input('Ingrese un numero: '))

print(power_of_two(n))