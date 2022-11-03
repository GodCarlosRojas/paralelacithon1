"""
FEcha: 2/11/2022
NOmbre: Carlos Andres Rojas Rocha
y crar un csv con la tima de tiempos
"""


import py_orbita
import cy_orbita
import time
"""
EJemplo  python usando a la tierra con datos de wikipedia
"""
tierraPy = py_orbita.Planet()
tierraPy.x = 100*10**3
tierraPy.y = 300*10**3
tierraPy.z = 700*10**3
tierraPy.vx = 2.000*10**3
tierraPy.vy = 29.87*10**3
tierraPy.vz = 0.034*10**3
tierraPy.m = 5.9741*10**24
"""
EJemplo  cython usando a la tierra con datos de wikipedia
"""
tierraCy = cy_orbita.Planet()
tierraCy.x = 100*10**3
tierraCy.y = 300*10**3
tierraCy.z = 700*10**3
tierraCy.vx = 2.000*10**3
tierraCy.vy = 29.87*10**3
tierraCy.vz = 0.034*10**3
tierraCy.m = 5.9741*10**24

time_span = 400
n_steps = 2000000

#DEfinicion de experimentos
#REduccion de ruido gaussiano

#Se crea un formato para la impresion sobre el fichero
formato_datos = "{:.5f},{:.5f}\n"

for i in range(2):
	#Toma de tiempos phyton
	inicioPy = time.time()
	tierraPy.step_time(tierraPy, time_span, n_steps)
	finalPy = time.time() - inicioPy
	
	#Toma de tiempos Cython
	inicioCy = time.time()
	tierraCy.step_time(tierraCy, time_span, n_steps)
	finalCy = time.time() - inicioCy

	with open("tierra.csv","a") as archivo:
		archivo.write(formato_datos.format(finalPy,finalCy))
