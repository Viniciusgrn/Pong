#install pygame e pywin32

import pygame
import sys



# Inicialização do Pygame
pygame.init()

# Definição de variáveis
WIDTH, HEIGHT = 640, 480
BALL_SPEED = 5
PADDLE_SPEED = 7

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criar a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Inicialização dos objetos do jogo
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
paddle_left = pygame.Rect(50, HEIGHT // 2 - 60, 20, 120)
paddle_right = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 60, 20, 120)

ball_direction = [1, 1]
paddle_left_direction = 0
paddle_right_direction = 0

clock = pygame.time.Clock()

    

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_right_direction = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle_right_direction = PADDLE_SPEED
            elif event.key == pygame.K_w:
                paddle_left_direction = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle_left_direction = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_right_direction = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_left_direction = 0

    # Atualizar a posição da bola
    ball.x += BALL_SPEED * ball_direction[0]
    ball.y += BALL_SPEED * ball_direction[1]

    # Verificar colisões com as paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction[1] *= -1

    # Verificar colisões com as paletas
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_direction[0] *= -1

    # Atualizar a posição das paletas
    paddle_left.y += paddle_left_direction
    paddle_right.y += paddle_right_direction

    # Desenhar os objetos na tela
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros por segundo
    clock.tick(60)







#Coloca som
# from pydub import AudioSegment 
# from pydub.playback import play 
# song = AudioSegment.from_mp3("note.mp3")
# play(song) 