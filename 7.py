#Parte 7

pesos = float(input("Ingrese la cantidad de pesos que desea convertir:"))
def Conversor(pesos):
    return f"${pesos*(1/3934.82)}"
print(f"{Conversor(pesos)} dólares")
