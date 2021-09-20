import pygame, sys# se cargan las librerias
from random import randint

ancho_ventana=640#Ancho en pixeles de la ventana
alto_ventana=600#Alto en pixeles de la ventana
Azul=(20,51,250)
negro=(0,0,0)

##Dibujar el bloque###
def bloque(bloque_x,bloque_y,bloque_ancho,bloque_alto,color):
    pygame.draw.rect(canva,negro,(bloque_inicio_x,bloque_y,bloque_ancho,bloque_alto))
######################

####Inicializar el bloque####
bloque_velocidad=5
bloque_alto=100
bloque_ancho=100
bloque_inicio_x=randint(0,ancho_ventana)
bloque_inicio_y=-bloque_alto

####fin del bloque###########
##Variable que cuenta numero bloques esquivados###
esquivados=0
###Funcion de colision###
def bloque_choca_con_jugador():
    if bloque_inicio_y+bloque_alto>y:
        if (x+imagen_carro.get_width() > bloque_inicio_x and
        x<bloque_inicio_x+bloque_ancho):
            return True
    return False
def crash():
    print("Te has chocado")
    print(f"Has esquivado {esquivados}")
    pygame.quit()
    sys.exit(0)
#########################
def coche(pos_x,pos_y):
    canva.blit(imagen_carro,(pos_x,pos_y))
tiempo=pygame.time.Clock()#Limitar la velocidad del juego
pygame.init() #Inciamos nuestra aplicacion
imagen_carro=pygame.image.load('racecar.png')#Cargar imagen
canva = pygame.display.set_mode((600,400))#Definimos largo y ancho
x=(ancho_ventana-imagen_carro.get_width())//2#Acomodar el carro en la mitad
y=(alto_ventana-imagen_carro.get_height())//1.6#Evitar que se me salga el carro de la pantalla
pygame.display.set_caption("Mi primera ventana de un juego")#Para agregar un titulo
he_chocado=False#Para salir cuando choque o le de en salir
while not he_chocado: #Hacer ciclo para mover
    for evento in pygame.event.get(): #Recorrer una lista de eventos
        incremento_x=0
        if evento.type ==pygame.QUIT: #Si es salir que se salga
            he_chocado=True
            break
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_LEFT:
                incremento_x=incremento_x-5#para que se mueva cada vez que este hundida la pantalla
            if evento.key==pygame.K_RIGHT:
                incremento_x=incremento_x+5 #para que se mueva cada vez que este hundida la pantalla
        if evento.type==pygame.KEYUP:
            if (evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT):#Cuando deje de hundir la tecla
                #no se mueva
                incremento_x=0   
    canva.fill(Azul)
    #Dibujamos el obstaculo
    bloque(bloque_inicio_x,bloque_inicio_y,bloque_ancho,bloque_alto,(0,0,0))
    #Para mostrar el obstaculo en cualquier parte de la ventana
    #Comprar los rangos de x
    if x+incremento_x>=0 and x+incremento_x+imagen_carro.get_width()<ancho_ventana:
        x=x+incremento_x
    #x=x+incremento_x
    ##actualizar elementos del programa####
    bloque_inicio_y+=bloque_velocidad
    if bloque_inicio_y>alto_ventana:
        bloque_inicio_y=-bloque_alto
        bloque_inicio_x=randint(0,ancho_ventana-bloque_ancho)
        bloque_velocidad+=0.1
        esquivados+=1
    ##Comprobar si nos chocamos
    if bloque_choca_con_jugador():
        crash()
        
    coche(x,y)#Recibe la imagen y luego recibe la posicion en pantalla
    pygame.display.update()
    tiempo.tick(60)#Para mostrar 60fps 
pygame.quit() #Para cerrar la ventana
sys.exit(0)#Terminar todos los procesos
