from turtle import Screen, Turtle
from lib.async_wrapper import AsyncWrapper


class GameScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)

    def start_menu(self, game):
        self.text = Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.color("White")
        self.username = self.screen.textinput('', "Как тебя зовут, странник?")
        self.text.write(f"{self.username}, нажми 'пробел' для начала игры!",
                        False, align="Center", font=("Arial", 16, "normal"))
        self.screen.listen()
        self.screen.onkey(game.start_game, "space")
        self.screen.exitonclick()

    @AsyncWrapper.background
    def get_username(self):
        return self.username

    def start_screen(self, snake):
        self.screen.onkey(None, "space")
        # self.screen.onkey(lambda:snake.rotate("Up"), "Up")
        # self.screen.onkey(lambda:snake.rotate("Down"),"Down")
        self.screen.onkey(lambda: snake.rotate("Left"), "Left")
        self.screen.onkey(lambda: snake.rotate("Right"), "Right")

    def update_score(self, score):
        self.text.clear()
        self.text.goto(0, 350)
        self.text.write(f"Очки: {score}", False,
                        align="Center", font=("Arial", 16, "normal"))

    def show_final_table(self, board, score):
        self.text.clear()

        self.text.goto(0, 30)
        self.text.color("White")

        self.text.write("Проиграл", False, align="Center",
                        font=("Arial", 40, "bold"))

        if board == None:
            self.text.goto(0, -50)
            self.text.write(f"Набрано очков: {score}", False, align="Center", font=(
                "Arial", 20, "normal"))

            # self.text.goto(0, -100)
            # self.text.color("Red")
            # self.text.write("Нет доступа к таблице", False, align="Center", font=("Arial", 15, "normal"))
            # self.text.color("White")
        else:
            self.text.goto(0, -10)
            self.text.write(
                f"Набрано очков: {score}", False, align="Center", font=("Arial", 20, "bold"))
            self.text.goto(0, -75)
            self.text.write(f"Таблица рекордсменов:", False,
                            align="Center", font=("Arial", 20, "normal"))

            self.text.goto(0, -250)
            scoreboard = '\n'.join(
                str(x[0] + " : " + str(x[1])) for x in board)
            self.text.write(f"{scoreboard}", False,
                            align="Center", font=("Arial", 20, "normal"))

    def draw_borders(self):

        border = Turtle()
        border.penup()
        border.color("White")
        border.shape(None)
        border.pensize(5)
        x_cor, y_cor = 300, 300
        border.goto(x_cor, y_cor)
        border.pendown()

        for _ in range(2):
            x_cor *= -1
            border.goto(x_cor, y_cor)
            y_cor *= -1
            border.goto(x_cor, y_cor)
            x_cor *= -1
            border.goto(x_cor, y_cor)
            y_cor *= -1
            border.goto(x_cor, y_cor)
        border.hideturtle()
