import time
import turtle
import paddles

screen = turtle.Screen()
ball = ""
scoreboard = ""
l_paddles = ""
r_paddles = ""


def set_screen():
    screen.setup(height=730, width=820)
    screen.bgcolor("#1A3636")
    screen.title("The Arcade Game")
    screen.listen()
    screen.tracer(0)


set_screen()


def boundary():
    """It creates boundary of the playground."""
    bud = turtle.Turtle()
    bud.hideturtle()
    bud.color("white")
    bud.penup()
    bud.goto(280, 290)
    bud.pendown()
    cords = [(-380, 290), (-380, -290), (380, -290), (380, 290), (-380, 290)]
    for cor in cords:
        bud.goto(cor)


boundary()

left_user = ""
right_user = ""


def player_names():
    global left_user, right_user
    name = turtle.Turtle()
    name.penup()
    name.hideturtle()
    name.color("white")
    name.goto(-300, 290)
    left_user = screen.textinput("Left User", "Name")
    right_user = screen.textinput("Right User", "Name")
    name.write(left_user, align="left", font=("Courier", 25, "bold"))
    name.goto(100, 290)
    name.write(right_user, align="left", font=("Courier", 25, "bold"))


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


is_first_try = 0


def btn_click(x, y):
    global is_first_try
    if -100 <= x <= 100 and -25 <= y <= 25:
        is_first_try += 1
        if is_first_try != 1:
            screen.clear()
            set_screen()
            boundary()
        player_names()
        set_screen()
        boundary()
        button.clear()
        button.hideturtle()
        win.clear()
        win.hideturtle()
        screen.onscreenclick(None)
        start_game()


start_btn(100, 30)
start_btn_text("Start", 48, 18)
screen.update()

# Timer Turtle
timer = turtle.Turtle()
timer.hideturtle()
timer.color("yellow")
timer.penup()
timer.goto(-40, 320)

# Flag to stop the timer
game_over = False


def countdown(time_left):
    if game_over:
        timer.clear()
        return
    minutes = time_left // 60
    seconds = time_left % 60
    timer.clear()
    timer.write(
        f"Time Left: {minutes:02d}:{seconds:02d}",
        align="center",
        font=("Courier", 24, "bold"),
    )
    if time_left > 0:
        screen.ontimer(lambda: countdown(time_left - 1), 1000)
    else:
        # Trigger game over logic here when time runs out
        end_game()


def end_game():
    global game_over, game_is_on
    game_over = True
    game_is_on = False
    timer.clear()
    result()


def start_game():
    global game_over, game_is_on, ball, scoreboard, l_paddles, r_paddles
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
    game_over = False

    countdown(300)  # Start the 5-minute countdown

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
        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce(y=-1)

        # Detect collision with Paddles
        if (
            ball.xcor() > 350
            and ball.distance(r_paddles) < 50
            or ball.xcor() < -350
            and ball.distance(l_paddles) < 50
        ):
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
            result()
            end_game()  # Call end_game to stop and hide the timer


def result():
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
    win.goto(-140, 40)

    if scoreboard.l_score > scoreboard.r_score:
        win.write(f"🎉{left_user} Won🎉", font=("Courier", 24, "bold"), align="left")
    else:
        win.write(f"🎉{right_user} Won🎉", font=("Courier", 24, "bold"), align="left")

    game_is_on = False
    start_btn(120, 30)
    start_btn_text("Play Again!", 97, 18)


screen.mainloop()
