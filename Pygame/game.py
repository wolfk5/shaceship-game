import pygame
import os
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

FPS = 60
VEL = 5
bullet_vel =   7
max_bullets = 3
space_witdh, spaceship_height = 55, 40

yellow_spaceship_image = pygame.image.load(os.path.join('Pygame', 'Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (space_witdh, spaceship_height)),  90)
red_spaceship_image = pygame.image.load(os.path.join('Pygame', 'Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (space_witdh, spaceship_height)),  270)


            

def main():
    red = pygame.Rect(700, 300, space_witdh, spaceship_height)
    yellow = pygame.Rect(100, 300, space_witdh, spaceship_height)
    
    red_bullets = []
    yellow_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    
                    
                if event_key == pygame.K_RCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height/2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
            
        draw_window(red, yellow)
            
    
    pygame.quit()
        
def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER )
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
        yellow.x  -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right
        yellow.x  += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y  -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #down
        yellow.y  += VEL       
        
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #LEFT
        red.x  -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x  += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y  -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #down
        red.y  += VEL
        
        
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if yellow.colliderect(bullet):
            
            yellow_bullets.remove(bullet)
        
if __name__  == "__main__":
    main()
