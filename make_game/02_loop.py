import pygame
# 파이게임 객체 시작
pygame.init()

# 윈도우 해상도 조정
our_screen = pygame.display.set_mode((400, 300))
 
# 윈도우 이름 부여
pygame.display.set_caption("파이게임")

#색상 값
color_blue = True
colors = (255,255,255)

# 게임 루프 구현
finish = False
while not finish:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             finish = True

# 사각형 그리기
# pygame.draw.rect(스크린객체, 색깔, 사각형(시작좌표, 크기))
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        color_blue = not color_blue

    if color_blue:
        colors = (0, 128, 255)
    else: 
        colors = (255,255,255)
    pygame.draw.rect(our_screen, colors, pygame.Rect(30,30, 60,60))
    pygame.display.flip()


