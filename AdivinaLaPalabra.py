print("\n---INICIO DEL JUEGO---")
print("Vamos a jugar al ahorcado!")
#resp=input("Quieres jugar?")

from random import choice 
palabras=["gato","perro","pajaro","raton","iguana"]
fallidas=[]
acertadas=[]
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
            vidas=-1
    print(lista_ocult)

def verificacion(palabra_oculta,l):
    if type(l)==str:
        if l in palabra_oculta:
            acertadas.append(l)
            cont=+1
        else:
            fallidas.append(l)
    else:
        print("La letra ingresada no es valida")
        l=print("Ingresa una nueva letra: ")
        verificacion(l)
    return palabra_oculta

palabra_oculta = eleccion(palabras) #Asignamos el resultadoa una nueva variable
letras_correctas=len(set(palabra_oculta)) #Contamos cuantas letras correctas tiene la palabra oculta
print("================================")
print(f"La paralabra que debes adivinar tiene",letras_correctas,"letras correctas")
l=input("Que letra quieres probar? ")
verificacion(palabra_oculta,l)
guiones(palabra_oculta)
print(f"Te restan",vidas,"vidas")
print(f"Tus letras incorrectas han sido: ",fallidas)