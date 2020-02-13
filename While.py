'''
Created on 11 feb. 2020

@author: DAM112
'''

secreto = "asdasd"
while True:
    clave=input("Dime la clave:")
    if clave != secreto:
        print("Clave incorrecta")
    if clave == secreto:
        break;
print("Bienvenido!!")
print("Programa Terminado")
