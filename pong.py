import pygame, sys
import random

ANCHO_VENTANA   = 640
ALTO_VENTANA    = 480
COLOR_NEGRO     = (  20,  14,   8 )
COLOR_BLANCO    = ( 240, 240, 242 )
COLOR_AMARILLO  = ( 240, 200,  20 )
COLOR_ROJO      = ( 251,  51, 102 )
COLOR_VERDE     = (   0, 255, 153 )
COLOR_AZUL      = ( 102, 255, 255 )

COLOR_FONDO     = COLOR_NEGRO
COLOR_ESCENARIO = COLOR_AMARILLO
COLOR_BOLA      = COLOR_VERDE
COLOR_PALA_1    = COLOR_AZUL
COLOR_PALA_2    = COLOR_ROJO
COLOR_SCORE_1   = COLOR_PALA_1
COLOR_SCORE_2   = COLOR_PALA_2

BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
PADDLE_SPEED = 4

LEFT = False
RIGHT = True

SCORE1_POS = (ANCHO_VENTANA//2 - 70, 50)
SCORE2_POS = (ANCHO_VENTANA//2 + 50, 50)

reloj = pygame.time.Clock()

def draw_text(texto, posicion, color):
  global canvas
  superficie = text_font.render(texto, True, color)
  canvas.blit(superficie, posicion)

def nuevo_juego():
  global pala_1_pos, pala_2_pos, pala_1_incremento_y, pala_2_incremento_y, score_1, score_2
          
  pala_1_pos = [0, ALTO_VENTANA // 2 - HALF_PAD_HEIGHT]
  pala_2_pos = [ANCHO_VENTANA - PAD_WIDTH, ALTO_VENTANA // 2 - HALF_PAD_HEIGHT]
  pala_1_incremento_y = 0
  pala_2_incremento_y = 0
  score_1 = 0
  score_2 = 0

  lanza_bola(RIGHT)

def lanza_bola(direccion):
  global ball_pos, ball_vel
  
  ball_pos = [ANCHO_VENTANA // 2, ALTO_VENTANA // 2]
  x_dir = random.randint(2, 4) # 2 ó 3
  if direccion == LEFT:
    x_dir = -x_dir # -2 ó -3
  ball_vel = [ x_dir, random.randint(-3, -1) ]

def key_down (tecla):
  global pala_1_incremento_y, pala_2_incremento_y
  
  if tecla == pygame.K_w:
    pala_1_incremento_y = -PADDLE_SPEED
    
  if tecla == pygame.K_s:
    pala_1_incremento_y = PADDLE_SPEED

  if tecla == pygame.K_UP:
    pala_2_incremento_y = -PADDLE_SPEED
  if tecla == pygame.K_DOWN:
    pala_2_incremento_y = PADDLE_SPEED
    
def key_up (tecla):
  global pala_1_incremento_y, pala_2_incremento_y
  if tecla == pygame.K_w or tecla == pygame.K_s:
    pala_1_incremento_y = 0
  if tecla == pygame.K_UP or tecla == pygame.K_DOWN:
    pala_2_incremento_y = 0
    
  
def draw():
  global ball_pos, pala_1_pos, pala_2_pos, pala_1_incremento_y, pala_2_incremento_y, score_1, score_2

  # Bola limite derecho
  if ball_pos[0] + BALL_RADIUS > ANCHO_VENTANA - PAD_WIDTH:
    # Bola se ha salido del limite y pierde el jugador 2
    if ball_pos[1] + BALL_RADIUS < pala_2_pos[1] or ball_pos[1] - BALL_RADIUS > pala_2_pos[1] + PAD_HEIGHT:
      score_1 += 1
      lanza_bola(LEFT)
    else:
    # Bola rebota con la pala2
      ball_vel[0] = -ball_vel[0]
      
  # Bola limite izquierdo
  if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
    # Bola se ha salido del limite?
    if ball_pos[1] + BALL_RADIUS < pala_1_pos[1] or ball_pos[1] - BALL_RADIUS > pala_1_pos[1] + PAD_HEIGHT:
      score_2 += 1
      lanza_bola(RIGHT)
    else:
    # Bola rebota con la pala1
      ball_vel[0] = -ball_vel[0]      
      
  # Actualizar posicion de la bola
  ball_pos[0] = ball_pos[0] + ball_vel[0] # x
  ball_pos[1] = ball_pos[1] + ball_vel[1] # y

  # Comprobar límites superior e inferior de la bola y hacer que rebote
  if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= ALTO_VENTANA - BALL_RADIUS:
    ball_vel[1] = -ball_vel[1]

  pala_1_pos[1] += pala_1_incremento_y
  pala_2_pos[1] += pala_2_incremento_y
  
  pygame.draw.line(canvas, COLOR_ESCENARIO,
                   (ANCHO_VENTANA // 2, 0),
                   (ANCHO_VENTANA // 2, ALTO_VENTANA),
                   1)
  
  pygame.draw.line(canvas, COLOR_ESCENARIO,
                   (PAD_WIDTH, 0),
                   (PAD_WIDTH, ALTO_VENTANA),
                   1)

  pygame.draw.line(canvas, COLOR_ESCENARIO,
                   (ANCHO_VENTANA - PAD_WIDTH, 0),
                   (ANCHO_VENTANA - PAD_WIDTH, ALTO_VENTANA),
                   1)

  pygame.draw.rect(canvas, COLOR_PALA_1,
                   (pala_1_pos[0], pala_1_pos[1], PAD_WIDTH, PAD_HEIGHT) )

  pygame.draw.rect(canvas, COLOR_PALA_2,
                   (pala_2_pos[0], pala_2_pos[1], PAD_WIDTH, PAD_HEIGHT) )

  pygame.draw.circle(canvas, COLOR_BOLA,
                     ball_pos,
                     20 )

  draw_text(str(score_1), SCORE1_POS, COLOR_SCORE_1)
  draw_text(str(score_2), SCORE2_POS, COLOR_SCORE_2)

pygame.init()
text_font = pygame.font.SysFont("Arial", 48)


nuevo_juego()

canvas = pygame.display.set_mode ( (ANCHO_VENTANA, ALTO_VENTANA) )
pygame.display.set_caption ('Udemy - Pong')

#######################################################################
#       Bucle de Juego                                                #
#######################################################################
running = True

while running:
  for evento in pygame.event.get():
    #
    # Cierre de ventana
    #
    if evento.type == pygame.QUIT:
      running = False

    if evento.type == pygame.KEYDOWN:
      key_down(evento.key)
      
    if evento.type == pygame.KEYUP:
      key_up(evento.key)

  canvas.fill( COLOR_NEGRO )

  draw()
  
  pygame.display.update()
  
  reloj.tick(60)
  
pygame.quit()
sys.exit(0)
