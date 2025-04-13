import pygame
import random
from paddle import Paddle
from ball import Ball
from brick import Brick, MegaBrick, IndestructibleBrick, SpawningBrick



class GameManager:
    def __init__(self, screen_width=600, screen_height=400):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # 3 : 2 aspect ratio
        self.clock = pygame.time.Clock()
        


        # Step 1. Initialize all the game variables and objects
        self.game_running = True
        self.score = 0
        self.level = 1
        self.max_level = 3
        self.coins = 0  # 1 coin = 1 point



        # Step 2. Error handling
        try:
            self.paddle = Paddle(self.screen_width, self.screen_height)
            self.ball = Ball(self.screen_width, self.screen_height)
            self.extra_balls = []
            self.bricks = self.create_bricks()

            # Checks if any object is None
            if not self.paddle or not self.ball or not self.bricks:
                raise ValueError("Failed to initialize game objects, please try again!")
        except Exception as e:
            print("Error: ", e)


    def check_collision(self, ball):
        # 1st possibility (Ball -> Paddle)
        # The idea is that the ball hits the paddle when the xPos is within the Paddle's length and the yPos is within the Paddle's height.
        ball_rect = pygame.Rect(ball.xPos - ball.radius, ball.yPos - ball.radius, ball.radius * 2, ball.radius * 2)
        paddle_rect = pygame.Rect(self.paddle.xPos, self.paddle.yPos, self.paddle.width, self.paddle.height)
        
        if ball_rect.colliderect(paddle_rect):
            ball.speed_y *= -1

            # Make it bounce sideways
            paddle_center = self.paddle.xPos + self.paddle.width / 2
            offset = (self.ball.xPos - paddle_center) / (self.paddle.width / 2)
            ball.speed_x += offset * 2
        

        # 2nd possibility (Ball -> Bricks)
        for brick in self.bricks:

            brick_rect = pygame.Rect(brick.xPos, brick.yPos, brick.width, brick.height)

            if not brick.is_destroyed:
                if ball_rect.colliderect(brick_rect):
                    need_to_spawn = brick.hit(ball.damage)
                    ball.speed_y *= -1

                    if brick.is_destroyed:
                        self.score += brick.score
                        self.coins = self.score  # 1 coin = 1 point

                    
                        if need_to_spawn:
                            # You create more balls into the game
                            new_ball = Ball(self.screen_width, self.screen_height)
                            new_ball.xPos = brick.xPos + brick.width // 2
                            new_ball.yPos = brick.yPos + brick.height // 2

                            self.extra_balls.append(new_ball)

                    break
    

    def create_bricks(self):
        rows = self.level * 2 - 1
        # rows = self.level - 1

        bricks = []
        options = ["Brick", "MegaBrick", "IndestructibleBrick", "SpawningBrick"]
        for row in range(rows):
            for i in range(self.screen_width // 50):
                if self.level == 1:
                    bricks.append(Brick(i * 55, row * 25)) 
                else:
                    chosen_option = random.choice(options)
                    if chosen_option == "Brick":
                        bricks.append(Brick(i * 55, row * 25)) 
                    elif chosen_option == 'MegaBrick':
                        bricks.append(MegaBrick(i * 55, row * 25)) 
                    elif chosen_option == 'SpawningBrick':
                        bricks.append(SpawningBrick(i * 55, row * 25)) 
                    else:
                        bricks.append(IndestructibleBrick(i * 55, row * 25)) 

        return bricks


    def display_message(self, message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))

        self.screen.blit(text, text_rect)

        # Display the score here:
        self.display_score(centered=True)

        pygame.display.flip()
        pygame.time.delay(2000)
    

    def display_score(self, centered=False):
        font = pygame.font.Font(None, 24)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        coins_text = font.render(f"Coins: {self.coins}", True, (0, 0, 0))

        if centered:
            # Center both lines of text under each other
            score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40))
            coins_rect = coins_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 70))
            self.screen.blit(score_text, score_rect)
            self.screen.blit(coins_text, coins_rect)
        else:
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(coins_text, (10, 30))





    def check_end_game(self):
        # 1st possibility: LOSE -> When ball falls off the screen (yPos > screen.height)
        active_balls = []
        all_balls = [self.ball] + self.extra_balls

        for ball in all_balls:
            if ball.yPos <= self.screen_height:
                active_balls.append(ball)

        if not active_balls:
            self.display_message('GAME OVER!')
            self.game_running = False


        # 2nd possibility: WIN -> All bricks are destroyed
        elif all(brick.is_destroyed for brick in self.bricks):
            if self.level == self.max_level:
                self.display_message('YOU WIN')
                self.game_running = False
            
            else:
                self.display_message('LEVEL COMPLETED')
                self.level += 1

                self.paddle = Paddle(self.screen_width, self.screen_height)
                self.ball = Ball(self.screen_width, self.screen_height)
                self.bricks = self.create_bricks()
                



    def start_game(self):
        # Step 3. Main gameplay
        while self.game_running:
            self.screen.fill((255, 255, 255))

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

            # Move the extra balls
            for extra_ball in self.extra_balls:
                extra_ball.move()

            # Check for collision right after the ball moves
            self.check_collision(self.ball)

            # Check collision for the rest of the balls
            for extra_ball in self.extra_balls:
                self.check_collision(extra_ball)


            self.check_end_game()

            if not self.game_running:
                pygame.time.delay(2000)  # Give time for message to appear
                pygame.quit()
                break  # Exit the loop


            self.ball.draw(self.screen)

            # Draw the extra balls
            for extra_ball in self.extra_balls:
                extra_ball.draw(self.screen)

            self.paddle.draw(self.screen)

            for brick in self.bricks:
                brick.draw(self.screen)

            # Display the score
            self.display_score()

            # This refreshes the screen to show the updated animation
            pygame.display.flip()
            self.clock.tick(60)