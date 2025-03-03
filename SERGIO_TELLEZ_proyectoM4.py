import os #Libreria para manejo de archivos y uso de directorios..
import requests # Libreria para mandar solicitudes a API.
import json #Libreria para leer y escribir archivos JSON.
import random # Libreria ára realizar operaciones con factor aleatorio.
import matplotlib.pyplot as plt #Creación de entrada Pokédex con imagén y texto.
from PIL import Image # Se utiliza para cargar y abrir imagenes.
from urllib.request import urlopen #Carga de imagenes disponibles en internet.

estabilidad = 0 #Parámetro de control

while estabilidad <1: #Parámetro de control: Entrada de datos
    creatura = input("¿Que Pokémon deseas buscar? (Nombre / ID) > ").strip().lower() #Entrada de número o palabra por el usuario.
    try:
        busqueda = int(creatura) #Mecanismo para detectar números escritos por el usuario.
        if busqueda in range (1,1026): #Rango operativo en base a Pokémones disponibles en base de datos.
            estabilidad += 1 #Continuación de proceso.
        if not busqueda in range (1,1026): #Detección de error en rango operativo (Números)
            print ("Escribe un número entero entre 1 y 1025.")
    except ValueError:
        if creatura.isalpha and len(creatura) >= 3: #Mecanismo para detectar datos proporcionados por el usuario.
            estabilidad += 1 #Continuación de proceso.
        else: #Detección de error en rango operativo (Letras)
            print ("Escribe un nombre o número por favor.")

while estabilidad <2: #Parámetro de control: Solicitud de información a PokéAPI.
    print ("Enviando solicitud a PokéAPI.")
    try:
        url = (f"https://pokeapi.co/api/v2/pokemon/{creatura}") #Primer intento de conexión a API con dato ingresado.
        conexion = requests.get(url, timeout=(5), verify=True) #Verificación de conexión segura y tiempo de espera de 5 segundos.
        conexion.raise_for_status() #Declaración de estatus HTTP.
        if conexion.status_code == 200: # Contacto exitoso con API.
            print (f"Recopilando datos de Pokédex. Preparando archivos. Código HTTP: {conexion.status_code}\n")
            estabilidad +=1 #Continuación de proceso.
    except requests.exceptions.ReadTimeout as errrt: #Excepción generada al no poder contactar API dentro de tiempo previsto.
        print("No se pudo establecer contacto con PokéAPI a tiempo. Por favor reinicie el programa.")
        exit() 
    except requests.exceptions.ConnectionError as conerr: #Excepción generada al no poder contactar API a causa de conexión a Internet.
        print("Error de conexión. Por favor reinicie el programa.")
        exit() 
    except requests.exceptions.RequestException as reqerr: #Excepción generada al no existir término dentro de API. 
        print(f"{creatura} no existe en la base de datos: {reqerr}")
        print("Realizando selección aleatoria de Pokémon.\n") #Reinicio automatizado de operación en base a catálogo de API.
        num_aleatorio = random.randint(1,1025) #Selección de número aleatorio
        creatura = num_aleatorio
        url = (f"https://pokeapi.co/api/v2/pokemon/{creatura}") #Definición de nueva URL funcional.
        conexion = requests.get(url, timeout=(5), verify=True)
        estabilidad += 1 #Continuación de proceso.
        print (url)
        
while estabilidad == 2:
    guardar = conexion.json() #Detección y reconocimiento de todos los datos disponibles dentro de página API.
    captura_pokemon = { #Definición y selección de datos relevantes de un único pokémon.
        "ID": guardar["id"], # Inicio de carga de datos generales en apartado individual y/o lista.
        "Nombre": guardar["name"],
        "Altura": guardar["height"],
        "Peso": guardar["weight"],
        "HP": guardar["stats"][0]["base_stat"],
        "Ataque": guardar["stats"][1]["base_stat"],
        "Defensa": guardar["stats"][2]["base_stat"],
        "Ataque Especial": guardar["stats"][3]["base_stat"],
        "Defensa Especial": guardar["stats"][4]["base_stat"],
        "Velocidad": guardar["stats"][5]["base_stat"],
        "Tipos": [data_type["type"]["name"] for data_type in guardar["types"]],
        "Experiencia Base": guardar["base_experience"],
        "Movimientos": [data_mov["move"]["name"] for data_mov in guardar["moves"]],
        "Habilidades": [data_skill["ability"]["name"] for data_skill in guardar["abilities"]], # Fin de carga de datos generales.
        "Imagen": guardar["sprites"]["front_default"] #Carga de imagen de Pokémon seleccionado.
    }

    plt.title(f"Entrada de Pokédex < ID: {captura_pokemon['ID']} >") #Inicio de generación de presentación visual de Pokédex.
    imgplot = plt.imshow(Image.open(urlopen(captura_pokemon["Imagen"]))) #Preparación de imagen de Pokémon
    plt.grid(False)
    plt.axis(False) #Eliminación de lineas usadas en gráficas.
    descripcion =( #Estructura comprehensible de todos los datos capturados. Aplicación de mayúsculas y unión de texto en listas. 
        f"Nombre: {captura_pokemon["Nombre"].title()} | Tipos: {', '.join(captura_pokemon["Tipos"]).title()}\n"
        f"Altura: {captura_pokemon["Altura"]} decimetros | Peso: {captura_pokemon["Peso"]} hectogramos  | EXP: {captura_pokemon['Experiencia Base']}\n"
        f"HP: {captura_pokemon["HP"]} | ATK: {captura_pokemon["Ataque"]} | DEF: {captura_pokemon["Defensa"]} | SP. ATK: {captura_pokemon['Ataque Especial']} | SP. DEF: {captura_pokemon["Defensa Especial"]} | SPD: {captura_pokemon['Velocidad']}\n"
        f"Movimientos: {', '.join(random.sample(captura_pokemon ["Movimientos"], 4)).title()} \n" #Selección aleatoria de cuatro movimientos.
        f"Habilidades: {', '.join(captura_pokemon["Habilidades"]).title()}"
    )
    #Formato de cuadros de texto en relación a imagen.
    plt.text(46, 94, descripcion, fontsize=11, bbox={'facecolor':'white','alpha':1,'edgecolor':'none','pad':1}, ha='center', va='center')
    plt.show() #Presentación de página visual Pokédex generada con código Python.

    print (descripcion) #Presentación de datos generados en terminal Python.
    os.makedirs("Pokedex", exist_ok=True) #Detección y/o creación de folder para almacenar información obtenida de API.
    almacenamiento = os.path.join("Pokedex", f"{captura_pokemon["ID"]} {captura_pokemon["Nombre"]}.json") #Vinculación a folder Pokédex.
    with open(almacenamiento, "w") as resultado:
        json.dump(captura_pokemon, resultado, indent=4) #Creacion de archivo individual de JSON para un Pokémon en especifico.
    print("\nEntrada de Pokédex creada exitosamente.")
    print(f"Archivo disponible en {almacenamiento}") #Confirmación de ejecución del programa
    conexion = requests.post(url=url, headers={'Connection':'close'}) #Conexión deshabilitada con API al finalizar el programa.
    exit() #Cierre del programa para su posible reinicio manual o cerrar editor de Python.
