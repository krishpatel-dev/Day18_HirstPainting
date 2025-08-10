import turtle as t
import random
tim = t.Turtle()

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGrey', 'SeaGreen']
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3, 11):
    tim.color(colors[shape_side - 3])
    draw_shape(shape_side)
