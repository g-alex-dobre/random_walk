import turtle as t
import random

tim = t.Turtle()
tim.width(15)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def random_step():
  change_color()
  random_direction = random.choice([0,90,180,270])
  tim.left(random_direction)
  tim.forward(50)

for _ in range(30):
  random_step()
  
  
