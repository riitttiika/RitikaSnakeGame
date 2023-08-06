import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

# Creating a body list which is empty at the start
bodies = []

# Setting up the screen
s = turtle.Screen()
s.title("Ritika's Snake Game")
s.bgcolor("pink")
s.setup(width=600, height=600)

# Create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.fillcolor("black")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score: 0 | Highest Score: 0", align="left", font=("Courier", 14, "normal"))


def moveup():
    if head.direction != "down":
        head.direction = "up"


def movedown():
    if head.direction != "up":
        head.direction = "down"


def moveleft():
    if head.direction != "right":
        head.direction = "left"


def moveright():
    if head.direction != "left":
        head.direction = "right"


def movestop():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Key mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")


def exit_game():
    s.bye()


def game_over():
    global highestscore
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the bodies
    for body in bodies:
        body.goto(1000, 1000)

    bodies.clear()  # Clear the bodies list

    if score > highestscore:
        highestscore = score

    sb.clear()
    sb.write("Game Over!\nYour Score: {}\nHighest Score: {}".format(score, highestscore), align="center",
             font=("Courier", 18, "normal"))
    time.sleep(2)
    sb.clear()
    reset_game()


def reset_game():
    global score, delay
    score = 0
    delay = 0.1
    sb.clear()
    sb.write("Score: {} | Highest Score: {}".format(score, highestscore), align="left", font=("Courier", 14, "normal"))
    head.goto(0, 0)
    head.direction = "stop"
    food.goto(random.randint(-290, 290), random.randint(-290, 290))


# Main game loop
while True:
    s.update()  # Update the screen

    # Check collision with borders
    if head.xcor() > 290:
        head.goto(-290, head.ycor())

    if head.xcor() < -290:
        head.goto(290, head.ycor())

    if head.ycor() > 290:
        head.goto(head.xcor(), -290)

    if head.ycor() < -290:
        head.goto(head.xcor(), 290)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the score
        score += 10
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, highestscore), align="left", font=("Courier", 14, "normal"))

        # Create a new body segment
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.fillcolor("yellow")
        body.penup()
        bodies.append(body)

        # Update the highest score
        if score > highestscore:
            highestscore = score

    # Move the snake bodies
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            game_over()

    time.sleep(delay)

s.mainloop()
