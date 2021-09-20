from random import randint#es generar un aleatorio entre dos numeros 
nombre=input("Ingrese el nombre \t")
numero=randint(1,100)#Genera numero entre 1 y 100
adivina=False

for i in range(0,6):#Para dar 6 oportunidadaes
    intento=int(input("Ingrese el valor o adivine \t"))#es pedir el intento
    if intento==numero:#Si acierta que muestre y se salga
        print(f"{nombre} acerto con el valor y es {numero}")
        adivina=True
        break
    if numero>intento:
        print(f"{nombre} el numero es mayor que {intento}")
    else:
        print(f"{nombre} el numero es menor que {intento}")
if not adivina:
    print(f"{nombre} no acerto y el numero es {numero}")