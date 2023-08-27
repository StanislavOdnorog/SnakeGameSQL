from random import randint
from turtle import Turtle


class Food(Turtle):

    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.75)
        self.color("red")
        self.speed("fastest")
        self.move_random(snake)

    def move_random(self, snake):

        while True:
            self.coor_x = randint(-270, 270)
            self.coor_x -= (self.coor_x % 20)
            self.coor_y = randint(-270, 270)
            self.coor_y -= (self.coor_y % 20)
            self.goto(self.coor_x, self.coor_y)

            for seg in snake.segments:
                if self.distance(seg) < 20:
                    self.move_random(snake)
                    break

            break
