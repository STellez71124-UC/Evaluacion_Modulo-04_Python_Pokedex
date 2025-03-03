# Evaluacion_Modulo-04_Python_Pokedex

REQUISITOS DEL PROGRAMA:
Es necesario tener instaladas las siguientes librerias y módulos para garantizar el funcionamiento del programa Python Pokédex:
1.- Módulo OS: Módulo para hacer uso del sistema operativo y el almacenamiento de la computadora.
2.- Módulo Requests: Módulo para enviar y recibir solicitudes HTTPS por conducto de programas de Python.
3.- Módulo JSON: Módulo para codificar, descodificar y modificar información en formato .json.
4.- Módulo Random: Módulo para introducir factor númerico o de selección pseudo-aleatorio.
5.- Libreria Matplotlib: Medio para llevar a cabo generación y visualización de gráficas o iconografía por medio de Python.
6.- Libreria Matplotlib: Mecanismo por el cual Python puede realizar el manejo de imagenes.
7.- Paquete Urllib: Medio para abrir, leer y trabajar con información almacenada en URLs.

DESARROLLO DEL PROGRAMA:
Evaluación de todos los conocimientos adquiridos anteriormente para generación de Pokédex (Envío de solicitudes a API, y medios para recibir datos de la misma, mostrarlos por medio de texto e imagen, y almacenarlos en el computador).

Para crear este programa se tuvo en consideración parámetros como lo son la cantidad definida de criaturas Pokémon y el posible desconocimiento de la identidad o número de identificacón de ellos por parte del usuario.

En atención a ello, se configuró la entrada de datos de modo que pueda recibir palabras o en su caso números para crear solicitud de información a PokéAPI. En caso de verificarse concordancia de dato ingresado con la base de datos, el proceso continua con normalidad. En caso contrario, se prepara el uso de número aleatorio que sobreescribe solicitud erronea enviada previamente y el proceso se lleva a cabo correctamente. Asimismo, se preveen supuestos de falla de conexión o demora considerable en contactar API, en cuyo caso, se requiere de reinicio manual del programa.

![Captura de pantalla 2025-03-02 222003](https://github.com/user-attachments/assets/704c8d97-2c37-4cfb-81dd-c4fc4ebe7198)

A continuación se presenta formado de diccionario Python, conformado por serie de llaves y espacio receptor de datos por parte de PokéAPI en base a información disponible en formato JSON. Se procede a realizar recopilación automatizada de datos considerados como relevantes y su posterior preparación para generar representación visual de Pokédex a traves del uso de matplotlib y algunas de sus funciones.

Una vez generada la pantalla donde la imagen y exposición acerca del Pokémon seleccionado, el usuario puede cerrar la ventana y el programa de Python verifica y/o crea un folder exclusivo para almacenar archivos JSON donde se reproduce integramente el contenido del diccionario usado en el Pokédex.

-----------------------------

REFLEXIONES DEL BOOTCAMP UTEL - FUNDAMENTOS DE PYTHON C28 - MODULO 04:
Considero que el Bootcamp de Fundamentos de Python me ha brindado oportunidades para desarrollar proyectos personales y contribuir a iniciativas públicas accesibles para principiantes y personas que aún están familiarizandose con el uso adecuado de python. Debido a circunstancias externas, fue necesario abordar el desarrollo del presente proyecto en su manifestación actual en un plazo de dos días, ya que planteamientos anteriores resultaron deficientes y no daban cumplimiento a la intención y objetivos planteados en las instrucciones proporcionadas por la institución. Sin embargo, pienso que el presente trabajo y las condiciones previamente aludidas permitieron tener una aproximación a el compromiso personal y profesional que el programador tiene para cumplir con una determinada tarea satisfactoriamente dentro de una fecha límite cercana.
