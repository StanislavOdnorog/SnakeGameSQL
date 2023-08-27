import time
import pygame

from game_screen import GameScreen
from snake import Snake
from food import Food
from user import User


class Game():
    def __init__(self):
        self.game_screen = GameScreen()
        self.user = User()
        self.screen = self.game_screen.screen

        self.snake = Snake()
        self.food = Food(self.snake)

        self.game_is_on = False
        self.game_screen.start_menu(self)

    def setup_game(self):

        self.user.initialize_database()
        self.user.username = self.game_screen.get_username

        self.game_screen.start_screen(self.snake)
        self.game_screen.draw_borders()
        self.game_screen.update_score(self.user.score)

        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        self.ambient = pygame.mixer.Sound('music/Ambient.mp3')
        self.score = pygame.mixer.Sound('music/Score.mp3')
        self.lost = pygame.mixer.Sound('music/Lost.mp3')

        self.score.set_volume(0.50)
        self.ambient.set_volume(0.20)
        self.lost.set_volume(0.20)

        self.channel1 = pygame.mixer.Channel(0)
        self.channel1.play(self.ambient, -1)

    def end_game(self):
        self.channel1.stop()
        self.score.stop()
        channel2 = pygame.mixer.Channel(0)
        channel2.play(self.lost, -1)

        self.user.save_score_to_db()

        self.screen.clear()
        self.screen.bgcolor("Black")
        self.game_screen.show_final_table(
            self.user.view_record_table(), self.user.score)

        self.screen.exitonclick()
        channel2.stop()

    def is_bumped(self):
        for seg in self.snake.segments[1:]:
            if self.snake.head.distance(seg) < 15:
                self.game_is_on = False

        if abs(self.snake.head.xcor()) > 290 or abs(self.snake.head.ycor()) > 290:
            self.game_is_on = False

    def is_food_consumed(self):
        if self.snake.head.distance(self.food) < 20:
            self.snake.add_segment()
            self.food.move_random(self.snake)

            self.score.play()
            self.user.add_score()
            self.game_screen.update_score(self.user.score)

    def start_game(self):
        if self.game_is_on == False:
            self.game_is_on = True

            self.setup_game()

            while self.game_is_on:
                self.screen.update()
                time.sleep(0.1)
                self.snake.move()
                self.is_food_consumed()
                self.is_bumped()

            self.end_game()


if __name__ == '__main__':
    Game()
