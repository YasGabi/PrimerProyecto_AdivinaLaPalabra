print("\n---INICIO DEL JUEGO---")
print("Vamos a jugar al ahorcado!")

#Se crean las variables iniciales
from random import choice 
palabras=["gato","perro","pajaro","raton","iguana"]
fallidas=[]
acertadas=[]
vidas=5
cont=0

#Eleccion de palabra a adivinar
def eleccion(palabras):
    palabra_oculta=choice(palabras)
    return palabra_oculta

#Muestra la letra seleccionada si es correcta o un guion si es incorrecta
def guiones(palabra_oculta,l):
    lista_ocult=[]
    for l in palabra_oculta:
        if l.lower() in acertadas:
            lista_ocult.append(l.lower())
        else:
            lista_ocult.append("-")
    print(lista_ocult)

#Verifica si la letra ingresada es del tipo string, y si se encuentra en la palabra oculta
#Resta vidas si es incorrecta, o suma un contador de aciertos si es correcta
def verificacion(palabra_oculta,l,vidas,cont):
    if type(l)==str:
        if l.lower() in palabra_oculta:
            if l.lower() not in acertadas:
                print("======================")
                print("Muy bien!!")
                acertadas.append(l.lower())
                print(f"Te restan",vidas,"vidas")
                cont+=1
        else:
            print("======================")
            print("Fallaste D:")
            fallidas.append(l.lower())
            vidas-=1
            print(f"Te restan",vidas,"vidas")
    else:
        print("La letra ingresada no es valida")
        l=input("Ingresa una nueva letra: ")
    return l, cont, vidas

palabra_oculta = eleccion(palabras) #Asignamos el resultadoa una nueva variable
letras_correctas=len(set(palabra_oculta)) #Contamos cuantas letras correctas tiene la palabra oculta

#Comienza el bucle del juego, se pide la letra al usuario, y se llaman a las funciones
while vidas>0: 
    print("===============================")
    print(f"La paralabra que debes adivinar tiene",letras_correctas,"letras correctas")
    l=input("Que letra quieres probar? ")
    l, cont, vidas=verificacion(palabra_oculta,l,vidas,cont)
    guiones(palabra_oculta,l)
    print(f"Tus letras incorrectas han sido: ",fallidas)

    #A continuacion, las condicionales determinan el restulado del juego y cierran el bucle
    if cont>=letras_correctas:
        print("===============================")
        print("Ganaste!!!")
        print(f"Tu palabra oculta es:",palabra_oculta.upper())
        print("Gracias por jugar!!")
        break
    if vidas==0:
        print("===============================")
        print("Has fallado D:")
        print("Vuelve a intentarlo pronto!")
        break