#Parte 6

minimo_antiguo = float(input("Ingrese el salario minimo antiguo:"))
def Salario_minimo_nuevo(minimo_antiguo):
    return ((minimo_antiguo)*0.042)+(minimo_antiguo)
print(f"El nuevo salrio mínimo para el próximo año es:{Salario_minimo_nuevo(minimo_antiguo)}")
