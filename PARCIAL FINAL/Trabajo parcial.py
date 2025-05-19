import os
import re
import json
import requests

archivos_log = [
    "access_log",
    "access_log.1",
    "access_log.2"
]

expresion = r'^(\d{1,3}(?:\.\d{1,3}){3}) - - \[(.*?)\] "(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) (\/\S*) HTTP\/\d\.\d"'

def extraer_datos(expresion, ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8", errors="ignore") as f:
        contenido = f.read()
    return re.findall(expresion, contenido, re.MULTILINE)

def obtener_pais(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        return data.get("country", "Desconocido")
    except:
        return "Desconocido"

resultado = {}

for archivo in archivos_log:
    if os.path.exists(archivo):
        datos = extraer_datos(expresion, archivo)
        for ip, fecha, metodo, ruta in datos:
            pais = obtener_pais(ip)
            if pais not in resultado:
                resultado[pais] = {"Hacks": []}
            resultado[pais]["Hacks"].append({
                "fecha": fecha,
                "metodo": metodo,
                "ruta": ruta
            })

with open("hacks_por_pais.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)

print("✅ Archivo JSON generado: hacks_por_pais.json")
