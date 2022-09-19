import random
import time

#Función que crea la sopa de letras
def crea_sopa(nivel):
    
    #Nivel 1
    if nivel==1:
        print("Encuentra las palabras en la sopa de letras\n")
        palabras=["gato","vaca","foca","leon","alce"]
        bandera=True
        while bandera:
            sopa=rellena_sopa_aleatoria(11,11)
            
            sopa_completa=rellena_sopa_palabras(sopa,palabras,11,11)
            
            lista_controladora=sopa_completa[1]
            
            contador=0
            for l in range(len(lista_controladora)-1):
                for k in range(l+1,len(lista_controladora)):
                    if lista_controladora[l]==lista_controladora[k]:
                        contador+=1        
            if contador==0:
                bandera=False
                                                                
        imprime_matriz(sopa_completa[0])
        puntaje=califica_sopa(palabras)

        if puntaje==5:
            puntaje_1=True
        else:
            puntaje_1=False
        
    #Nivel 2
                
    elif nivel==2:
        palabras=["abeja","burro","zorro","cebra","ganso","hiena","lince"]
        bandera=True
        while bandera:
            sopa=rellena_sopa_aleatoria(15,20)
            
            sopa_completa=rellena_sopa_palabras(sopa,palabras,15,20)
            
            lista_controladora=sopa_completa[1]
            
            contador=0
            for l in range(len(lista_controladora)-1):
                for k in range(l+1,len(lista_controladora)):
                    if lista_controladora[l]==lista_controladora[k]:
                        contador+=1
            if contador==0:
                bandera=False
                                                                
        imprime_matriz(sopa_completa[0])
        puntaje=califica_sopa(palabras)
        
        if puntaje==7:
            puntaje_1=True
        else:
            puntaje_1=False

    else:
        palabras=["aguila","bufalo","castor","ciervo","medusa","jaguar","iguana","jirafa"]
        
        bandera=True
        while bandera:
            sopa=rellena_sopa_aleatoria(18,24)
            
            sopa_completa=rellena_sopa_palabras(sopa,palabras,18,24)
            
            lista_controladora=sopa_completa[1]
            
            contador=0
            for l in range(len(lista_controladora)-1):
                for k in range(l+1,len(lista_controladora)):
                    if lista_controladora[l]==lista_controladora[k]:
                        contador+=1
            if contador==0:
                bandera=False
                                                                
        imprime_matriz(sopa_completa[0])
        puntaje=califica_sopa(palabras)
        
        if puntaje==8:
            puntaje_1=True
        else:
            puntaje_1=False
            
    return puntaje_1


#Función que rellena la sopa de letras aleatoriamente

def rellena_sopa_aleatoria(filas,columnas):
    letras="abcdefghijklmnopqrstuvwxyz"
    matriz=[]
    for i in range(filas):
        sublista=[]
        for j in range(columnas):
            x=random.choice(letras)
            sublista.append(x)
        matriz.append(sublista)
    return matriz



#Función que le pone las palabras a la sopa de letras

def rellena_sopa_palabras(sopa_rellena,lista_palabras,filas,columnas):
    lista_control=[]
    for m in range(len(lista_palabras)):
        posicion=random.randint(1,2)
        
        #Verticales
        if posicion==1:
            i=random.randint(0,filas -len(lista_palabras[0]))
            j=random.randint(0,columnas-1)
            for a in range(len(lista_palabras[0])):
                lista_control.append((i+a)*100 + j)
                sopa_rellena[i+a][j]=lista_palabras[m][a]

           #horizontales    
        elif posicion==2:
            i=random.randint(0,filas-1)
            j=random.randint(0,columnas-len(lista_palabras[0]))
            for a in range(len(lista_palabras[0])):
                lista_control.append((i)*100 + j+a)
                sopa_rellena[i][j+a]=lista_palabras[m][a]
                
    return sopa_rellena, lista_control



#Función que califica la sopa de letras

def califica_sopa(lista_palabras):

    print(f"\n Encuentra los {len(lista_palabras)} nombres de animales que estan en el la sopa de letras:")
    print(f"En caso de no encontrar todas las palabras, da enter para omitir")
    aciertos=0    
    for w in range(len(lista_palabras)):
        animal=input(f"Ingresa la palabra {w+1}: ")
        if animal in lista_palabras:
            aciertos+=1
            lista_palabras.remove(animal)
            
    return aciertos


