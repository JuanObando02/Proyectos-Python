# ENTREGA CORTE 1

#CONFUGURACIÓN GRAN PRIX

# funciones
def campos_obligatorios_str(text):
    """
    Revisa que todos los campos de tipo 
    string no estén vacíos
    """
    while True:
        x = input(text)
        if x:
            break
        print("Este es un campo obligatorio, por favor complételo")
    return x

def campos_obligatorios_int(text):
    """
    Revisa que todos los campos de tipo 
    int no estén vacíos
    """
    while True:
        x = input(text)
        if x:
            break
        print("Este es un campo obligatorio, por favor complételo")
    return int(x)

def campos_obligatorios_float(text):
    """
    Revisa que todos los campos de tipo 
    float no estén vacíos
    """
    while True:
        x = input(text)
        if x:
            break
        print("Este es un campo obligatorio, por favor complételo")
        
    return float(x)

def formato_tiempo(segundos):
    """
    Transforma el tiempo en el formato deseado
    """
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos:02.0f}:{segundos_restantes:06.3f}"


# variables iniciales

pais_prix = campos_obligatorios_str("Ingrese el país donde se celebrará el Grand Prix: ")
nombre_prix = campos_obligatorios_str("Ingrese el nombre que sea poner al Grand Prix: ")
longitud_circuito = campos_obligatorios_int("Ingrese la longuitud del circuito en Km: ")
while True:
    vueltas_prix = campos_obligatorios_int("Ingrese la cantidad de vueltas que desea que tenga la competencia: ")
    if 260 <= vueltas_prix*longitud_circuito <= 305:
        break
    print("La distancia total recorrida debe encontrarse entre 260 - 305 Km, por favor ajuste el número de vueltas")
while True:
    pilotos_prix = campos_obligatorios_int("Ingrese la cantidad de pilotos que participarán: ")
    if 0 <= pilotos_prix+1 <= 20: #Cambiar 0 a 10
        break
    print("La cantidad de pilotos no es la adecuada, deben participar entre 10-20 pilotos")


pilotos = []
mejor_pole = None

for i in range(pilotos_prix):
    nombre_piloto = campos_obligatorios_str("Ingrese el Nombre: ")
    numero_piloto = campos_obligatorios_int("Ingrese el Numero: ")
    nombre_equipo = campos_obligatorios_str("Ingrese el nombre del equipo: ")
    tiempo_vuelta = round((campos_obligatorios_float("Ingrese el tiempo de vuelta en segundos: ")), 3)

    informacion_piloto = {
        "Nombre" : nombre_piloto,
        "Numero" : numero_piloto,
        "Equipo" : nombre_equipo,
        "Tiempo vuelta" : tiempo_vuelta,
    }

    

    pilotos.append(informacion_piloto)
    
    for i in pilotos: # siendo i la información de cada piloto en un diccionario
        if mejor_pole == None:
            mejor_pole = i["Tiempo vuelta"]
            pole_provisional = i
            print(f"{pole_provisional["Nombre"]} tiene el pole provisional")
        elif i["Tiempo vuelta"] < mejor_pole:
            mejor_pole = i["Tiempo vuelta"]
            pole_provisional = i # pole_provisional es un diccionario
            print(f"{pole_provisional["Nombre"]} tiene el pole provisional")
    


# mejor_pole = None

# for i in pilotos: # siendo i la información de cada piloto en un diccionario
#     if mejor_pole == None:
#         mejor_pole = i["Tiempo vuelta"]
#     if i["Tiempo vuelta"] < mejor_pole:
#         mejor_pole = i["Tiempo vuelta"]
#         pole_provisional = i # pole_provisional es un diccionario
# print(f"{pole_provisional['Nombre']} tienes el pole provisional")

    # for k,v in i.items(): # me devuelve tuplas de la infromación de un único piloto
    #     if k == "Tiempo vuelta":
    #         if mejor_pole == None:
    #             mejor_pole = v   
    #         elif v < mejor_pole:  #idenfica quién es el mejor pole y lo asigna a la variable pole_provisional #Corregir mayor
    #             mejor_pole = v
    #             pole_provisional = i # pole_provisional es un diccionario
    #             print(f"{pole_provisional['Nombre']} tienes el pole provisional")

