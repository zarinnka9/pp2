import pygame
import sys

pygame.init()

WIDTH, 













































import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Interaction with Sound")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Загрузка звука
pygame.mixer.init()
sound_effect = pygame.mixer.Sound("your_sound_file.wav")  # Укажите путь к вашему звуковому файлу

# Шрифты
font = pygame.font.SysFont('Arial', 40)

# Кнопки
button1 = pygame.Rect(100, 250, 200, 100)
button2 = pygame.Rect(500, 250, 200, 100)

# Тексты кнопок
text1 = "Button 1"
text2 = "Button 2"

# Статус кнопки
button1_clicked = False  # Определяет, была ли нажата кнопка 1

# Основной игровой цикл
def main():
    global button1_clicked, text2

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)  # Фон

        # Проверка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    button1_clicked = True
                    text2 = "Clicked Button 1"  # Изменяем текст на второй кнопке
                    sound_effect.play()  # Воспроизводим звук

                if button2.collidepoint(event.pos):
                    text2 = "Clicked Button 2"  # Вы можете оставить текст измененным, если хотите

        # Отображаем кнопки
        pygame.draw.rect(screen, BLUE, button1)
        pygame.draw.rect(screen, BLUE, button2)

        # Отображаем текст на кнопках
        button1_text = font.render(text1, True, WHITE)
        button2_text = font.render(text2, True, WHITE)
        screen.blit(button1_text, (button1.centerx - button1_text.get_width() // 2, button1.centery - button1_text.get_height() // 2))
        screen.blit(button2_text, (button2.centerx - button2_text.get_width() // 2, button2.centery - button2_text.get_height() // 2))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Запуск игры
if __name__ == "__main__":
    main()




















import pygame
import sys
 
pygame.init()

WIDTH = 500
HEIGHT = 300
screen = pygame.display.set_sode((WIDTH, HEIGHT))
pygame.display.set_caption("SOMETHINS")

WHITE = (255, 255, 255)

rec_x, rec_y= 100,100

clock = pygame.time.Clock()
def main():
    global rec_x, rec_y

    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                running = False

    






pygame.draw.rect(screen, RED, (rect_x, rect_y, 100, 60))\

pygame.display.flip()
clock.tick(60)
pygame.quit
sys.exit()
    


import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Between Rectangle and Circle")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Переменные для прямоугольника
rect_x, rect_y = 100, 100
rect_speed_x, rect_speed_y = 5, 5

# Переменные для круга
circle_x, circle_y = 400, 300
circle_speed_x, circle_speed_y = 3, 3
circle_radius = 40

# Часы для контроля частоты кадров
clock = pygame.time.Clock()

def main():
    global rect_x, rect_y, circle_x, circle_y, rect_speed_x, rect_speed_y, circle_speed_x, circle_speed_y

    # Главный цикл игры
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление координат прямоугольника и круга
        rect_x += rect_speed_x
        rect_y += rect_speed_y
        circle_x += circle_speed_x
        circle_y += circle_speed_y

        # Проверка столкновения между прямоугольником и кругом
        distance = ((rect_x - circle_x) ** 2 + (rect_y - circle_y) ** 2) ** 0.5
        if distance < circle_radius + 50:  # 50 - половина ширины прямоугольника
            # Меняем направление движения объектов
            rect_speed_x = -rect_speed_x
            rect_speed_y = -rect_speed_y
            circle_speed_x = -circle_speed_x
            circle_speed_y = -circle_speed_y

        # Обработка столкновений с границами экрана для прямоугольника и круга
        if rect_x > 800 - 100 or rect_x < 0:
            rect_speed_x = -rect_speed_x
        if rect_y > 600 - 60 or rect_y < 0:
            rect_speed_y = -rect_speed_y

        if circle_x > 800 - circle_radius or circle_x < circle_radius:
            circle_speed_x = -circle_speed_x
        if circle_y > 600 - circle_radius or circle_y < circle_radius:
            circle_speed_y = -circle_speed_y

        # Отображение
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (rect_x, rect_y, 100, 60))
        pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()







import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определяем размеры экрана и создаем окно
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Click Example")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Звук
pygame.mixer.init()
click_sound = pygame.mixer.Sound("click_sound.wav")  # Путь к файлу с звуком

# Шрифты
font = pygame.font.SysFont('Arial', 50)

# Кнопки
button1 = pygame.Rect(100, 250, 200, 100)
button2 = pygame.Rect(500, 250, 200, 100)

# Тексты
text1 = "Click Me 1"
text2 = "Click Me 2"
current_text = "Press a Button"

# Фон
background_color = WHITE

# Основной игровой цикл
def main():
    global current_text, background_color

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(background_color)  # Фон

        # Проверка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    current_text = "Button 1 Pressed"
                    background_color = RED
                    click_sound.play()  # Воспроизведение звука
                elif button2.collidepoint(event.pos):
                    current_text = "Button 2 Pressed"
                    background_color = GREEN
                    click_sound.play()  # Воспроизведение звука

        # Отображаем кнопки
        pygame.draw.rect(screen, BLUE, button1)
        pygame.draw.rect(screen, BLUE, button2)

        # Отображаем текст на кнопках
        button1_text = font.render(text1, True, WHITE)
        button2_text = font.render(text2, True, WHITE)
        screen.blit(button1_text, (button1.centerx - button1_text.get_width() // 2, button1.centery - button1_text.get_height() // 2))
        screen.blit(button2_text, (button2.centerx - button2_text.get_width() // 2, button2.centery - button2_text.get_height() // 2))

        # Отображаем текущий текст
        current_text_render = font.render(current_text, True, BLACK)
        screen.blit(current_text_render, (WIDTH // 2 - current_text_render.get_width() // 2, HEIGHT - 100))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Запуск игры
if __name__ == "__main__":
    main()
