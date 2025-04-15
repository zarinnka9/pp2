import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button with sound")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

pygame.mixer.init()
sound_effect = pygame.mixer.Sound("electr.wav")  

font = pygame.font.SysFont('Arial', 40)

button1 = pygame.Rect(50, 150, 100, 50)
button2 = pygame.Rect(200, 170, 150, 70)

text1 = "Button 1"
text2 = "Button 2"

button1_clicked = False  

def main():
    global button1_clicked, text2

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    button1_clicked = True
                    text2 = "Clicked Button 1" 
                    sound_effect.play() 

                if button2.collidepoint(event.pos): 
                    text2 = "Clicked Button 2"

        pygame.draw.rect(screen, BLUE, button1)
        pygame.draw.rect(screen, BLUE, button2)

        
        button1_text = font.render(text1, True, WHITE)
        button2_text = font.render(text2, True, WHITE)
        screen.blit(button1_text, (button1.centerx - button1_text.get_width() // 2, button1.centery - button1_text.get_height() // 2))
        screen.blit(button2_text, (button2.centerx - button2_text.get_width() // 2, button2.centery - button2_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
