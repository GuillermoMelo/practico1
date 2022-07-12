import string
#ARCHIVOS A USAR
lectura="spanish.lst"
provisorio="texto_provisorio.txt"
nueva_frase=""
#EXCEPCION
try:
    with open(lectura,'r') as archivo:
        for linea in archivo:
            print(end='')
except FileNotFoundError:
    print("No se a encontrado el archivo spanish.lst")
#PROGRAMA PASADO A MINUSCULAS
frase=input("ingrese texto: ").lower()
#QUITAR TILDES
def tildes(frase):
    a,b='áéíóú','aeiou'
    cambio=str.maketrans(a,b)
    nueva_frase=frase.translate(cambio)
    return (nueva_frase)
tildes(frase)
#BUCLE HASTA @FIN
archivo=open(provisorio,'w' , encoding="utf-8")
while frase != "@fin":  
    
    frase=input("ingrese texto: ").lower()
    tildes(frase)
    frase_final=nueva_frase.translate(str.maketrans('','',string.punctuation))
    archivo.write(frase_final + "\n")
archivo.close()
