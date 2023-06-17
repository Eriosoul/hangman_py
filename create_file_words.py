import requests
import os

url = "https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/master/0_palabras_todas_no_conjugaciones.txt"
r = requests.get(url)
if r.status_code == 200:
    palabras = r.text.splitlines()  # Divide el contenido por líneas
    palabras_con_coma = ['"' + palabra + '",' for palabra in palabras]  # Agrega comillas y coma a cada palabra

    try:
        with open("words.py", "w", encoding="utf-8") as file:
            file.write("\n".join(palabras_con_coma))  # Escribe las palabras con comas separadas por líneas
        print("Archivo guardado exitosamente.")
    except IOError:
        print("Error al abrir o escribir en el archivo.")
else:
    print("Error al descargar el contenido desde la URL.")
