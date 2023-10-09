import pygame
import numexpr as ne

pygame.init()

screen = pygame.display.set_mode((310, 385))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
calc = []
mathsignban = True
answer = 0

running = True
while running:

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #buttons

        #1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 70 and 100 <= mouse[1] <= 160:
                mathsignban = False
                calc.append('1')

        #2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mouse[0] <= 140 and 100 <= mouse[1] <= 160:
                mathsignban = False
                calc.append('2')

        #3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= mouse[0] <= 210 and 100 <= mouse[1] <= 160:
                mathsignban = False
                calc.append('3')

        #+
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 240 <= mouse[0] <= 300 and 100 <= mouse[1] <= 160 and not mathsignban:
                mathsignban = True
                calc.append('+')

        #4
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 70 and 170 <= mouse[1] <= 230:
                mathsignban = False
                calc.append('4')

        #5
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mouse[0] <= 140 and 170 <= mouse[1] <= 230:
                mathsignban = False
                calc.append('5')

        #6
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= mouse[0] <= 210 and 170 <= mouse[1] <= 230:
                mathsignban = False
                calc.append('6')

        #-
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 240 <= mouse[0] <= 300 and 170 <= mouse[1] <= 230 and not mathsignban:
                mathsignban = True
                calc.append('-')

        #7
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 70 and 240 <= mouse[1] <= 300:
                mathsignban = False
                calc.append('7')

        #8
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mouse[0] <= 140 and 240 <= mouse[1] <= 300:
                mathsignban = False
                calc.append('8')

        #9
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= mouse[0] <= 210 and 240 <= mouse[1] <= 300:
                mathsignban = False
                calc.append('9')

        #*
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 240 <= mouse[0] <= 300 and 240 <= mouse[1] <= 300 and not mathsignban:
                mathsignban = True
                calc.append('*')

        #C
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 70 and 310 <= mouse[1] <= 370:
                mathsignban = True
                calc.clear()
                answer = 0

        #0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 80 <= mouse[0] <= 140 and 310 <= mouse[1] <= 370:
                mathsignban = False
                calc.append('0')

        #=
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 150 <= mouse[0] <= 210 and 310 <= mouse[1] <= 370:
                mathsignban = True

                # result calculation
                try:
                    answer = ne.evaluate(str(calc).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', ''))
                    calc.clear()
                    answers = str(answer)
                    for i in range(len(answers)):
                        calc.append(answers[i])
                except ZeroDivisionError:
                    calc.clear()
                    error = 'Error'
                    for i in range(len(error)):
                        calc.append(error[i])

        #/
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 240 <= mouse[0] <= 300 and 310 <= mouse[1] <= 370 and not mathsignban:
                mathsignban = True
                calc.append('/')

    screen.fill((0, 0, 0))

    # drawing button base

    # 1st row
    pygame.draw.rect(screen, (150, 150, 150), (10, 100, 60, 60), 3)  # 1
    pygame.draw.rect(screen, (150, 150, 150), (80, 100, 60, 60), 3)  # 2
    pygame.draw.rect(screen, (150, 150, 150), (150, 100, 60, 60), 3)  # 3
    pygame.draw.rect(screen, (150, 150, 150), (240, 100, 60, 60), 3)  # +

    # 2nd row
    pygame.draw.rect(screen, (150, 150, 150), (10, 170, 60, 60), 3)  # 4
    pygame.draw.rect(screen, (150, 150, 150), (80, 170, 60, 60), 3)  # 5
    pygame.draw.rect(screen, (150, 150, 150), (150, 170, 60, 60), 3)  # 6
    pygame.draw.rect(screen, (150, 150, 150), (240, 170, 60, 60), 3)  # -

    # 3rd row
    pygame.draw.rect(screen, (150, 150, 150), (10, 240, 60, 60), 3)  # 7
    pygame.draw.rect(screen, (150, 150, 150), (80, 240, 60, 60), 3)  # 8
    pygame.draw.rect(screen, (150, 150, 150), (150, 240, 60, 60), 3)  # 9
    pygame.draw.rect(screen, (150, 150, 150), (240, 240, 60, 60), 3)  # *

    # 4th row
    pygame.draw.rect(screen, (150, 150, 150), (10, 310, 60, 60), 3)  # C
    pygame.draw.rect(screen, (150, 150, 150), (80, 310, 60, 60), 3)  # 0
    pygame.draw.rect(screen, (150, 150, 150), (150, 310, 60, 60), 3)  # =
    pygame.draw.rect(screen, (150, 150, 150), (240, 310, 60, 60), 3)  # /

    # drawing numbers and math signs

    # 1
    text_surface = my_font.render('1', False, (255, 255, 255))
    screen.blit(text_surface, (32, 105))

    # 2
    text_surface = my_font.render('2', False, (255, 255, 255))
    screen.blit(text_surface, (102, 105))

    # 3
    text_surface = my_font.render('3', False, (255, 255, 255))
    screen.blit(text_surface, (172, 105))

    # +
    text_surface = my_font.render('+', False, (255, 255, 255))
    screen.blit(text_surface, (262, 105))

    # 4
    text_surface = my_font.render('4', False, (255, 255, 255))
    screen.blit(text_surface, (32, 175))

    # 5
    text_surface = my_font.render('5', False, (255, 255, 255))
    screen.blit(text_surface, (102, 175))

    # 6
    text_surface = my_font.render('6', False, (255, 255, 255))
    screen.blit(text_surface, (172, 175))

    # -
    text_surface = my_font.render('-', False, (255, 255, 255))
    screen.blit(text_surface, (262, 175))

    # 7
    text_surface = my_font.render('7', False, (255, 255, 255))
    screen.blit(text_surface, (32, 245))

    # 8
    text_surface = my_font.render('8', False, (255, 255, 255))
    screen.blit(text_surface, (102, 245))

    # 9
    text_surface = my_font.render('9', False, (255, 255, 255))
    screen.blit(text_surface, (172, 245))

    # *
    text_surface = my_font.render('*', False, (255, 255, 255))
    screen.blit(text_surface, (262, 245))

    # C
    text_surface = my_font.render('C', False, (255, 255, 255))
    screen.blit(text_surface, (32, 315))

    # 0
    text_surface = my_font.render('0', False, (255, 255, 255))
    screen.blit(text_surface, (102, 315))

    # =
    text_surface = my_font.render('=', False, (255, 255, 255))
    screen.blit(text_surface, (172, 315))

    # /
    text_surface = my_font.render('/', False, (255, 255, 255))
    screen.blit(text_surface, (262, 315))

    #drawing strocke
    pygame.draw.rect(screen, (150, 150, 150), (0, 0, 310, 385), 3)
    pygame.draw.rect(screen, (150, 150, 150), (10, 10, 290, 60), 3)

    #result output
    pushback = 275
    calcr = list(reversed(calc))
    for i in range (len(calc)):
        text_surface = my_font.render(str (*calcr[i]), False, (255, 255, 255))
        screen.blit(text_surface, (pushback, 13))
        pushback -= 15

    pygame.display.update()
    tmp = calc

pygame.quit()
