# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:22:01 2021

@author: Andrés Díaz
"""
import random

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

# 2. En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.


print('\n---------- SORTEO DE DESCUENTOS ----------\n')
valor_compra = float(input('Ingrese valor de la compra: '))
num_sorteo = random.randint(0, 100)
descuento = 0
precio_total = 0
descuento_uno = 15/100
descuento_dos = 20/100
resultado = ""

if(num_sorteo < 74):
    descuento = valor_compra * descuento_uno
    precio_total = valor_compra - descuento
    resultado = "es menor que 74, el cliente ganó un descuento del 15%."
else:
    descuento = valor_compra * descuento_dos
    precio_total = valor_compra - descuento
    resultado = "es mayor que 74, el cliente ganó un descuento del 20%."
print('\n---------- RESULTADOS DEL SORTEO ----------\n')
print(f'Precio de la compra: ${valor_compra:,}')
print(f'El número del sorteo es {num_sorteo}, este {resultado}')
print(f'Valor del descuento: ${descuento:,}')
print(f'Precio total con descuento: ${precio_total:,}')









