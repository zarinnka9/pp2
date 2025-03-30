import pygame
import sys

# Инициализация
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Program Extended")
clock = pygame.time.Clock()

# Переменные по умолчанию
radius = 5
color = (0, 0, 255)
tool = "line"  # 'line', 'rect', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'
drawing = False
start_pos = (0, 0)

def draw_rectangle(surface, start, end, color, thickness):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_circle(surface, start, end, color, thickness):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    radius = int((dx ** 2 + dy ** 2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, thickness)

def draw_square(surface, start, end, color, thickness):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start, (side, side))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_right_triangle(surface, start, end, color, thickness):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_equilateral_triangle(surface, start, end, color, thickness):
    side = abs(end[0] - start[0])
    height = (3 ** 0.5 / 2) * side
    points = [start, (start[0] + side, start[1]), (start[0] + side // 2, start[1] - height)]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_rhombus(surface, start, end, color, thickness):
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    points = [(center[0], start[1]), (start[0], center[1]), (center[0], end[1]), (end[0], center[1])]
    pygame.draw.polygon(surface, color, points, thickness)

def main():
    global radius, color, tool, drawing, start_pos

    running = True
    screen.fill((255, 255, 255))  # Белый фон

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Выбор инструмента
                if event.key == pygame.K_1:
                    tool = "line"
                if event.key == pygame.K_2:
                    tool = "rect"
                if event.key == pygame.K_3:
                    tool = "circle"
                if event.key == pygame.K_4:
                    tool = "square"
                if event.key == pygame.K_5:
                    tool = "right_triangle"
                if event.key == pygame.K_6:
                    tool = "equilateral_triangle"
                if event.key == pygame.K_7:
                    tool = "rhombus"
                if event.key == pygame.K_8:
                    tool = "eraser"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    drawing = True
                    start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos

                    if tool == "rect":
                        draw_rectangle(screen, start_pos, end_pos, color, radius)
                    elif tool == "circle":
                        draw_circle(screen, start_pos, end_pos, color, radius)
                    elif tool == "square":
                        draw_square(screen, start_pos, end_pos, color, radius)
                    elif tool == "right_triangle":
                        draw_right_triangle(screen, start_pos, end_pos, color, radius)
                    elif tool == "equilateral_triangle":
                        draw_equilateral_triangle(screen, start_pos, end_pos, color, radius)
                    elif tool == "rhombus":
                        draw_rhombus(screen, start_pos, end_pos, color, radius)

        pygame.display.set_caption(f"Tool: {tool.upper()} | Color: {color} | Radius: {radius}")
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()
