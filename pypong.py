# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#Ball
ball = pygame.image.load('./images/pypong-image-ball.png').convert()
ball_position_x = 390
ball_position_y = 290
ball_flying_right = False
ball_flying_down = False
ball_rect = pygame.Rect(ball_position_x, ball_position_y, 20, 20)


#Player Paddle
player_paddle =pygame.image.load('./images/pypong-image-player-paddle.png').convert()
player_position_x = 40
player_position_y = 250
player_rect = pygame.Rect(player_position_x, player_position_y, 20, 100)


#Computer Paddle
computer_paddle =pygame.image.load('./images/pypong-image-computer-paddle.png').convert()
computer_position_x = 760
computer_position_y = 250
computer_rect = pygame.Rect(computer_position_x, computer_position_y, 20, 100)

paddle_movement_speed = 15
ball_movement_speed_vertical = 5
ball_movement_speed_horizontal = 9


# score
player_score = 0
computer_score = 0

font = pygame.font.SysFont(None, 24)

def reset_game():
    ball_position_x = 390
    ball_position_y = 290

def ball_hitting_computer_paddle():
    return ball_rect.collidepoint()

def ball_hitting_player_paddle():
    return player_rect.colliderect(ball_rect)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            player_position_y = event.pos[1] - 50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_position_y = player_position_y - paddle_movement_speed
                
            if event.key == pygame.K_DOWN:
                player_position_y = player_position_y + paddle_movement_speed

            if event.key == pygame.K_q:
                running=False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Scores
    player_score_image = font.render(str(player_score), True, (0,0,0))
    computer_score_image = font.render(str(computer_score), True, (0,0,0))

    screen.blit(player_score_image, (20, 20))
    screen.blit(computer_score_image, (760, 20))

    pygame.draw.line(screen, (0,0,0), (400, 0), (400, 600))

    # Ball Flug Logik 
    if ball_flying_right == True:
        ball_position_x = ball_position_x + ball_movement_speed_horizontal
    if ball_flying_right == False:
        ball_position_x = ball_position_x - ball_movement_speed_horizontal
    if ball_flying_down == True:
        ball_position_y = ball_position_y + ball_movement_speed_vertical
    if ball_flying_down == False:
        ball_position_y = ball_position_y - ball_movement_speed_vertical

    # Ball Steuerungslogik
    if ball_position_y <= 0:
        ball_flying_down = True
    if ball_position_y >= 600:
        ball_flying_down = False
    if ball_position_x <= 0:
        ball_flying_right = True
        
    if ball_rect.center[1] > computer_rect.center[1]:
        computer_position_y = computer_position_y + 3
    if ball_rect.center[1] < computer_rect.center[1]:
        computer_position_y = computer_position_y - 3

    if ball_position_x >= 800: # player scored
        player_score = player_score + 1
        ball_flying_right = False
        ball_position_x = 390
        ball_position_y = 290
    if ball_position_x <= 0: # computer scored
        computer_score = computer_score + 1
        ball_flying_right = True
        ball_position_x = 390
        ball_position_y = 290

    ball_rect.left = ball_position_x
    ball_rect.top = ball_position_y
    
    player_rect.left = player_position_x   
    player_rect.top = player_position_y
    
    computer_rect.left = computer_position_x
    computer_rect.top = computer_position_y


    if pygame.Rect.colliderect(ball_rect, player_rect):
        ball_flying_right = True
    if pygame.Rect.colliderect(ball_rect, computer_rect):
        ball_flying_right = False

    # RENDER YOUR GAME HERE
    screen.blit(ball, (ball_position_x, ball_position_y))
    #pygame.draw.rect(screen, "aquamarine", ball_rect,  2)
    screen.blit(player_paddle, (player_position_x, player_position_y))
    #pygame.draw.rect(screen, "aquamarine", player_rect,  2)
    screen.blit(computer_paddle, (computer_position_x, computer_position_y))
    #pygame.draw.rect(screen, "aquamarine", computer_rect,  2)
         
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
    # player wins
    if player_score == 10:
        running = False
        print('Player has won')
    # computer wins
    if computer_score == 10:
        running = False
        print('Computer has won')
        
pygame.quit()
