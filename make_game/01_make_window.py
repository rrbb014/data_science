import pygame
# 파이게임 객체 시작
pygame.init()

# 윈도우 해상도 조정
our_screen = pygame.display.set_mode((400, 300))

# 윈도우 이름 부여
pygame.display.set_caption("파이게임")

# 게임 루프 구현
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        pygame.display.update()

