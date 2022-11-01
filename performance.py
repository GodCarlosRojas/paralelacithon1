# FIchero para la prueba
# comparativa de rendimiento
# solo python con cython

import time
import py_planet
import cy_planet
#Python----------------------------------------------------------
init_time = time.time()
planetita = py_planet.Planet()
planetita.step_time(planetita, 100, 100)
fin_time = time.time()
total_time_python = fin_time - init_time
print("TIempo total de python", total_time_python)

#Cython----------------------------------------------------------
init_time = time.time()
planetita = cy_planet.Planet()
planetita.step_time(planetita, 100, 100)
fin_time = time.time()
total_time_cython = fin_time - init_time
print("Tiempo total de cython", total_time_cython)

#Comparativa----------------------------------------------------------
print(f"Cython es {total_time_python/total_time_cython} veces mas rapido que python")
