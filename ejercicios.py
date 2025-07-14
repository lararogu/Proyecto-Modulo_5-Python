# 1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados
lista="cadena de letras"

def count_letras(texto):
    """
    Esta función recoge un texto y cuenta la frecuencia de cada letra
    
    Args:
        texto (string)
   """ 
    dic={}
    for i in texto:
        if i==" ":
            #Si el valor es un espacio, saltamos a la siguiente iteracion
            continue
        else:
            dic.update({i:texto.count(i)})

    return dic

print(count_letras(lista))

# 2.Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
lista=[1,2,3,4]
lista_doble=list(map(lambda x:x*2, lista))


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
lista_palabras=["hola mundo", "que tal estas", "mi casa"]
palabra="mundo"
def encontrar_palabra(lista_palabras, palabra):
    """
        Esta función recoge una lista de palabras y una palabra objetivo y devuelve una lista
        con las palabras que contienen la palabra objetivo
    Args:
        Lista de palabras y palabra objetivo
    """
    palabras_encontradas = []
    for i in lista_palabras:
        if palabra in i:
            palabras_encontradas.append(i)
 
    return palabras_encontradas

encontrar_palabra(lista_palabras, palabra)

# 4.Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
lista1=[1,4,5]
lista2=[1,3,2]
def diferencia(a, b):
  return [item for item in a if item not in b]

list(map(diferencia, lista1,lista2))

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.
lista=[2, 8, 6]

def calcular_media(lista, nota_aprobado=5):
    """
    Esta función calcula la media de una lista de notas e indica el estado (aprobado/suspenso)
    
    Args:
        lista de notas, nota_aprobado
   """
    suma=0
    tupla=()
    for i in lista:
        suma+=i
    media=suma/len(lista)
    
    if media>=nota_aprobado:
        tupla=(media, "aprobado")
    else:
        tupla=(media, "suspenso")
    
    return tupla

print(calcular_media(lista))
#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def calcular_factorial(numero):
    if numero<0:
        return None
    elif numero==0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
tuple=("a","b","c","d")      
string=list(map(lambda tupla: str(tupla),tuple))
print(string)
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.
try:
    # Solicitamos al usuario que ingrese un número y lo convertimos a entero.
    num1 = int(input("Ingrese un número: "))
    # Mostramos por pantalla el número ingresado por el usuario.
    print("El primer número ingresado por el usuario es:", num1)    
    num2 = int(input("Ingrese un número: "))
    print("El segundo número ingresado por el usuario es:", num2)    
    resultado=num1/num2
# Capturamos el error en caso de que el usuario ingrese un valor no válido (por ejemplo, una letra).
except ValueError:
    print("Por favor, ingrese un número válido.")   
# Capturamos el error en caso de que el usuario ingrese 0 como divisor, lo cual es inválido.
except ZeroDivisionError:
    print("No se puede dividir entre cero.")  
else:
    print("El resultado de la división es:", round(resultado,2))
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
lista=["Perro", "Cocodrilo", "Tortuga"]

