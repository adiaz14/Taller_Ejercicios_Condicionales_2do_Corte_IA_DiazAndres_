# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:22:01 2021

@author: Andrés Díaz
"""

# Realizar los algoritmos que den solución a la problemática presentada
# en los siguientes ejercicios

# 1. Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

print('\n---------- VENTA DE CAMISAS ----------\n')
num_camisas = int(input('Ingrese cantidad de camisas a comprar: '))
precio_unitario = float(input('Ingrese el precio de las camisas: '))

descuento = 0
precio_bruto = 0
precio_total = 0
descuento_uno = 10/100
descuento_dos = 30/100
precio_bruto = num_camisas * precio_unitario

if(num_camisas > 0 and precio_unitario > 0):
    if (num_camisas < 3):
        descuento = num_camisas * precio_unitario * descuento_uno
        precio_total = precio_bruto - descuento
    else:
        descuento = num_camisas * precio_unitario * descuento_dos
        precio_total = precio_bruto - descuento
    print('\n---------- RESUMEN DE VENTA DE CAMISAS ----------\n')
    print(f'Número de camisas: {num_camisas}')
    print(f'Precio unitario: ${precio_unitario:,}')
    print(f'Precio total antes de descuento: ${precio_bruto:,}')
    print(f'Valor del descuento: ${descuento:,}')
    print(f'Precio total con descuento: ${precio_total:,}')
else:
    print('El número de camisas y sus precios deben ser mayores a cero\n')
