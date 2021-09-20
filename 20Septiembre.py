#Importar las librerias
import pygame,sys
from random import randint
#Definir tamonio de la pantalla
ancho_ventana=640
alto_ventana=480
COLOR_NEGRO=(10,10,10)
COLOR_LINEA=(250,250,250)
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS=20
PADDLE_SPEED=-4
LEFT=False
RIGHT=True
score_1=0
score_2=0
SCORE1_POS=(ancho_ventana//2-70,50)
SCORE2_POS=(ancho_ventana//2+70,50)
def draw_text(texto,posicion,color=COLOR_LINEA):
    global canva
    superficie=text_font.render(texto,True,color)
    canva.blit(superficie,posicion)
def lanza_bola(direccion):
  global ball_pos, ball_vel
  
  ball_pos = [ancho_ventana // 2, alto_ventana // 2]
  x_dir = randint(2, 4) # 2 ó 3
  if direccion == LEFT:
    x_dir = -x_dir # -2 ó -3
  ball_vel = [ x_dir, randint(-3, -1) ]
def draw():
    global ball_pos, pala_1_pos, pala_2_pos, pala_1_incremento_y, pala_2_incremento_y,score_1,score_2
    #Actualizar posiciones de mis poterias
    pala_1_pos[1] += pala_1_incremento_y
    pala_2_pos[1] += pala_2_incremento_y
    #Si la pelota choca con la pared:
    if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=alto_ventana-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]

    #Actualizar la posicion de la pelota
    
    ball_pos[0] = ball_pos[0] + ball_vel[0] # x
    ball_pos[1] = ball_pos[1] + ball_vel[1] # y

    #Preguntar si la pelota entra en la poteria o rebota
    if ball_pos[0] + BALL_RADIUS > ancho_ventana - PAD_WIDTH:
    # Bola se ha salido del limite y pierde el jugador 2
        if ball_pos[1] + BALL_RADIUS < pala_2_pos[1] or ball_pos[1] - BALL_RADIUS > pala_2_pos[1] + PAD_HEIGHT:
            score_1+=1
            print("Jugador 1",score_1)
            lanza_bola(LEFT)
        else:
    # Bola rebota con la pala2
            ball_vel[0] = -ball_vel[0]
    # Bola limite izquierdo
    if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
        # Bola se ha salido del limite?
        if ball_pos[1] + BALL_RADIUS < pala_1_pos[1] or ball_pos[1] - BALL_RADIUS > pala_1_pos[1] + PAD_HEIGHT:
            score_2+=1
            print("Jugador 2",score_2)
            lanza_bola(RIGHT)
        else:
    # Bola rebota con la pala1
            ball_vel[0] = -ball_vel[0] 
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
    pygame.draw.circle(canva, COLOR_LINEA,
                     ball_pos,
                     20 )
    draw_text(str(score_1),SCORE1_POS)
    draw_text(str(score_2),SCORE2_POS)
canva=pygame.display.set_mode((ancho_ventana,alto_ventana))
pygame.display.set_caption("Pong")

def key_up(tecla):
    global pala_2_incremento_y,pala_1_incremento_y
    if tecla==pygame.K_w or pygame.K_s:
        pala_1_incremento_y=0
    if tecla==pygame.K_UP or tecla==pygame.K_DOWN:
        pala_2_incremento_y=0
def key_down(tecla):
    global pala_2_incremento_y,pala_1_incremento_y
    if tecla==pygame.K_w:
        pala_1_incremento_y=PADDLE_SPEED
    if tecla==pygame.K_s:
        pala_1_incremento_y=-PADDLE_SPEED
    if tecla==pygame.K_UP:
        pala_2_incremento_y=PADDLE_SPEED
    if tecla==pygame.K_DOWN:
        pala_2_incremento_y=-PADDLE_SPEED
def nuevo_juego():
    global pala_1_pos,pala_2_pos,pala_2_incremento_y,pala_1_incremento_y,score_1,score_2
    pala_1_pos=[0,alto_ventana//2-PAD_HEIGHT//2]
    pala_2_pos=[ancho_ventana-PAD_WIDTH,alto_ventana//2-PAD_HEIGHT//2]
    pala_1_incremento_y=0
    pala_2_incremento_y=0
    score_1=0
    score_2=0
    lanza_bola(RIGHT)
nuevo_juego()
pygame.init()
text_font=pygame.font.SysFont("Arial",40)
#Reloj para definir tasa de refresco
reloj=pygame.time.Clock()
salir=False
while not salir:
    ###Cierre ventana
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            salir=True
            break
        if evento.type==pygame.KEYDOWN:
            key_down(evento.key)
        if evento.type==pygame.KEYUP:
            key_up(evento.key)
    canva.fill(COLOR_NEGRO)
    draw()
    pygame.display.update()
    #Definir la velocidad de refresco en 60fps
    reloj.tick(60)
pygame.quit()
sys.exit(0)
    