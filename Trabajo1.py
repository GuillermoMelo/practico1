import string
#ARCHIVOS A USAR
diccionario="spanish.lst"
provisorio="texto_provisorio.txt"
nueva_frase=""
frase_final=""
final_lista=[]
conteo=0
#EXCEPCION
try:
    with open(diccionario,'r') as archivo:
        for linea in archivo:
            print(end='')
except FileNotFoundError:
    print("No se a encontrado el archivo spanish.lst")
#PROGRAMA PASADO A MINUSCULAS
frase=input("ingrese texto: ").lower()
#QUITAR TILDES
def borrar_tildes(frase):
    a,b='áéíóú','aeiou'
    cambio=str.maketrans(a,b)
    nueva_frase=frase.translate(cambio)
    return (nueva_frase)
nueva_frase=borrar_tildes(frase)
##PRIMERA ETAPA##
#BUCLE HASTA @FIN
archivo=open(provisorio,'w' , encoding="utf-8")
while frase != "@fin":  
    frase_final=nueva_frase.translate(str.maketrans('','',string.punctuation))
    archivo.write(frase_final + "\n")
    frase=input("ingrese texto: ").lower()
    nueva_frase=borrar_tildes(frase)
archivo.close()
#CAMBIO DE FORMATO Y BUSQUEDA
with open (provisorio,"r", encoding="utf-8") as archivo_provisorio:
     #lista es archivo provisorio pasado a una lista
    lista2=archivo_provisorio.read()
    lista=lista2.split()
    with open (diccionario, "r", encoding="utf-8") as archivo_diccionario:
        
        # diccionario total es todo el diccionario pasado a una lista
        diccionario_total2= archivo_diccionario.read()
        diccionario_total=diccionario_total2.split()
       #print(diccionario_total)
        
for palabra in lista:
    if palabra not in final_lista:
        if palabra not in diccionario_total:
            conteo += 1
            final_lista.append(palabra)
            print(final_lista)
for elem in final_lista:
    print(f"las palabras que no estan en el diccionario son: {conteo} y son: {elem}")
pregunta=input("desea agregarlas: S/n")
if pregunta == "s":
    with open (diccionario,"a", encoding="utf-8") as agregado:
        diccionario_total.append(final_lista)
elif pregunta == "si":
    with open (diccionario,"a", encoding="utf-8") as agregado:
        diccionario_total.append(final_lista)
elif pregunta == "n":
    print ("gracias")
elif pregunta == "no":
    print("gracias")
else:
    print("respuesta erronea")
    pregunta=input("desea agregarlas: S/n")