def identificar_animal(lista):
    lista_prohibida=["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
    return lista not in lista_prohibida

nueva_lista=list(filter(identificar_animal,lista))
print(nueva_lista)

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.
lista=[1,5,4]

def calcular_promedio(lista):
    """
    Suma todos los elementos de la lista y divide el total de la suma entre la longitud de la lista. Si la longitud de la lista es cero, salta una excepcion.
    """
    suma=0
    try:
        for i in lista:
            suma+=i
        media=suma/len(lista)
        print(f"El promedio es:{media}")
    except ZeroDivisionError:
        print("No se puede calcular el promedio. La lista esta vacia")


calcular_promedio(lista)

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
try:
    # Solicitamos al usuario que ingrese un número y lo convertimos a entero.
    edad = int(input("Ingrese su edad: "))  
   
# Capturamos el error en caso de que el usuario ingrese un valor no válido (por ejemplo, una letra).
except ValueError:
    print("Por favor, ingrese un número válido.")   
 
else:
    if edad < 0 or edad > 120:
        print("La edad introducida no es valida")
    else:
        # Mostramos por pantalla el número ingresado por el usuario. 
        print(f"Tu edad es {edad} años")

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def calcular_long_frase(frase):
    palabras = frase.split()
    longitudes = [len(palabra) for palabra in palabras]
    return longitudes
frase="esto es una frase"
print (calcular_long_frase(frase))
#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
caracteres=['i','o','p']
def devuelve_mayus_minus(caracteres):
    caracteres2=[]
    for i in caracteres:
        caracteres2.append(i.upper())
        caracteres2.append(i.lower())
    return caracteres2

print(tuple(map(devuelve_mayus_minus,caracteres)))
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()
palabras=["casa", "autobus","alfabeto", "oso"]
palabras_filtro=list(filter(lambda x:True if x[0]=="a" else False, palabras))
print(palabras_filtro)
#15. Crea una función lambda que sume 3 a cada número de una lista dada.
lista=[1,4,5]
suma=lambda lista: [item+3 for item in lista]

print(suma(lista))
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()
texto="esto es una cadena de texto"
n=7

def analizar_inicio_palabra (texto, n):
    palabras = texto.split()
    for i in palabras:
        if len(i)>n:
            return True
        else:
            return False
    
filter(analizar_inicio_palabra, texto, n)
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()
from functools import reduce
digitos=[2,4,6]
reduce(lambda x,y:x*10 + y,digitos)

#18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
#90. Usa la función filter()
nombres=["Carlos", "Ana", "Maria", "Pepe"]
edades=["19", "20", "19", "22"]
calificaciones=["70", "55", "93", "66"]
def crear_diccionario(nombres, edades, calificaciones):
    lista_dic=[]
    diccionario={}
    for nombre,edad,nota in zip(nombres,edades,calificaciones):
        diccionario.update({"nombre":nombre,"edad":edad,"calificacion":nota})
        lista_dic.append(diccionario)
    return lista_dic

mi_diccionario=crear_diccionario(nombres, edades, calificaciones)

filter(list(lambda dic:True if dic["calificacion"] >90 else False, mi_diccionario))

#19.Crea una función lambda que filtre los números impares de una lista dada.
lista_numeros=[3, 8, 6, 5]
print(list(filter(lambda x: True if x%2 !=0 else False, lista_numeros)))

#20.Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
#filter()
print(list(filter(lambda x: True if type(x)==int else False, lista)))
#21.Crea una función que calcule el cubo de un número dado mediante una función lambda
valor_al_cubo=lambda x:x**3
valor_al_cubo(5)
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce
numeros=[3, 8, 6, 5]
reduce(lambda x,y:x*y, numeros)

#23. Concatena una lista de palabras.Usa la función reduce()
from functools import reduce

def unir_iterables(valor):
    str=""
    str.join(valor)
    return str

lista=["Esto","es","un","curso","online"]
lista_concatenada=reduce(unir_iterables,lista)
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()
from functools import reduce
numeros=[3, 8, 6, 5]
reduce(lambda x,y:x-y, numeros)
#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
texto="esto es una cadena de texto"
def contar_longitud(texto):
    palabras = texto.split()
    longitud=0
    for i in palabras:
        long+=len(i)
    return longitud

contar_longitud(texto)

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
division=lambda x,y: x%y
division(5,3)
#27. Crea una función que calcule el promedio de una lista de números.
def calcular_media(lista):
    total=0
    for i in lista:
      total+=i
    media=total/len(lista)
    return media

lista=[1,2,3]
calcular_media(lista)
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def encontrar_duplicado(lista):
    duplicados=[]
    for i in lista:
            if i in duplicados:
                return i
            else:
                duplicados.append(i)

lista=[1,2, 5, 4, 2, 8, 3,5]
encontrar_duplicado(lista)
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los
#caracteres con el carácter '#', excepto los últimos cuatro.
cadena_texto=556778
def convertir_cadena(cadena_texto):
    cadena=str(cadena_texto)
    return "#" * (len(cadena)-4) + cadena[-4:]

convertir_cadena(cadena_texto)

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.
str1="amor"
str2="mora"
def anagramas(str1, str2):
    for i in str1:
       if str2.find(i)==-1:
            #Si devuelve -1 significa que no ha encontrado el caracter en el segundo string
            print("Las palabras no son anagramas")
            return False
       else:
           continue
    
    print("Las palabras son anagramas")
    return True

anagramas(str1, str2)

#31.Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.
nombres=[]
nombres_total=3
for i in range(nombres_total):
    # Solicitamos el nombre al usuario
    nombre = input(f"Ingresa el nombre {i + 1}: ")
    # Lo agregamos a la lista
    nombres.append(nombre)

nombre_buscado = input(f"Ingresa un nombre para buscar en la lista anterior: ")

if nombre_buscado in nombres:
    print(" El nombre buscado esta en la lista")

else:
    raise ValueError("El nombre buscado no esta en la lista")


#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.
def buscar_empleado (nombre, lista):
    for i in lista:
        if i==nombre:
            print("El puesto del empleado es",lista.index(i))
            return lista.index(i)
        else:
            continue
    print(f"El empleado con nombre",{nombre}, "no trabaja aqui")

lista=["Jose Perez", "Ana Silva", "David Gutierrez"]
nombre="David Gutierrez"
buscar_empleado (nombre, lista)

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista1=[1,2, 5, 4, 2, 8, 3,5]
lista2=[1,4, 6, 4, 2, 1, 3,2]

suma = lambda lista1,lista2 : [a + b for a, b in zip(lista1, lista2)]


#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
class Arbol:
    def __init__(self, tronco):
        self.tronco=tronco
        self.rama=[]
    def crecer_tronco(self, unidades):
        self.tronco+=unidades

    def nueva_rama(self):
       self.rama.insert(len(self.rama)-1, 1)

    def crecer_ramas(self):
        for i in range(len(self.rama)):
            self.rama[i]+=1


    def quitar_rama(self, posicion_rama):
        self.rama.pop(posicion_rama)

    def info_arbol(self):
        print (f"El arbol tiene los siguientes datos: Longitud tronco={self.tronco}, Numero Ramas={len(self.rama)}, Longitud ramas={self.rama}")

mi_arbol=Arbol(5)
mi_arbol.crecer_tronco(1)
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)
mi_arbol.info_arbol()

