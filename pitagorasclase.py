import math
 
def opuesto(h,a):
    resultado = math.sqrt((h**2)-(a**2))
    print('El Cateto Opuesto es: ',resultado)
    
def adyacente(h,o):
    resultado = math.sqrt((h**2)-(o**2))
    print('El Cateto Adyacente es: ',resultado)
    
def hipotenusa(o,a):
    resultado = math.sqrt((o**2)+(a**2))
    print('La hipotenusa es: ',resultado)
 
def main():
    print("Teorema de Pitagoras \n1. Cateto Opuesto \n2. Cateto Adyacente \n3. Hipotenusa")
    opc=int(input("Ingese la opcion a calcular: "))
    if opc == 1:
        a = int(input("Cateto Adyacente: "))
        h = int(input("Hipotenusa: "))
        opuesto(h,a)
    elif opc == 2:
        o = int(input("Cateto Opuesto: "))
        h = int(input("Hipotenusa: "))
        adyacente(h,o)
    elif opc==3:
        o = int(input("Cateto Opuesto: "))
        a = int(input("Cateto Adyacente: "))
        hipotenusa(o,a)
    elif opc !=4:
        print("Opcion incorrecta")
        main()
 
main()    