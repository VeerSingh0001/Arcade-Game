import time
import turtle

import ball
import paddles
import scoreboard

screen = turtle.Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The classic legend Pong Game")
screen.listen()
screen.tracer(0)



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
# screen.update()

l_paddles = paddles.Paddles(-370, 0)
r_paddles = paddles.Paddles(370, 0)
# screen.tracer(1)
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()
# screen.update()
screen.onkey(r_paddles.up, "Up")
screen.onkey(r_paddles.down, "Down")
screen.onkey(l_paddles.up, "w")
screen.onkey(l_paddles.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce(y=-1)

    # Detect collision with r_paddle
    if ball.xcor() > 350 and ball.distance(r_paddles) < 50 or ball.xcor() < -350 and ball.distance(l_paddles) < 50:
        ball.bounce(x=-1)
        # current_ball_speed = ball.speed()
        # current_delay = screen.delay()
        # print(current_delay)
        # ball.speed(current_ball_speed + 5)
        # screen.delay(current_delay - 5)
        # print(ball.speed())

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

screen.exitonclick()
