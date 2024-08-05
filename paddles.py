import turtle

screen = turtle.Screen()


class Paddles(turtle.Turtle):

    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.x = x_cord
        self.y = y_cord
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(self.x, self.y)

    def up(self):
        self.y += 20
        self.goto(self.x, self.y)
        screen.update()

    def down(self):
        self.y -= 20
        self.goto(self.x, self.y)
        screen.update()