#Función que imprime la matriz

def imprime_matriz(m):
    for lista in m:
        for valor in lista:
            print(valor, end=" ")
            
        print()
        

#Función que imprime listas
def imprime_lista(l):
    for elem in l:
        print(elem, end=" ")
    



#Juego Recuerda palabra
        
def recuerda_palabra(t,n):
    
    print("Recuerda las siguientes palabras: \n")
    lista_juego2=elige_lista(n)
    elemento_agregado=elige_palabra(n)
    imprime_lista(lista_juego2[t-1])
    time.sleep(n+2)
    borra_pantalla()
    lista_juego2[t-1].append(elemento_agregado[t-1])
    random.shuffle(lista_juego2[t-1])
    imprime_lista(lista_juego2[t-1])
    respuesta=input("\n¿Que palabra no estaba en la lista original? ")
    
    if respuesta == elemento_agregado[t-1]:
        print(f"\nCorrecto, {elemento_agregado[t-1]}  no estaba en la lista original")
        puntaje=True
    else:
        print(f"\nIncorrecto, {respuesta}  si estaba en la lista original")
        puntaje=False
        
    return puntaje
    

#Función que elimina de la vista el usuario la lista
def borra_pantalla():
    for i in range(25):
        print()
            
#Función para elegir la lista del conjunto de palabras    
def elige_lista(n):
    
    if n==1:
        lista=[ ["Perro", "Gato", "Ratón", "Borrego"],
                ["Juan", "Hugo", "Lucía", "Elena"],
                ["Alemania", "Perú", "China", "Islandia"]
            ]
        
    elif n==2:
        lista=[ ["Cocodrilo", "Elefante", "Foca", "Venado", "Zebra"],
                ["Laura", "Alicia", "Manuel", "Luis", "Isabel"],
                ["Suecia", "Guatemala", "España", "Canadá", "Dinamarca"]
            ]
    else:
        lista=[ ["Rinoceronte","Mono","Jirafa","Camello","Vivora","Zorro","Tortuga","Oso"],
                ["Diego", "Mariana", "Natalia", "Jorge", "Raquel", "Julio", "Emilio", "Cristian"],
                ["Bélgica", "México", "Nigeria", "Portugal", "Finlandia", "Francia", "Chile", "Ecuador"]
               ]
    return lista


#Función con listas de palabras que se van a agregar

def elige_palabra(n):
    
    if n==1:
        lista=["Jaguar","Pedro","Argentina"]
    
    elif n==2:
        lista=["Caballo","Carla","India"]
    
    else:
        lista=["Orangután","Alison","Rumania"]
        
    return lista


        
#Juego ordena oraciones
            
def ordena_oraciones(n):
    
    print("Se te presentara unas oraciones desordenadas, tendras que ordenarlas \n")
    oraciones=listas_frases(n)
    oracion=oraciones[random.randint(0,2)]
    lista_oracion=oracion.split()
    random.shuffle(lista_oracion)
    imprime_lista(lista_oracion)
    respuesta=input("\nOrdena la oración: ")
    respuesta.lower()
    if respuesta==oracion:
        print("Correcto!!!")
        puntaje=True
    else:
        print("Lo siento, la oración no está ordenada correctamente")
        print(f"La oración deberia quedar así:  \n{oracion}")
        puntaje=False
            
    return puntaje


def listas_frases(n):
    
    if n==1:
        lista_frases=["soy muy inteligente y capaz",
                      "el teléfono negro de mi tía no es moderno",
                      "el león salvaje come tranquilo en la selva",
                    ]
        
    elif n==2:
        lista_frases=["mientras más practiqué mejor me saldrá",
                      "Juan hace su tarea de español en su cuarto",
                      "el niño rompio la ventana con su pelota",
                   ]
    else:
        
        lista_frases=["es importante que siga ejercitando mi cerebro, me traé muchos beneficios",
                      "no me gusta la piel del pulpo",
                      "hallé varios billetes y una joya en la playa",
                   ]
    return lista_frases
        
def lee_nivel():
    
    niveles=[]
    archivo=open("../Programas python/Niveles.txt","r")
    for row in archivo:
        niveles.append(row)
    archivo.close()
    lista=[]
    for recorre in niveles:
        lista.append(recorre.strip())
    
    return lista
    
