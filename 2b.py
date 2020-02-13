'''
Created on 11 feb. 2020

@author: DAM112
'''
import random
numaleatorio = random.randint(1, 100)

for var in range(1,11):
    num=int(input("Escribe un numero"))
    if num>numaleatorio:
        print(num,"es mayor que el numero aleatorio")
    elif num<numaleatorio:
         print(num,"es menor que el numero aleatorio")
    else:
       print("has acertado en",var,"intento")
       break

