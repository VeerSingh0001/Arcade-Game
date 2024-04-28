import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.draw_line()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def draw_line(self):
        self.goto(0, 280)
        self.setheading(270)
        self.pensize(2)
        while self.ycor() > -283:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)

    def update_score(self):
        self.clear()
        self.draw_line()
        self.goto(-100, 217)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(100, 217)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))
