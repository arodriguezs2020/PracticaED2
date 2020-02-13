'''
Created on 11 feb. 2020

@author: DAM112
'''

paises = ["China", "India", "USA", "Indonesia"]
poblaciones = [1987, 168, 587, 688]
print(list(zip(paises, poblaciones)))

for pais, poblacion in zip(paises, poblaciones):
    print("{}: {} millones de habitantes.".format(pais, poblacion))