# Programa principal


menu=1
while menu!=5:
    print("""\n
            MENÚ DE Juegos cognitivos
            1. Sopa de letras
            2. Recuerda la palabra
            3. Ordena la oración
            4. SALIR
        """)
    menu=int(input("Elige una opción: "))
    
    if menu==1:
        print("Elige el nivel de dificultad de la sopa de letras: ")
        print("Recuerda que solo puedes subir de nivel hasta que hayas completado los niveles previos")
        print("1-Nivel 1 \n2-Nivel 2 \n3-Nivel 3")
        level=int(input("Ingresa el número del nivel que deseas: "))
        print("\n")
        nivel_guardado=lee_nivel()
        
        if nivel_guardado[0]=="Nivel 1":
            nivel_numero=1
            
        elif nivel_guardado[0]=="Nivel 2":
            nivel_numero=2

        elif nivel_guardado[0]=="Nivel 3":
            nivel_numero=3
            
        if level<=nivel_numero:
            sopa=crea_sopa(level)
            if sopa:
                print("Felicidades completaste el nivel!!!")
                archivo=open("../Programas python/Niveles.txt","w")
                archivo.write(f"Nivel {level+1}\n")
                archivo.write(f"{nivel_guardado[1]}\n")
                archivo.write(f"{nivel_guardado[2]}\n")
                archivo.close()
            else:
                print("Lo siento te equivocaste")
        
        else:
            print("No puedes jugar este nivel porque no has completado los niveles previos")
            
        
    elif menu==2:
        tematica=int(input("¿De que temática quieres las palabras?\n1. Animales\n2. Nombres de personas\n3. Países\n Elección: "))
        print("Elige el nivel de dificultad del juego recordar palabras")
        print("Recuerda que solo puedes subir de nivel hasta que hayas completado los niveles previos")
        print("1-Nivel 1 \n2-Nivel 2 \n3-Nivel 3")
        level=int(input("Ingresa el número del nivel que deseas: "))
        print("\n")
        nivel_guardado=lee_nivel()
        
        if nivel_guardado[1]=="Nivel 1":
            nivel_numero=1
            
        elif nivel_guardado[1]=="Nivel 2":
            nivel_numero=2

        elif nivel_guardado[1]=="Nivel 3":
            nivel_numero=3
            
        if level<=nivel_numero:
            
            juego_recuerda=recuerda_palabra(tematica,level)
            
            if juego_recuerda:
                
                print("Felicidades completaste el nivel!!!")
                archivo=open("../Programas python/Niveles.txt","w")
                archivo.write(f"{nivel_guardado[0]}\n")
                archivo.write(f"Nivel {level+1}\n")
                archivo.write(f"{nivel_guardado[2]}\n")
                archivo.close()                
        
        else:

            print("No puedes jugar este nivel porque no has completado los niveles previos")        
        
        
    elif menu==3:
        print("Elige el nivel de dificultad del juego ordena oraciones")
        print("Recuerda que solo puedes subir de nivel hasta que hayas completado los niveles previos")
        print("1-Nivel 1 \n2-Nivel 2 \n3-Nivel 3")
        level=int(input("Ingresa el número del nivel que deseas: "))
        print("\n")
        nivel_guardado=lee_nivel()
        
        if nivel_guardado[2]=="Nivel 1":
            nivel_numero=1
            
        elif nivel_guardado[2]=="Nivel 2":
            nivel_numero=2

        elif nivel_guardado[2] =="Nivel 3":
            nivel_numero=3
            
        if level<=nivel_numero:
            
            juego_ordena=ordena_oraciones(level)
            
            if juego_ordena:
                
                print("Felicidades completaste el nivel!!!")
                archivo=open("../Programas python/Niveles.txt","w")
                archivo.write(f"{nivel_guardado[0]}\n")
                archivo.write(f"{nivel_guardado[2]}\n")
                archivo.write(f"Nivel {level+1}\n")
                archivo.close()
                

        else:

            print("No puedes jugar este nivel porque no has completado los niveles previos") 
        

    elif menu==4:
        
        print("Gracias por su visita, recuerde seguir ejercitando su cerebro. Lo está haciendo muy bien, vuelva pronto.")  
   
    else:
        print("La opción que eligió no está dentro de nuestro menú")  