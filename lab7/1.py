import pygame
import sys
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

mickey_body = pygame.image.load("clock.png").convert_alpha()
right_hand = pygame.image.load("min_hand.png").convert_alpha()  
left_hand = pygame.image.load("sec_hand.png").convert_alpha() 


clock = pygame.time.Clock()
FPS = 60

def rotate_and_blit(image, angle, position):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=position)
    screen.blit(rotated_image, rotated_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = (minute / 60) * 360 - 90
    second_angle = (second / 60) * 360 - 90

    screen.fill((255, 255, 255)) 

    mickey_rect = mickey_body.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(mickey_body, mickey_rect)

    center_point = (WIDTH//2, HEIGHT//2)

    rotate_and_blit(right_hand, minute_angle, center_point)
    rotate_and_blit(left_hand, second_angle, center_point)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()


