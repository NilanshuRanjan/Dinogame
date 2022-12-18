import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 500
screen = pygame.display.set_mode((600, 360))

bg = pygame.image.load("dinog\\bg2.jpg")
dore = pygame.image.load("space invaders\\dinosaur.png")
bullet = pygame.image.load("space invaders\\d1.png").convert_alpha()

player_x = 260
player_y = 198


box_x = 50

m_r = False
m_l = False

t = 0
v = 0.5
m = 0.0005
s = False
jump = False
activate = True
bg_width = bg.get_width()
tiles = int(600 / bg_width) + 1
scroll = 0

print(tiles)

timestop = False
while activate:

    #clock.tick(fps)

    obstacle = pygame.Rect(box_x, 230, 30, 30)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            activate = False
        if events.type == pygame.KEYDOWN:
            
            if events.key == pygame.K_RIGHT:
                m_r = True
            if events.key == pygame.K_LEFT:
                m_l = True
            if events.key == pygame.K_SPACE:
                if jump is False:
                    jump = True
            if events.key == pygame.K_t:
                timestop = True
            if events.key == pygame.K_DOWN:
                s = True
        if events.type == pygame.KEYUP:
            
            if events.key == pygame.K_RIGHT:
                m_r = False
            if events.key == pygame.K_LEFT:
                m_l = False
            if events.key == pygame.K_t:
                timestop = False
            if events.key == pygame.K_DOWN:
                s = False
    if timestop:
        pygame.time.delay(2)
    if m_r:
        player_x += 0.3
    if m_l:
        player_x -= 0.3

    if jump:
        player_y -= v
        v -= 0.0012
        if v < -0.5:
            jump = False
            v = 0.5
            player_y = 198
    
    for i in range(0, tiles):
        screen.blit(bg, (i*bg_width+scroll, 0))

    scroll -= 0.2

    if abs(scroll)>bg_width:
        scroll = 0 
    """
    pygame.draw.rect(screen, (0, 0, 0), obstacle, 4)

    
    if box_x >= 600:
        if timestop:
            pygame.time.delay(20)
        box_x -= 0.3
    if box_x < 600:
        box_x = 600
    """
    
    if s:
        screen.blit(bullet, (player_x, player_y + 32))
        p = pygame.Rect(player_x, player_y+32, bullet.get_width(), bullet.get_height())
    if not s:
        screen.blit(dore, (player_x, player_y))
        p = pygame.Rect(player_x, player_y, dore.get_width(), dore.get_height())

    if p.colliderect(obstacle):
        pygame.draw.rect(screen, (255, 0, 0), p, 4)
        # box_x = 0
        # print("gameover")

    
    pygame.display.update()

























