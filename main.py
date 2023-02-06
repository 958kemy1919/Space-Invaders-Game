from turtle import Turtle, Screen
from time import sleep
from random import randint

screen = Screen()
screen.title("Game")
screen.bgcolor("black")
screen.setup(width=800,height=700)
screen.tracer(0)

lifes = 3
score = 0
try:
    with open("highest_score.txt",mode="r") as data_file:
        highest_score = int(data_file.read())
except FileNotFoundError:
    with open("highest_score.txt",mode="w") as data_file:
        data_file.write("0")
        highest_score = 0

scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.color("green")
scoreboard.goto(-300,-300)
scoreboard.write(f"Score: {score}   Highest Score: {highest_score}   Lifes: {lifes}",True,font=("Arial",20,"bold"))

player = Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0,-250)
player.shapesize(0.5,2)
cannon = Turtle()
cannon.color("blue")
cannon.shape("circle")
cannon.penup()
cannon.goto(0,-235)
cannon.shapesize(1)

rocket = Turtle()
rocket.shape("circle")
rocket.color("white")
rocket.penup()
rocket.setheading(90)
rocket.shapesize(0.5,0.6)
rocket.speed("slow")
rocket.goto(player.position())

aliens = []
alien_rocket = Turtle("circle")
alien_rocket.color("yellow")
alien_rocket.penup()
alien_rocket.setheading(270)
alien_rocket.shapesize(0.6,0.7)
alien_rocket.speed("slow")
alien_rocket.hideturtle()
for i in range(0,21):
    new_turtle = Turtle("turtle")
    new_turtle.color("yellow")
    new_turtle.shapesize(0.7,0.7)
    new_turtle.penup()
    new_turtle.speed("slowest")
    new_turtle.setheading(270)
    aliens.append(new_turtle)
x_pos = -250
y_pos = 120
num = 0
for i in range(0,3):
    y_pos += 50
    for j in range(0,7):
        aliens[num].goto((x_pos,y_pos))
        num += 1
        x_pos += 70
    x_pos = -250

def turn_left():
    player.setheading(180)
    cannon.setheading(180)
    player.forward(20)
    cannon.forward(20)
def turn_right():
    player.setheading(0)
    cannon.setheading(0)
    player.forward(20)
    cannon.forward(20)

screen.listen()
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")

def move_rocket():
    rocket.forward(30)

def move_aliens():
    for i in range(0,21):
        aliens[i].goto(aliens[i].xcor(),aliens[i].ycor()-1)

hitted_aliens = []

is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.05)

    move_aliens()

    if alien_rocket.ycor() < -350:
        alien_rocket.hideturtle()
        alien_rocket.setheading(270)
        random_alien = aliens[randint(0,20)]
        while random_alien in hitted_aliens:
            random_alien = aliens[randint(0, 20)]
        alien_rocket.goto(random_alien.xcor(),random_alien.ycor())
        alien_rocket.showturtle()
        alien_rocket.forward(20)
    else:
        alien_rocket.forward(20)

    if rocket.ycor() > 350:
        rocket.hideturtle()
        rocket.goto((player.xcor(),player.ycor()+30))
        rocket.showturtle()
    else:
        move_rocket()

    for i in range(0,len(aliens)):
        if aliens[i].distance(rocket) < 12 and aliens[i] not in hitted_aliens:
            score += 1
            if score > highest_score:
                highest_score = score
                with open("highest_score.txt",mode="w") as data_file:
                    data_file.write(f"{highest_score}")
            aliens[i].hideturtle()
            hitted_aliens.append(aliens[i])
            rocket.goto(player.position())
            scoreboard.clear()
            scoreboard.goto(-300, -300)
            scoreboard.write(f"Score: {score}   Highest Score: {highest_score}   Lifes: {lifes}", True, font=("Arial", 20, "bold"))

    if alien_rocket.distance(player) < 12:
        lifes -= 1
        scoreboard.clear()
        scoreboard.goto(-300, -300)
        scoreboard.write(f"Score: {score}  Highest Score: {highest_score}   Lifes: {lifes}", True, font=("Arial", 20, "bold"))
        if lifes == 0:
            scoreboard.goto(-300, -300)
            scoreboard.write(f"Score: {score}  Highest Score: {highest_score}   Lifes: {lifes}", True, font=("Arial", 20, "bold"))
            is_game_on = False
            scoreboard.goto(-150,0)
            scoreboard.write("GAME OVER !!",True, font=("Arial", 40, "bold"))
            break
    if aliens[0].ycor() < -230:
        is_game_on = False
        scoreboard.goto(-150, 0)
        scoreboard.write("GAME OVER !!",True, font=("Arial", 40, "bold"))
        break


screen.exitonclick()
