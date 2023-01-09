from snake import *
import random

def food_random_position():
    if head.distance(food) < 20:
        # move food to a rondom sport once the food is consumed by the snake
        x = random.randint(-330, 330)
        y = random.randint(-330, 330)
        food.goto(x, y)