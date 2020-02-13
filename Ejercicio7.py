'''
Created on 10 feb. 2020

@author: DAM112
'''
from Tools.scripts import pindent

min = int(input("Introducee el numero de minutos:"))

horas = min // 60
mins = min % 60

print(horas,"horas y",mins,"minutos")

