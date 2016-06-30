import pygame
# 파이게임 객체 시작
pygame.init()

# 윈도우 해상도 조정
our_screen = pygame.display.set_mode((1000, 500))
 
# 윈도우 이름 부여
pygame.display.set_caption("파이게임")

#색상 값
color_blue = True
colors = (255,255,255)

# 사각형이 그려질 좌표를 변수로 선언
x = 30
y = 30

# 시간
clock = pygame.time.Clock()
# 게임 루프 구현
finish = False
while not finish:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             finish = True

# 사각형 그리기
# 스페이스바를 누르면 색상이 바뀐다.
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        color_blue = not color_blue

    if color_blue:
        colors = (0, 128, 255)
    else: 
        colors = (255,255,255)

# 방향키를 눌러서 사각형을 제어하자.
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    
# 기존 화면에 있는 것을 지워주자
    our_screen.fill((0,0,0))

# pygame.draw.rect(스크린객체, 색깔, 사각형(시작좌표, 크기))
    pygame.draw.rect(our_screen, colors, pygame.Rect(x,y, 60,60))
    pygame.display.flip()

# 초당 60프레임으로.
    clock.tick(60)
