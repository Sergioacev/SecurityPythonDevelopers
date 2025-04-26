import re, json

navegadoresContados = {}

def extractFromRegularExpression(regex, data):
    if data:
        return re.findall(regex, data)
    return []

# Abrir y leer el archivo de logs
with open(r"C:\Users\sergi\Downloads\access.log", "r", encoding="utf-8") as file:
    data = file.read()

# Expresión regular para capturar el User-Agent (último grupo entre comillas)
regex = r'\"[^\"]*\"[^\"]*\"[^\"]*\"[^\"]*\"[^\"]*\"([^\"]*)\"'

# Extraer los User-Agents
resultados = extractFromRegularExpression(regex, data) or []

# Si no se encuentran resultados, informar
if not resultados:
    print("No se encontraron coincidencias. Verifica el formato del archivo o la expresión regular.")
else:
    # Clasificar los User-Agents por tipo de navegador
    for agente in resultados:
        if "Chrome" in agente and "Edg" not in agente:
            navegador = "Chrome"
        elif "Firefox" in agente:
            navegador = "Firefox"
        elif "Safari" in agente and "Chrome" not in agente:
            navegador = "Safari"
        elif "Edge" in agente or "Edg" in agente:
            navegador = "Edge"
        elif "Googlebot" in agente:
            navegador = "Googlebot"
        elif "Feedfetcher" in agente or "FeedBurner" in agente:
            navegador = "Feedfetcher"
        else:
            navegador = "Otros"

        if navegador not in navegadoresContados:
            navegadoresContados[navegador] = 0

        navegadoresContados[navegador] += 1

    # Mostrar resultados en formato JSON
    print(json.dumps(navegadoresContados, indent=4, ensure_ascii=False))





