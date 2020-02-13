'''
Created on 10 feb. 2020

@author: DAM112
'''

sueldo = int(input("Introduce el sueldo:"))
comision1 = int(input("Introduce la primera comision"))
comision2 = int(input("Introduce la segunda comision"))
comision3 = int(input("Introduce la tercera comision"))

sueldototal = sueldo + (comision1+comision2+comision3)*0.1

print(sueldototal)