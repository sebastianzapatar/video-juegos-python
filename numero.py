#Importar las librerias
import pygame,sys

#Definir tamonio de la pantalla
ancho_ventana=640
alto_ventana=480
COLOR_NEGRO=(10,10,10)
COLOR_LINEA=(250,250,250)
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS=20
PADDLE_SPEED=4
def draw():
    pygame.draw.line(canva, COLOR_LINEA,
                   (ancho_ventana // 2, 0),
                   (ancho_ventana // 2, alto_ventana),
                   1)
    pygame.draw.line(canva, COLOR_LINEA,
                   (PAD_WIDTH, 0),
                   (PAD_WIDTH , alto_ventana),
                   1)
    pygame.draw.line(canva, COLOR_LINEA,
                   (ancho_ventana-PAD_WIDTH, 0),
                   (ancho_ventana-PAD_WIDTH , alto_ventana),
                   1)
    pygame.draw.rect(canva,COLOR_LINEA,
    (pala_1_pos[0],pala_1_pos[1],PAD_WIDTH,PAD_HEIGHT))
    pygame.draw.rect(canva,COLOR_LINEA,
    (pala_2_pos[0],pala_2_pos[1],PAD_WIDTH,PAD_HEIGHT))
    pygame.draw.circle(canva,COLOR_LINEA,(ancho_ventana//2,alto_ventana//2),BALL_RADIUS)
canva=pygame.display.set_mode((ancho_ventana,alto_ventana))
pygame.display.set_caption("Pong")
def nuevo_juego():
    global pala_1_pos,pala_2_pos,pala_2_incremento_y,pala_1_incremento_y
    pala_1_pos=[0,alto_ventana//2-PAD_HEIGHT//2]
    pala_2_pos=[ancho_ventana-PAD_WIDTH,alto_ventana//2-PAD_HEIGHT//2]
    pala_1_incremento_y=0
    pala_2_incremento_y=0
nuevo_juego()
#Reloj para definir tasa de refresco
reloj=pygame.time.Clock()
salir=False
while not salir:
    ###Cierre ventana
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            salir=True
            break
    canva.fill(COLOR_NEGRO)
    draw()
    pygame.display.update()
    #Definir la velocidad de refresco en 60fps
    reloj.tick(60)
pygame.quit()
sys.exit(0)
    