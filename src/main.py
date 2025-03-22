import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

def main():
    # Initialise pygame
    pygame.init()
    screen_height = 400
    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_height)) # 3 : 2 aspect ratio
    clock = pygame.time.Clock()


    # Intialise all the game objects
    game_running = True 
    paddle = Paddle(screen_width, screen_height)
    ball = Ball(screen_width, screen_height)

    bricks = []
    for i in range(screen_width // 50):
        bricks.append(Brick(i * 57, 0))


    while game_running:
        screen.fill((0, 0, 0)) # Use the RGB value of a colour

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()
        
        ball.move()
        ball.draw(screen)
        paddle.draw(screen)

        for brick in bricks:
            brick.draw(screen)

        # This refreshes the screen to show the updated animation (calling draw functions must be on top)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()