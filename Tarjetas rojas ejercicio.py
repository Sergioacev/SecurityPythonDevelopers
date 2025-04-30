import json

# Abrir el archivo JSON
with open('c:/Users/306/Downloads/cuartos_champions_2019.json', 'r') as archivo:
    datos = json.load(archivo)

total_rojas = 0
total_amarillas = 0
detalle_partidos = []
ganadores = []

# Procesar los partidos
for partido in datos["Resultados"]:
    rojas = 0
    amarillas = 0

    # Verificar si hay tarjetas
    if "tarjetas" in partido:
        rojas = partido["tarjetas"].get("rojas", 0)
        amarillas = partido["tarjetas"].get("amarillas", 0)
        total_rojas += rojas
        total_amarillas += amarillas

    # Procesar los goles si están en los campos 'goles_local' y 'goles_visitante'
    goles_local = partido.get("goles_local", 0)
    goles_visitante = partido.get("goles_visitante", 0)
    local = partido.get("local", "Desconocido")
    visitante = partido.get("visitante", "Desconocido")

    # Determinar el ganador
    if goles_local > goles_visitante:
        ganador = local
    elif goles_visitante > goles_local:
        ganador = visitante
    else:
        ganador = "Empate"

    if ganador != "Empate":
        ganadores.append(ganador)

    # Guardar detalle del partido
    detalle_partidos.append({
        "Partido": f'{local} vs {visitante}',
        "Tarjetas Rojas": rojas,
        "Tarjetas Amarillas": amarillas
    })

# Guardar resultados en un archivo
salida = {
    "Total Tarjetas Rojas": total_rojas,
    "Total Tarjetas Amarillas": total_amarillas,
    "Detalle por Partido": detalle_partidos
}

with open('total_tarjetas.json', 'w') as salida_archivo:
    json.dump(salida, salida_archivo, indent=4)

# Mostrar resumen de tarjetas
print("Resumen de tarjetas:")
print(f"Total Tarjetas Rojas: {total_rojas}")
print(f"Total Tarjetas Amarillas: {total_amarillas}")
print("\nDetalle por partido:")
for detalle in detalle_partidos:
    print(f'{detalle["Partido"]} - Rojas: {detalle["Tarjetas Rojas"]}, Amarillas: {detalle["Tarjetas Amarillas"]}')

# Mostrar ganadores
print("\nGanadores de los partidos de cuartos de final:")
for equipo in ganadores:
    print(equipo)

print("\nArchivo creado con éxito: total_tarjetas.json")


