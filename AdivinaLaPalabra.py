print("---INICIO DEL JUEGO---")
print("Vamos a jugar al ahorcado!")
#resp=input("Quieres jugar?")

from random import choice 
palabras=["gato","perro","pajaro"]
fallidas=[]
acertadas=["p","a"]
vidas=5
juego_terminado=False

#Eleccion de palabra a adivinar
def eleccion(palabras):
    palabra_oculta=choice(palabras)
    return palabra_oculta

#Muestra la letra seleccionada si es correcta o un guion si es incorrecta
def guiones(palabra_oculta):
    lista_ocult=[]
    for l in palabra_oculta:
        if l in acertadas:
            lista_ocult.append(l)
        else:
            lista_ocult.append("-")
    print(lista_ocult)

palabra_oculta = eleccion(palabras) #Asignamos el resultadoa una nueva variable
letras_correctas=len(set(palabra_oculta)) #Contamos cuantas letras correctas tiene la palabra oculta
guiones(palabra_oculta)