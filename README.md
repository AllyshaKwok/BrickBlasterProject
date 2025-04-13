Game Description:
Brick Blaster is a fast-paced, arcade-style game where players use a paddle to bounce a ball and break through layers of bricks. With simple controls and increasingly challenging levels, the game blends classic gameplay with modern visuals and exciting power-ups. Designed for both casual and competitive players, Brick Blaster delivers a satisfying mix of strategy, reflexes, and fun.



Purpose:
The purpose of a brick blaster game is to challenge the player’s reflexes, coordination, and strategic thinking by having them control a paddle to keep a ball in play while aiming to break all the bricks on the screen. The main goal is to clear each level by destroying every brick using the bouncing ball without letting it fall past the paddle. As the game progresses, the increasing difficulty and differing brick patterns keep the gameplay engaging and dynamic. The game encourages players to aim for high scores, improve their reaction time, and master timing and precision through this nostalgic arcade-style game.



Key features:
A brick blaster game typically involves a player-controlled paddle located at the bottom of the screen, which can be moved left and right to bounce a ball. The objective is to use the ball to break a formation of bricks positioned at the top of the screen. If the ball falls below the paddle, the player loses a life or the game ends. The game features various types of bricks, some of which may require multiple hits to break or may be indestructible. As players progress, they can encounter different levels, each with unique brick layouts and increasing difficulty. A scoring system tracks points based on the number of bricks destroyed. A 'NEXT LEVEL' screen should appear once all of the bricks are destroyed before the player advances to the next level. Once the player has reached the max level, the screen should say 'YOU WIN' before the game ends. In my specific game, these features should be noted:
- Wall = white background
- Ball = red and circular object
- BigBall = green circular object
- StrongBall = yellow circular object
- Paddle = grey, thin rectangular object
- Brick = neon green rectangle
- MegaBrick = orange rectable
- IndestructibleBrick = red rectangle
- SpawningBrick = dark blue rectangle
- PowerUpBrick = light blue rectangle (must be purchased so not yet available)

Prerequisites:
Before running the game, make sure your system meets the following requirements:

1. Python Version
- Python 3.10 or 3.11
- In order to check what your current version of python is, input the following line into your terminal: python --version

Instructions:
To play BrickBlaster, make sure you have the game files and Python installed on your computer. First, download and install Python (version 3.10 or newer is best). Once installed, double-click or open your terminal or command prompt and navigate to the game folder. If you see a folder called venv, double-click the activate file inside it to start the game’s environment (or run the command source venv/bin/activate on Mac/Linux or venv\Scripts\activate on Windows). Then, open the src folder and run the game by double-clicking main.py (if set up with Python), or run it from the terminal with the command python main.py. Once launched, you can use the left and right arrow keys to control the paddle and bounce the ball to break the bricks.

How to play:
1. First, the ball will drop vertically, and you will be required to ensure that the ball hits your paddle. You can move the paddle using the 'left' or 'right' keys in order to ensure the paddle touches the ball. On the first level, there will only be 1 row of the basic brick type.
2. Your aim is to hit the bricks using the ball which is guided by the motion of the paddle, this being controlled by the 'left' and 'right' key movements. 
3. Once you've hit all of the bricks, you will progress to the next level where this process repeats except with bricks of different types and patterns. If the ball falls past your paddle, the game will end and the 'GAME OVER' screen will appear.
4. Once you've completed all 3 levels, you win!

Requirements Reference:
<<<<<<< HEAD
In my first deliverable, I said I would use Object Oriented Programming to create my various game objects (such as the ball, paddle and bricks), which I have done in my game. I also stated that there would be various versions of each game object in order to keep the game interesting and exciting. In my second deliverable, I aimed to create subclasses of the original objects, which I have done in my game for the bricks(IndestructibleBrick, MegaBrick etc), balls (BigBall, StrongBall) and paddles (ExtendedPaddle). I did state in my original deliverable that I would create an option for players to purchase different versions of the game objects however, I was unable to complete this task by the due date and will be implementing those features later on. I did use encapsulation to contain the methods and attributes for each object in order to make the code more scalable and clean so that they could easily be called by their subclasses and used in their own way. For example, the parent class 'Brick' had the attribute 'self.score = 1', whilst the MegaBrick subclass had the same attribute but at a different value, this being 'self.score = 3'. The ball mechanics work successfully as they do move autonomously off the walls, bricks and paddle. The paddle movement also works using the 'left' and 'right' keys, enabling the player to restrict the boundaries of the balls movement. There are also various levels which increase in difficulty, the first level only having one rows of bricks to then having mutltiple rows and types of bricks in the second and third levels. There is also the implementation of unique bricks, such as the 'SpawningBrick' which adds additional balls into the game when hit however, I didn't end up making the design of the brick have the "o" or "+" which I planned in my first deliverable.
=======
In my first deliverable, I said I would use Object Oriented Programming to create my various game objects (such as the ball, paddle and bricks), which I have done in my game. I also stated that there would be various versions of each game object in order to keep the game interesting and exciting. In my second deliverable, I aimed to create subclasses of the original objects, which I have done in my game for the bricks(IndestructibleBrick, MegaBrick etc), balls (BigBall, StrongBall) and paddles (ExtendedPaddle). I did state in my original deliverable that I would create an option for players to purchase different versions of the game objects however, I was unable to complete this task by the due date and will be implementing those features later on. I did use encapsulation to contain the methods and attributes for each object in order to make the code more scalable and clean so that they could easily be called by their subclasses and used in their own way. For example, the parent class 'Brick' had the attribute 'self.score = 1', whilst the MegaBrick subclass had the same attribute but at a different value, this being 'self.score = 3'. The ball mechanics work successfully as they do move autonomously off the walls, bricks and paddle. The paddle movement also works using the 'left' and 'right' keys, enabling the player to restrict the boundaries of the balls movement. There are also various levels which increase in difficulty, the first level only having one rows of bricks to then having mutltiple rows and types of bricks in the second and third levels. There is also the implementation of unique bricks, such as the 'SpawningBrick' which adds additional balls into the game when hit however, I didn't end up making the design of the brick have the "o" or "+" which I planned in my first deliverable.
>>>>>>> 942cf798247162a87df140dcd018e66a75114110
