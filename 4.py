# Parte 4

taller_1 = (float((input("Ingrese la nota de Taller 1:")))*(0.2))
taller_2 = (float((input("Ingrese la nota de Taller 2:")))*(0.15))
cuestionario_1 = float(input("Ingrese la nota de cuestionario 1:"))*(0.22)
cuestionario_2 = float(input("Ingrese la nota de cuetionario 2:"))*(0.1)
proyecto_final = float(input("Ingrese la nota del proyecto final:"))*(0.33)
print(f"La nota definitiva del del estudiante es: {cuestionario_1+cuestionario_2+proyecto_final+taller_1+taller_2}")
