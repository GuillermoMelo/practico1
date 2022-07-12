import string
#ARCHIVOS A USAR
diccionario="spanish.lst"
provisorio="texto_provisorio.txt"
nueva_frase=""
frase_final=""
final_lista=[]
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
    lista=archivo_provisorio.readlines()
    with open (diccionario, "r", encoding="utf-8") as archivo_diccionario:
        
        # diccionario total es todo el diccionario pasado a una lista
        diccionario_total = archivo_diccionario.readlines()
#modificar lo que sigue
        for palabra in lista:
            lo_encontre=False
            for busqueda in archivo_diccionario:
                if palabra==busqueda:
                    lo_encontre=True
                    break
            final_lista.append(palabra)
    print (lista)
    print (final_lista)
