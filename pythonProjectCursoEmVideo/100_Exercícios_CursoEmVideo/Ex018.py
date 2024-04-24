# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print(f"Seno do ângulo de {angulo}°: {seno:.2f}")

cosseno = math.cos(math.radians(angulo))
print(f'Cosseno do ângulo de {angulo}°: {cosseno:.2f}')

tangente = math.tan(math.radians(angulo))
print(f'Tangente do ângulo de {angulo}°: {tangente:.2f}')
