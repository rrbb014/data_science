import pygame

# 파이게임 초기화
pygame.init()

display_width = 1000   # 스크린 사이즈 가로
display_height = 750   # 스크린 사이즈 세로

# 스크린 생성
our_screen = pygame.display.set_mode((display_width, display_height))

myimg = pygame.image.load("csb.jpg")

# 함수 정의
def myimage(x,y):
    our_screen.blit(myimg, (x, y))

# 이미지 출력을 위한 위치 선정
x = (display_width * 0.3)
y = 0


#이벤트 루프 생성
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # 그림을 잘 보이게 하기위해 배경색을 흰색으로!
    our_screen.fill((255,255,200))
    # 이미지를 화면에 표시하는 함수 
    myimage(x,y)
    pygame.display.flip()

pygame.quit()
quit()

