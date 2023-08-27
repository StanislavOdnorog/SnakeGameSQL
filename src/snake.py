from turtle import Turtle
START_POSITION = [[0, 0], [-20, 0], [-40, 0]]
SNAKE_SPEED = 20


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, start_position=None):
        segment = Turtle()
        segment.penup()
        segment.shapesize(0.9)
        segment.shape("square")
        segment.color("white")
        if start_position:
            segment.goto(start_position)
        else:
            segment.goto(self.segments[-1].position())
        self.segments.append(segment)

    def create_snake(self):
        for pos in START_POSITION:
            self.add_segment(pos)
        # self.time = time.time()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(SNAKE_SPEED)

    def rotate(self, key):
        if key == "Right":
            self.head.right(45)

        elif key == "Left":
            self.head.left(45)
        # if time.time() - self.time >= 0.005:
            # if key == "Down":
            #     if self.head.heading() != 90.0:
            #         self.head.setheading(270)

            # elif key == "Up":
            #     if self.head.heading() != 270.0:
            #         self.head.setheading(90)

            # elif key == "Right":
            #     if self.head.heading() != 180.0:
            #         self.head.setheading(0)

            # elif key == "Left":
            #     if self.head.heading() != 0.0:
            #         self.head.setheading(180)
        # self.time = time.time()
