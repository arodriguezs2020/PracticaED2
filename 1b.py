'''
Created on 11 feb. 2020

@author: DAM112
'''

num = int(input("Escribe un numero:"))
numaux=1;

while num>1:
    numaux=numaux*num
    num=num-1
print("Factorial",numaux)