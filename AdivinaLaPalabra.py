print("\n---INICIO DEL JUEGO---")
print("Vamos a jugar al ahorcado!")
#resp=input("Quieres jugar?")

from random import choice 
palabras=["gato","aperro","pajaro","araton","iguana"]
fallidas=[]
acertadas=[]
vidas=5
juego_terminado=False

#Eleccion de palabra a adivinar
def eleccion(palabras):
    palabra_oculta=choice(palabras)
    return palabra_oculta

#Muestra la letra seleccionada si es correcta o un guion si es incorrecta
def guiones(palabra_oculta,l):
    lista_ocult=[]
    for l in palabra_oculta:
        if l in acertadas:
            lista_ocult.append(l)
        else:
            lista_ocult.append("-")
    print(lista_ocult)

#Verifica si la letra ingresada es del tipo string, y si se encuentra en la palabra oculta
def verificacion(palabra_oculta,l,vidas):
    cont=0
    if type(l)==str:
        if l in palabra_oculta:
            acertadas.append(l)
            cont+=1
            print(f"Te restan",vidas,"vidas")
        else:
            fallidas.append(l)
            vidas-=1
            print(f"Te restan",vidas,"vidas")
    else:
        print("La letra ingresada no es valida")
        l=input("Ingresa una nueva letra: ")
    return l, cont

palabra_oculta = eleccion(palabras) #Asignamos el resultadoa una nueva variable
letras_correctas=len(set(palabra_oculta)) #Contamos cuantas letras correctas tiene la palabra oculta
print("================================")
print(f"La paralabra que debes adivinar tiene",letras_correctas,"letras correctas")
l=input("Que letra quieres probar? ")
l,cont=verificacion(palabra_oculta,l,vidas)
guiones(palabra_oculta,l)
print(f"Tus letras incorrectas han sido: ",fallidas)