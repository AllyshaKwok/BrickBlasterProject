import pygame
import random
from paddle import Paddle
from ball import Ball
from brick import Brick, MegaBrick, IndestructibleBrick

class GameManager:
    def __init__(self, screen_width=600, screen_height=400):
        pygame.init()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # 3 : 2 aspect ratio
        self.clock = pygame.time.Clock()

        # Intialise all the game variables and  objects
        self.game_running = True 
        self.score = 0


        # Error handling
        try:
            self.paddle = Paddle(self.screen_width, self.screen_height)
            self.ball = Ball(self.screen_width, self.screen_height)
            self.bricks = self.create_bricks(4)

            # Checks if any object is None
            if not self.paddle or not self.ball or not self.bricks:
                raise ValueError("Failed to initialise game objects, please try again!")
        except Exception as e:
            print("Error: ", e)


    def draw_text(screen, text, size, x, y, color=(255, 255, 255)):
        font = pygame.font.Font(None, size)  # Use default font
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)


    def check_collision(self):
        if self.paddle.xPos < self.ball.xPos < self.paddle.xPos + self.paddle.width and self.paddle.yPos < self.ball.yPos + self.ball.radius < self.paddle.yPos + self.paddle.height:
            self.ball.speed_y *= -1

        for brick in self.bricks:
            if not brick.is_destroyed:
                if brick.xPos < self.ball.xPos < brick.xPos + brick.width and brick.yPos < self.ball.yPos + self.ball.radius < brick.yPos + brick.height:
                    brick.hit()
                    self.ball.speed_y *= -1

                    if brick.is_destroyed:
                        self.score += brick.score


    def create_bricks(self, rows):
        bricks = []
        options = ["Brick", "MegaBrick", "IndestructibleBrick"]
        for row in range (rows):
            for i in range(self.screen_width // 50):
                chosen_option = random.choice(options)
                if chosen_option == "Brick":
                    bricks.append(Brick(i * 57, row * 25))
                elif chosen_option == "MegaBrick":
                    bricks.append(MegaBrick(i * 57, row * 25))
                else:
                    bricks.append(IndestructibleBrick(i * 57, row * 25))

        return bricks




    def display_message(self, message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))

        self.screen.blit(text, text_rect)

        self.display_score(centred=True)

        pygame.display.flip()
        pygame.time.delay(2000)

    
    
    def display_score(self, centred=False):
        font = pygame.font.Font(None, 24)
        score_text = font.render(f"Score: {self.score}", True, (255, 0, 0))
        
        if centred:
            score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40))
            self.screen.blit(score_text, score_rect)
        else:
            self.screen.blit(score_text, (10, 10))

    
    
    def check_end_game(self):
        # 1st possibility: LOSE -> when ball falls off the screen (yPos > screen.height)
        if self.ball.yPos > self.screen_height:
            self.display_message('GAME OVER!')
            self.game_running = False

        # 2nd possibility: WIN -> All bricks are destroyed
        if all(brick.is_destroyed for brick in self.bricks):
            self.display_message('YOU WIN!')
            self.game_running = False



    def start_game(self):
        while self.game_running:
            self.screen.fill((0, 0, 0)) # Use the RGB value of a colour

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False 
                    pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle.move_left()
            if keys[pygame.K_RIGHT]:
                self.paddle.move_right()
            
            self.ball.move()
            # check for collision right after the ball moves
            self.check_collision()

            self.check_end_game()

            if not self.game_running:
                pygame.quit()

            self.ball.draw(self.screen)
            self.paddle.draw(self.screen)

            for brick in self.bricks:
                brick.draw(self.screen)

            # Display the score
            self.display_score()

            # This refreshes the screen to show the updated animation (calling draw functions must be on top)
            pygame.display.flip()
            self.clock.tick(60)


