
# Librerías Python - Matplotlib - Numpy

import matplotlib.pyplot as plt

import numpy as np


# Diagramas Barras - 001


eje_x = ['Python', 'R', 'Node.js', 'PHP']
 
eje_y = [50,20,35,47]
 
plt.bar(eje_x, eje_y)
 
plt.ylabel('Cantidad de usuarios')

plt.xlabel('Lenguajes de programación')
 
plt.title('Usuarios de lenguajes de programación')
 
plt.show()

plt.figure()

# Diagrama Barras - 002

eje_x = ['Prog.', 'Ciencia', 'Mat.', 'Ing.']
 

eje_y = [76,31,45,57]
 
plt.barh(eje_x, eje_y, color="green")

plt.ylabel('Empleados')

plt.xlabel('Habilidades')

plt.title('Habilidades')

plt.show()

plt.figure()


# Diagranas Barras - 003

serie_1 = [406, 387, 442, 457, 485]
serie_2 = [421, 453, 435, 478, 512]
 
 
numero_de_grupos = len(serie_1)
indice_barras = np.arange(numero_de_grupos)
ancho_barras =0.35
 
plt.bar(indice_barras, serie_1, width=ancho_barras, label='Hombres')
plt.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Mujeres')
plt.legend(loc='best')

plt.xticks(indice_barras + ancho_barras, ('2017', '2018', '2019', '2020','2021'))
 
plt.ylabel('Numero de habitantes')
plt.xlabel('Año')
plt.title('Numero de habitantes por genero')
 
plt.show()

plt.figure()