# Ganador pole 
pole_provisional_copia = pole_provisional
      
print("---Ganador de la Pole Position---")
tiempo_pole = formato_tiempo(pole_provisional_copia['Tiempo vuelta']) #Modifica el formato del tiempo pero no modifica el dict
velocidad = round((longitud_circuito*vueltas_prix)/(pole_provisional_copia['Tiempo vuelta']/3600),3)
pole_provisional_copia["Tiempo vuelta"] = tiempo_pole
pole_provisional_copia["Velocidad en Km/h"] = velocidad
for i, j in pole_provisional_copia.items():
    print(i,':', j)



# CARRERA
# FALTA EVALUAR QUE NINGUNO SEA MEJOR AL MEJOR POLE; DANNA LO TIENE
print("---Carrera---")
for piloto in pilotos:
    print(f"Nombre: {piloto["Nombre"]}\nNúmero: {piloto["Numero"]}")
    while True:
        piloto["Tiempo promedio"] = round(campos_obligatorios_float("Ingrese el tiempo vuelta: "), 3)
        if float(piloto["Tiempo promedio"]) < float(pole_provisional["Tiempo vuelta"]):
            print("No puede haber un tiempo mejor que el de la Pole Position, ingrese un nuevo tiempo.")
            continue
        else:
            break
    piloto["Vuelta rapida"] = round(campos_obligatorios_float("Ingrese el tiempo de vuelta más rápido en segundos: "), 3)
    piloto["Timepo total"] = piloto['Tiempo promedio'] * vueltas_prix
    piloto["Velocidad promedio"] = (vueltas_prix*longitud_circuito)/piloto["Tiempo total"]
    print(f"El tiempo total de la carrera es de {piloto["Tiempo total"]}, y la velocidad promedio fue {piloto["Velocidad promedio"]} ")
    

# PREMIACIÓN

print(f"Premiación del Grand Prix de {pais_prix} ")
# distancia total recorrida ¿En la carrera? o ¿carrera + clasificación?
distancia_total = round((vueltas_prix * longitud_circuito * pilotos_prix),1)
print(f"La distancia total recorrida fue de {distancia_total}")

primer_lugar = None
segundo_lugar = None
tercer_lugar = None

for piloto in pilotos:
    tiempo_promedio = piloto["Tiempo vuelta"]
    if primer_lugar is None or tiempo_promedio < primer_lugar:
        tercer_lugar = segundo_lugar
        segundo_lugar = primer_lugar
        primer_lugar = tiempo_promedio
    elif segundo_lugar is None or tiempo_promedio < segundo_lugar:
        tercer_lugar = segundo_lugar
        segundo_lugar = tiempo_promedio
    elif tercer_lugar is None or tiempo_promedio < tercer_lugar:
        tercer_lugar = tiempo_promedio

ganador = None
segundo = None
tercero = None

for piloto in pilotos:
    if piloto["Tiempo vuelta"] == primer_lugar:
        ganador = piloto
    elif piloto["Tiempo vuelta"] == segundo_lugar:
        segundo = piloto
    elif piloto["Tiempo vuelta"] == tercer_lugar:
        tercero = piloto

for piloto in pilotos:
    vuelta_rapida = piloto["Tiempo vuelta"]
    if mas_rapido is None or vuelta_rapida < mas_rapido:
        mas_rapido = vuelta_rapida

piloto_rapido = None

for piloto in pilotos:
    if piloto["Tiempo vuelta"] == mas_rapido:
        piloto_rapido = piloto

print(f"El ganador de la carrera es {ganador["Nombre"]} con número {ganador["Numero"]}")
print(f"En segundo lugar quedó {segundo["Nombre"]} con número {segundo["Numero"]}")
print(f"En tercer lugar quedó {tercero["Nombre"]} con número {tercero["Numero"]}")
print(f"El piloto con la vuelta más rápida fue {piloto_rapido["Nombre"]} con número {piloto_rapido["Numero"]}, tomándose {piloto_rapido["Tiempo vuelta"]} a una velocidad de {piloto_rapido["Vuelta rapida"]} km/h")




