import json

with open('c:/Users/306/Downloads/cuartos_champions_2019.json', 'r') as archivo:
    datos = json.load(archivo)
total_rojas = 0

for partido in datos["Resultados"]:
    total_rojas += datos["Resultados"][partido]["Tarjetas"]["Rojas"]

# Creamos el nuevo JSON con el total de tarjetas rojas
salida = {
    "Total Tarjetas Rojas": total_rojas
}

# Guardamos el nuevo archivo
with open('total_rojas.json', 'w') as salida_archivo:
    json.dump(salida, salida_archivo, indent=4)

print("Archivo creado con éxito: total_rojas.json")
