import pygame
import time
import random



"""Также необходимо пользоваться методом init() для инициализации экрана в начале кода"""
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis=pygame.display.set_mode((dis_width,dis_height))
"""Для создания экрана при помощи Pygame нужно воспользоваться функцией display.set_mode()."""

pygame.display.set_caption('Snake game')
""" при помощи функции display.set_caption(), мы вывели заголовок нашего экрана — ‘Snake game"""
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)



def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        #рисуем змею


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    """для сохранения изменений координат x и y  исп  две  переменные: x1_change и y1_change"""

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, dis_height-snake_block)/10.0)*10.0

    while not game_over:#цикл который работает до окончания игры
        while game_close == True:
            dis.fill(blue)
            message("You lost! Press Q-Qiut or C-Play Again", red)

            Your_score(Length_of_snake - 1)
            pygame.display.update(())

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            """на экране  будут отображаться все действия игры из за  функции event.get()"""
            if event.type == pygame.QUIT:
                game_over = True #для закрытия приложения
            """Чтобы передвигать змейку, исп использовать ключевые события из класса KEYDOWN библиотеки Pygame. 
            События K_UP, K_DOWN, K_LEFT, и K_RIGHT заставят змейку двигаться вверх, вниз, влево и вправо соответственно."""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True


        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        """цвет дисплея меняется от черного (по умолчанию) до белого при помощи метода fill()"""

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        """для рисования исп функция draw.rect()"""

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #увеличиваем змею

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)


        pygame.display.update()
        """Метод update() используется для применения каких-либо изменений на экране."""

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    """ и методом quit() для его закрытия в конце"""
    quit()


gameLoop()


