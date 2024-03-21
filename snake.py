"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

BodyColorSet = ['black', 'blue', 'green', 'yellow', 'orange']
FoodColorSet = ['black', 'blue', 'green', 'yellow', 'orange']

rBodyColor = random.choice(BodyColorSet)
rFoodColor = random.choice(FoodColorSet)

if rBodyColor == rFoodColor:
    rFoodColor = random.choice(FoodColorSet)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    # Move food to random location
    dx, dy = randrange(-1, 2) * 10, randrange(-1, 2) * 10
    new_x, new_y = food.x + dx, food.y + dy

    # Check if new location is within boundaries
    if -200 <= new_x <= 190 and -200 <= new_y <= 190:
        food.x, food.y = new_x, new_y

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food() # Move food to random location
    else:
        snake.pop(0)
    move_food() # Move food to random location at every move

    clear()

    for body in snake:
        square(body.x, body.y, 9, rBodyColor)

    square(food.x, food.y, 9, rFoodColor)
    update()
    ontimer(move, 100)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()