#36.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#agregar dinero al saldo.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre=nombre
        self.saldo=saldo
        self.cuenta_corriente=cuenta_corriente
    def retirar_dinero(self, cantidad):
        if self.saldo<cantidad:
            print("La cuenta no tiene suficiente saldo")
            return ValueError
        else:
            self.saldo-=cantidad

    def transferir_dinero(self, cantidad, usuario_origen):
       if usuario_origen.retirar_dinero(cantidad) ==ValueError:
           print("No ha sido posible realizar la transferencia")
       else:
           self.saldo+=cantidad
           usuario_origen.retirar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
       self.saldo+=cantidad

#1. Creacion de usuarios
Alicia=UsuarioBanco("Alicia", 100, True)
Bob=UsuarioBanco("Bob", 50, True)
#2. Agregar 20 unidades de saldo de "Bob".
Bob.agregar_dinero(20)
#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
Alicia.transferir_dinero(80, Bob)
#4. Retirar 50 unidades de saldo a "Alicia".
Alicia.retirar_dinero(50)

#37.Cea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#de la función procesar_texto .
def contar_palabras(texto):
    diccionario={}
    palabras = texto.split()
    for i in palabras:
        diccionario.update({i:palabras.count(i)})
    return diccionario

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    texto.replace(palabra_original, palabra_nueva)
    return texto

def eliminar_palabras(texto, palabra_eliminar):
    diccionario={}
    palabras = texto.split()
    palabras.pop(palabras.index(palabra_eliminar))
    return palabras


def procesar_texto(texto, funcion,*palabras):

   """
    Esta función procesa un texto con varias funciones posibles
    
    Args:
        texto (string)
        funcion: contar, eliminar o reemplazar
        argumentos variables (palabras) segun la funcion elegida
   """  
   if funcion =="contar":
      print("contando")
      return contar_palabras(texto)
   elif funcion == "reemplazar":
      palabra_original=palabras[0] 
      palabra_nueva=palabras[1]
      return reemplazar_palabras(texto,palabra_original, palabra_nueva)
   elif funcion=="eliminar":
      return eliminar_palabras(texto, palabras)
   else:
      "No se ha indicado ninguna funcion valida"

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
try:
    # Solicitamos al usuario que ingrese una hora
    hora = int(input("Ingrese la hora del dia con el formato hh: "))  
   
# Capturamos el error en caso de que el usuario ingrese un valor no válido (por ejemplo, una letra).
except ValueError:
    print("Por favor, ingrese un valor válido.")   
 
else:
    if 0 < hora < 7:
        print("Es de madrugada")
    elif 7 < hora < 12:
        print("Es la mañana")
    elif 12 < hora < 20:
        print("Es la tarde")
    elif 20 < hora < 24:
        print("Es la noche")
    else:
        print("Por favor, ingrese una hora en el formato correcto")  
#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
def obtener_calificacion(nota):
    if 0 < nota < 69:
        print (" La calificacion es: Insuficiente")
    elif 70 <nota <79:
        print (" La calificacion es: Bien")
    elif 80 <nota <89:
        print (" La calificacion es: Muy bien")
    elif 90 <nota <100:
        print (" La calificacion es: Excelent")
    else:
        print("Introduce una calificacion valida entre 0 y 100")

#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def calcular_area (figura, datos):
    if figura=="rectangulo":
        area=datos[0]*datos[1]
        return area
    elif figura=="triangulo":
        area=datos[0]*datos[1]
        return area
    elif figura=="circulo":
        area=math.pi* datos[0]**2
        return area
    else:
        print("No se ha indicado un valor de figura correcto")


#41.En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento
#1. Solicita al usuario que ingrese el precio original de un artículo.
precio_original = int(input("Ingresa el precio original del articulo"))
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
descuento = input("Indica si tienes un cupon de descuento (si/no)")
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
if descuento=="si":
    valor_descuento = int(input("Indica el valor del cupon de descuento"))
elif descuento=="no":
    valor_descuento =0
else:
    print("Por favor, introduce una respuesta valida")
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#a cero). Por ejemplo, descuento de 15€.
if valor_descuento>0:
    precio_final=precio_original-valor_descuento
else:
    precio_final=precio_original
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.

print(f"El precio final de tu compra es:{precio_final} euros")
