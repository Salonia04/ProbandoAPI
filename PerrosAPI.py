from asyncore import write
#API DE PERROS
import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")

respuesta= response.json()

with open("archivo.txt", "w") as archivo:
    archivo.write(str(respuesta))
archivo.close



            
