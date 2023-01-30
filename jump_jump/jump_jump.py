import pygame,time,random,types
pygame.init()

screen=pygame.display.set_mode((1000,600))
screen.fill((230,230,230))

block = pygame.image.load('block1.png').convert_alpha()
chess = pygame.image.load('chess.png').convert_alpha()

pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.KEYDOWN)
pygame.event.set_allowed(pygame.KEYUP)
pygame.event.set_allowed(pygame.QUIT)

time_total = 0
count = 0

screen.blit(block, (100, 300))
screen.blit(chess, (182, 240))

pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            time_1 = time.time()
            count = count + 1
            print("count",count)

    if event.type == pygame.KEYUP:
        time_2 = time.time()
        time_total = time_2 - time_1
        pygame.display.flip()
        count = count + 1
        print("count", count)

    distance = time_total * 500

    #刷新屏幕
    if count == 1 or count == 2:
        screen.blit(block, (100, 300))

    if count > 2:
        print("count/4",count%4)
        if count%4 == 0:
            distance_block_1 = random.randint(200, 640)
            screen.fill((230, 230, 230))
            screen.blit(block, (100 + distance_block_1, 300))
            pygame.display.flip()

    if count%4 == 0:
        distance_block = random.randint(200, 640)
        screen.fill((230, 230, 230))
        screen.blit(block,(100+distance_block, 300))
        pygame.display.flip()


    screen.blit(chess,(182+distance, 240))
    pygame.display.flip()