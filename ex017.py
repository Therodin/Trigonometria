from math import sqrt

co = float(input('qual a medida do cateto oposto?: '))
ca = float (input('qual a medida do cateto adjacente?: '))

hi = (co ** 2 + ca **2)
hii = sqrt (hi)

print(f'A soma do quadrado dos catetos é igual ao quadrado da hipotenusa: {hii:.2f} ')