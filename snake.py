import turtle, time, random


delay = 0.1
high_score = 0

"""score board"""
pen = turtle.Turtle()
pen.speed(0)
pen.up()
pen.color("black")
pen.ht()
pen.goto(0, 350)


"""setting up the screen.."""
window = turtle.Screen()
window.title("Snake Game by @Samdice_sands ")
window.bgcolor("#E5BA73")
window.setup(width=800, height=800)
window.tracer(0)  # turn of screen updates
border = turtle.Turtle()
border.ht()
border.up()
border.pensize(4)
border.goto(-350, -350)
border.down()
for _ in range(4):
    border.fd(700)
    border.lt(90)


"""creating a snake head (we are going to use an arrow for now"""
head = turtle.Turtle()
head.shape("triangle")
head.speed(0)
head.color("#FAEAB1")
head.up()
head.goto(0, 0)  # start position for the snake, but by default itll always start here
head.direction = "stop"  # configures our head to stay still when the game starts

"""snake body"""
snake_body = []


def move():
    """move function for our turtle"""
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def move_up():
    """move up function for our snake"""
    if head.direction != "down":
        head.setheading(90)
        head.direction = "up"


def move_down():
    """move down function for our snake"""
    if head.direction != "up":
        head.setheading(270)
        head.direction = "down"


def move_left():
    """move left function for our snake"""
    if head.direction != "right":
        head.setheading(180)
        head.direction = "left"


def move_right():
    """move right function for our snake"""
    if head.direction != "left":
        head.setheading(0)
        head.direction = "right"


"""snake food"""
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("#3C2317")
food.up()
food.goto(random.randint(-330, 330), random.randint(-330, 330))


"""keyboard key configuration"""
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")


if __name__ == "__main__":
    while True:
        """main game loop"""
        window.update()

        score = 10 * len(snake_body)

        if score > high_score:
            high_score = score

        pen.clear()  # removes the previous score
        pen.write(
            f"Score: {score}      High Score: {high_score}",
            align="center",
            font=("Courier", 24, "normal"),
        )

        if (
            head.xcor() > 320
            or head.xcor() < -320
            or head.ycor() > 320
            or head.ycor() < -320
        ):
            # check colusion
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # remove snake body
            for part in snake_body:
                part.goto(-90000, -900000)

            snake_body.clear()

        if head.distance(food) < 20:
            # check if the player has reached the food
            x = random.randint(-330, 330)
            y = random.randint(-330, 330)
            food.goto(
                x, y
            )  # move food to a rondom sport once the food is consumed by the snake

            new_bodypart = turtle.Turtle()
            new_bodypart.speed(0)
            new_bodypart.shape("square")
            new_bodypart.color("#C58940")
            new_bodypart.up()
            snake_body.append(
                new_bodypart
            )  # extends the snake's body once it consumes food

        for i in range(len(snake_body) - 1, 0, -1):
            part_x = snake_body[i - 1].xcor()
            part_y = snake_body[i - 1].ycor()
            snake_body[i].goto(part_x, part_y)  # join body with head

        if len(snake_body) > 0:
            part_x = head.xcor()
            part_y = head.ycor()
            snake_body[0].goto(
                part_x, part_y
            )  # move the first part to where the head is

        move()

        # check for body collision
        for part in snake_body:
            if part.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                for part in snake_body:
                    part.goto(-90000, -900000)

                snake_body.clear()

        time.sleep(delay)

"""credits to a youtube channel: @TokyoEdtech"""
