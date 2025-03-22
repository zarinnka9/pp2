import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH = 400
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GOLD = (255, 223, 0)

# Настройка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer + Coins")
clock = pygame.time.Clock()

# Шрифт для текста
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Счётчик монет
coins_collected = 0

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))  # Простая форма машины
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 80)
        self.speed = 5

    def move(self):
        # Движение влево/вправо по нажатию клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 40:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 40:
            self.rect.move_ip(self.speed, 0)

# Класс препятствия (других машин)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
        self.speed = random.randint(4, 6)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
            self.speed = random.randint(4, 6)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GOLD, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
        self.speed = 4

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        # Сброс позиции, если монета ушла за экран
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

# Игрок, враги и монеты
player = Player()
enemy1 = Enemy()
enemy2 = Enemy()

coin1 = Coin()
coin2 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(enemy1, enemy2)

coins = pygame.sprite.Group()
coins.add(coin1, coin2)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy1, enemy2, coin1, coin2)

# Основной игровой цикл
running = True
while running:
    screen.fill(GRAY)  # Цвет дороги
    pygame.draw.rect(screen, WHITE, (30, 0, 10, HEIGHT))   # Левая полоса
    pygame.draw.rect(screen, WHITE, (WIDTH - 40, 0, 10, HEIGHT))  # Правая полоса

    # Текст очков
    coins_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(coins_text, (WIDTH - 120, 10))

    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение игрока и врагов
    player.move()

    for enemy in enemies:
        enemy.move()

    for coin in coins:
        coin.move()

    # Проверка на столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        game_over = font_big.render("Game Over", True, WHITE)
        screen.blit(game_over, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Проверка на сбор монет
    collected_coins = pygame.sprite.spritecollide(player, coins, dokill=False)
    for coin in collected_coins:
        coins_collected += 1
        coin.reset()

    # Отрисовка всех спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.update()
    clock.tick(FPS)
