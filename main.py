import time
import turtle

import paddles

screen = turtle.Screen()


def set_screen():
    screen.setup(height=600, width=800)
    screen.bgcolor("#1A3636")
    screen.title("The classic legend Pong Game")
    screen.listen()
    screen.tracer(0)


set_screen()


def boundary():
    """It creates boundary of the playground."""
    bud = turtle.Turtle()
    bud.hideturtle()
    bud.color("white")
    bud.penup()
    bud.goto(280, 280)
    bud.pendown()
    cords = [(-380, 280), (-380, -280), (380, -280), (380, 280), (-380, 280)]
    for cor in cords:
        bud.goto(cor)


boundary()

is_first_try = 0


def btn_click(x, y):
    global is_first_try
    if -100 <= x <= 100 and -25 <= y <= 25:
        is_first_try += 1
        if is_first_try != 1:
            screen.clear()
        button.clear()
        button.hideturtle()
        win.clear()
        win.hideturtle()
        screen.onscreenclick(None)
        set_screen()
        boundary()
        start_game()


"""Draw button"""
button = turtle.Turtle()
button.hideturtle()
"""Win Turtle"""
win = turtle.Turtle()
win.hideturtle()


def start_btn(x, y):
    button.penup()
    button.color("white")
    button.width(3)
    button.penup()
    button.goto(x, 0)
    button.pendown()
    button_cord = [(x, y), (-x, y), (-x, -y), (x, -y), (x, 0)]
    for cord in button_cord:
        button.goto(cord)


def start_btn_text(text, x, y):
    """Draw button text"""
    button.penup()
    button.goto(-x, -y)
    button.write(text, font=("Courier", 24, "bold"))
    button.hideturtle()
    screen.onscreenclick(btn_click)


start_btn(100, 30)
start_btn_text("Start", 48, 18)
screen.update()


def start_game():
    import ball
    import scoreboard

    ball = ball.Ball()
    scoreboard = scoreboard.Scoreboard()

    l_paddles = paddles.Paddles(-370, 0)
    r_paddles = paddles.Paddles(370, 0)
    screen.onkey(r_paddles.up, "Up")
    screen.onkey(r_paddles.down, "Down")
    screen.onkey(l_paddles.up, "w")
    screen.onkey(l_paddles.down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect paddles collisions
        if l_paddles.ycor() > 220:
            screen.onkey(None, "w")
        else:
            screen.onkey(l_paddles.up, "w")
        if l_paddles.ycor() < -220:
            screen.onkey(None, "s")
        else:
            screen.onkey(l_paddles.down, "s")
        if r_paddles.ycor() > 220:
            screen.onkey(None, "Up")
        else:
            screen.onkey(r_paddles.up, "Up")
        if r_paddles.ycor() < -220:
            screen.onkey(None, "Down")
        else:
            screen.onkey(r_paddles.down, "Down")

        # Detect collision with wall
        if ball.ycor() > 260 or ball.ycor() < -260:
            ball.bounce(y=-1)

        # Detect collision with Paddles
        if ball.xcor() > 350 and ball.distance(r_paddles) < 50 or ball.xcor() < -350 and ball.distance(l_paddles) < 50:
            ball.bounce(x=-1)

        # Detect Right paddle misses of ball
        if ball.xcor() > 390:
            ball.reset_position()
            scoreboard.l_score += 1
            scoreboard.update_score()

        # Detect Left paddle misses of ball
        if ball.xcor() < -390:
            ball.reset_position()
            scoreboard.r_score += 1
            scoreboard.update_score()
        # Check Winner
        if scoreboard.l_score == 10 or scoreboard.r_score == 10:
            screen.onkey(None, "Up")
            screen.onkey(None, "Down")
            screen.onkey(None, "w")
            screen.onkey(None, "s")
            ball.reset()
            l_paddles.reset()
            r_paddles.reset()
            scoreboard.reset()
            win.color("#FDDE55")
            win.penup()
            win.goto(-180, 40)
            if scoreboard.l_score > scoreboard.r_score:
                win.write("🎉Left Player Won🎉", font=("Courier", 24, "bold"))
            else:
                win.write("🎉Right Player Won🎉", font=("Courier", 24, "bold"))
            game_is_on = False
            start_btn(120, 30)
            start_btn_text("Play Again!", 97, 18)


screen.mainloop()
