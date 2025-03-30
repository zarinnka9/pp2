import pygame
import random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Функция рисования сетки шахматного типа
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки на поле
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            for _ in range(food.value):  # Добавляем столько сегментов, сколько стоит еда
                self.body.append(Point(head.x, head.y))
            return True
        return False

# Класс еды с таймером исчезновения
class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.value = random.randint(1, 3)  # Вес еды (насколько увеличится змейка)
        self.timer = pygame.time.get_ticks() + random.randint(3000, 7000)  # Исчезновение через 3-7 секунд

    def draw(self):
        color = [colorGREEN, colorBLUE, colorPURPLE][self.value - 1]  # Цвет еды по весу
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self):
        return pygame.time.get_ticks() > self.timer

FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    draw_grid_chess()
    snake.move()

    if snake.check_collision(food):
        food.spawn()
    elif food.is_expired():  # Если еда пропала, создаем новую
        food.spawn()

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()