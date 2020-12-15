import math
angulo = float(input('Qual a ângulo que você deseja calcular?: '))

sen = math.sin(math.radians(angulo))

coss = math.cos(math.radians(angulo))

tg = math.tan(math.radians(angulo))

print(f'O seno do ângulo é {sen:.2f} \n o cosseno desse ângulo é {coss:.2f} \n a tangente desse ângulo é {tg:.2f}')
