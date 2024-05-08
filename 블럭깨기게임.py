import pygame
import sys

# 게임에 사용되는 전역변수 정의
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLOCK_SIZE = (30, 30)
BALL_SIZE = (10, 10)

# 블록 클래스 정의
class Block:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect
        self.speed = 2

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# 공 클래스 정의
class Ball:
    def __init__(self, color, rect, speed):
        self.color = color
        self.rect = rect
        self.speed = speed

    def draw(self):
        pygame.draw.ellipse(screen, self.color, self.rect)

# 파이게임 초기화
pygame.init()

# 화면 생성
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Block 인스턴스 생성
blocks = [Block(RED, pygame.Rect(x, 780, *BLOCK_SIZE)) for x in range(0, SCREEN_WIDTH, BLOCK_SIZE[0])]

# Ball 인스턴스 생성
ball = Ball(YELLOW, pygame.Rect(300, 400, *BALL_SIZE), 10)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 화면을 검은색으로 채우고 블록, 공을 그립니다.
    screen.fill(BLACK)
    for block in blocks:
        block.draw()
    ball.draw()

    # 블록을 움직이게 합니다.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blocks[0].rect.centerx -= blocks[0].speed
    elif keys[pygame.K_RIGHT]:
        blocks[0].rect.centerx += blocks[0].speed

    # 공을 움직이게 합니다.
    ball.rect.centery -= ball.speed

    # 공과 블록이 충돌했는지 확인합니다.
    for block in blocks:
        if ball.rect.colliderect(block.rect):
            ball.speed = -ball.speed
            blocks.remove(block)

    # 화면을 업데이트 합니다.
    pygame.display.flip()
