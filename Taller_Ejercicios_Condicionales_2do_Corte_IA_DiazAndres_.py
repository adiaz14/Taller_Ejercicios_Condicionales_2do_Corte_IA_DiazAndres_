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

# 3. Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que consite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.

print('\n---------- COMPAÑIA DE SEGUROS ----------\n')

finaza = float(input('Ingrese valor de la fianza: '))

monto_pagar = 0
porcentaje_cuota_uno = 2/100
porcentaje_cuota_dos = 3/100
porcentaje = 0

if(finaza < 50000):
    monto_pagar = finaza * porcentaje_cuota_dos
    porcentaje = porcentaje_cuota_dos * 100
else:
    monto_pagar = finaza * porcentaje_cuota_uno
    porcentaje = porcentaje_cuota_uno * 100
print('\n---------- RESUMEN DEL ESTUDIO DE FINANZA ----------\n')
print(f'Valor de la fianza del cliente: ${finaza:,}')
print(f'Porcentaje cuota: {porcentaje:,}%')
print(f'Monto a pagar por el cliente: ${monto_pagar:,}')

# 4. Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.

print('\n---------- AUDITORÍA DE CONTROL DE CONTAMINACIÓN ----------\n')

ganancias = float(input('Ingrese valor de las ganancias diarias de '
                        'la fábrica: '))
multa = 0
ganancia_total = 0
acumulado = 0
dias_evaluacion = 5
contaminacion = 0

for dia in range(dias_evaluacion):
    puntos = float(input(f'Ingrese puntos de contaminación del día {dia + 1} '
                         f'de la evaluación: '))
    acumulado += puntos
contaminacion = acumulado / 5

print('\n-------- RESUMEN DE AUDITORÍA DE CONTROL DE CONTAMINACIÓN --------\n')
print(f'Las ganancias diarios de la fabrica son: ${ganancias:,}')
print(f'El promedio de puntos de contaminación es: {contaminacion}')
if(contaminacion > 170):
    multa = ganancias * 50 / 100
    print(f'La empresa no supero la prueba de contaminación, '
          f'fue multada por un monto de: ${multa:,}')
else:
    print('La empresa supero la prueba de contaminación, no fue multada.')

# 5. Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del valor
# del terreno. Ayúdale a esta pesona a determinar si debe o no comprar
# el automóvil.

print('\n---------- COMPRA DE AUTOMÓVIL O TERRENO ----------\n')

valor_bien = float(input('Ingrese valor del bien: '))
tasa_devaluacion = float(input('Ingrese porcentaje de devaluación del'
                               ' automóvil: '))
tasa_valorizacion = float(input('Ingrese porcentaje de valorización'
                                ' del terreno: '))

bien_devaluado = 0
bien_valorizado = 0
valor_devaluacion_anio = valor_bien * tasa_devaluacion / 100
valor_valorizacion_anio = valor_bien * tasa_valorizacion / 100
respuesta_comprador = ""

valor_devaluacion_anio = valor_devaluacion_anio * 3
valor_valorizacion_anio = valor_valorizacion_anio * 3

if(valor_devaluacion_anio < (valor_valorizacion_anio/2)):
    respuesta_comprador = "El comprador debe adquirir el automóvil."
else:
    respuesta_comprador = "El comprador debe adquirir el terreno."

print('\n---------- RESULTADOS DEL ANÁLISIS DE COMPRA DE BIENES ----------\n')
print(f'El valor de los bienes es ${valor_bien:,}, respectivamente.')
print(f'Devaluación acumulada del automóvil en 3 años: '
      f'${valor_devaluacion_anio:,}')
print(f'Valorización acumulada del terreno en 3 años: '
      f'${valor_valorizacion_anio:,}')
print(respuesta_comprador)






