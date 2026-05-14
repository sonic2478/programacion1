# Librerias importadas
import string
import requests
import hashlib
from hashlib import sha1
import getpass
import re

numver = []
option = 0
nonfil = []
fil = []
puntglo = 0
while True:
    puntaje = 100
    option = int(input('Elige una opcion: \n' \
    '1. Revisar contraseña \n' \
    '2. Mostrar resumen \n' \
    '3. Salir \n'))
    match option:
        case 1: 
            # Input de la contraseña
            passwd = getpass.getpass('Inserta tu contraseña: \n')
            # Creacion del hash y recorte a los primeros 5 caracteres del hash
            inp = sha1(passwd.encode('utf-8')).hexdigest()
            hash = inp.upper()
            pack = hash[:5]
            rest = hash[5:]
            # Peticion a la API de haveibeenpwned con nuestra contrasena hasheada
            url = f'https://api.pwnedpasswords.com/range/{pack}'

            # Manejo de la respuesta de la API 
            response = requests.get(url)
            pswdlist = response.text
            arr = []
            arr =  pswdlist.splitlines()
            lst = []

            # Algoritmo propio para puntuacion de contrasenas
            dec = [0,1,2,3,4,5,6,7,8,9]
            abc = string.ascii_letters
            specials = string.punctuation

            coincidencias = re.findall(r'(.)\1+', passwd)
            if len(coincidencias) > 0:
                puntaje = puntaje - 10

            if puntaje < 100:     
                if re.search(r'[a-z]', passwd) or re.search(r'[A-Z]', passwd):
                    puntaje = puntaje + 10
                else:
                    puntaje = puntaje - 10
            else:
                puntaje = 100
            if puntaje < 100:
                if re.search(r'[0-9]', passwd):
                    puntaje = puntaje + 10
                else:
                    puntaje = puntaje - 10
            else:
                puntaje = 100
            if puntaje < 100:
                if re.search(r'[^a-zA-Z0-9]', passwd):
                    puntaje = puntaje + 20
            if len(passwd) > 12:
                if puntaje < 100:
                    puntaje = puntaje + 20
            else:
                puntaje = puntaje - 10

            if puntaje > 100:
                puntaje = 100

            # Verificacion para descubrir si la contrasena ha sido filtrada o no
            for e in arr:
                tope =  e.find(':')
                psw = e[:tope]
                lst.append(psw)
                if psw == rest:
                    puntaje = puntaje - 30
                    print(f'Tu contraseña ha sido filtrada {e[tope + 1:]} veces')
                    fil.append(passwd)

            if rest not in lst:
                print(f'Contraseña no filtrada. Felicidades \n')
                nonfil.append(passwd)

            print(f'Tu puntuacion es: {puntaje}')
        case 2: 
            # Hacer la suma de contrasenas filtradas y no filtradas, y sacar el promedio de cada caso
            puntglo = puntglo + puntaje
            prom = puntglo / (len(nonfil)+ len(fil))
            porfil = (len(fil) / (len(fil)+ len(nonfil))) * 100
            pornonfil = (len(nonfil) / (len(fil)+ len(nonfil))) * 100

            print(f'EL total de contrasenas verificadas es de {len(nonfil) + len(fil)} contrasenas')
            print(f'El numero de contrasenas filtradas fue de {len(fil)} contrasenas, dando un porcentaje del {porfil}%')
            print(f'El numero de contrasenas no filtradas fue de {len(nonfil)} contrasenas, dando un porcentaje del {pornonfil}%')

        case 3:
            break