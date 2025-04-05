import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

# Commands to push changes to GitHub
# 1. git add .
# 2. git commit -m "Message"
# 3. git push

def draw_text(screen, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)  # Use default font
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def check_collision(ball, paddle, bricks, score):
    if paddle.xPos < ball.xPos < paddle.xPos + paddle.width and paddle.yPos < ball.yPos + ball.radius < paddle.yPos + paddle.height:
        ball.speed_y *= -1

    for brick in bricks:
        if not brick.is_destroyed:
            if brick.xPos < ball.xPos < brick.xPos + brick.width and brick.yPos < ball.yPos + ball.radius < brick.yPos + brick.height:
                brick.is_destroyed = True
                ball.speed_y *1 -1
                score += 1

    return score



def create_bricks(rows, screen_width):
    bricks = []
    for row in range (rows):
        for i in range(screen_width // 50):
            bricks.append(Brick(i * 57, row * 25))

    return bricks

def check_end_game(screen, ball, bricks, screen_width, screen_height):
    game_running = True
    # 1st possibility: LOSE -> when ball falls off the screen (yPos > screen.height)
    if ball.yPos > screen_height:
        display_message(screen, 'GAME OVER!', screen_width, screen_height)
        game_running = False

    # 2nd possibility: WIN -> All bricks are destroyed
    if all(brick.is_destroyed for brick in bricks):
        display_message(screen, 'YOU WIN!', screen_width, screen_height)
        game_running = False

    return game_running

def display_message(screen, message, screen_width, screen_height):
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)


def display_score(screen, score):
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, (255, 0, 0))

    screen.blit(score_text, (10, 10))


def main():
    # Initialise pygame
    pygame.init()
    screen_height = 400
    screen_width = 600
    screen = pygame.display.set_mode((screen_width, screen_height)) # 3 : 2 aspect ratio
    clock = pygame.time.Clock()

    # Intialise all the game variables and  objects
    game_running = True 
    score = 0


    # Error handling
    try:
        paddle = Paddle(screen_width, screen_height)
        ball = Ball(screen_width, screen_height)
        bricks = create_bricks(4, screen_width)

        # Checks if any object is None
        if not paddle or not ball or not bricks:
            raise ValueError("Failed to initialise game objects, please try again!")
    except Exception as e:
        print("Error: ", e)

    while game_running:
        screen.fill((0, 0, 0)) # Use the RGB value of a colour

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False 
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()
        
        ball.move()
        # check for collision right after the ball moves
        score = check_collision(ball, paddle, bricks, score)


        game_running = check_end_game(screen, ball, bricks, screen_width, screen_height)
        if not game_running:
            pygame.quit()

        ball.draw(screen)
        paddle.draw(screen)

        for brick in bricks:
            brick.draw(screen)

        # Display the score
        display_score(screen, score)

        # This refreshes the screen to show the updated animation (calling draw functions must be on top)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()