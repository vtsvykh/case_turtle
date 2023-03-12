'''
"Circus"
Group:
Fishchukova Sofia
Tsvykh Viktoria
'''

import turtle


def triangle(x, y, a, b, angle1, angle2, color, fill):
    '''
    Function for draw triangle.
    :param x: x start coordinate
    :param y: y start coordinate
    :param a: length of side
    :param b: length of side
    :param angle1: external angle between sides
    :param angle2: the angle of the cursor after the end
    :param color: stroke color
    :param fill: fill color
    :return:
    '''

    turtle.color(color, fill)
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.forward(a)
    turtle.left(angle1)
    turtle.forward(b)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.seth(angle2)


def ellipse(x, y, a, b, color, fill, pensize):
    '''
    Function for draw ellipse.
    :param x: x start coordinate
    :param y: y start coordinate
    :param a: axis length on x-axis
    :param b: axis length on y-axis
    :param color: stroke color
    :param fill: fill color
    :param pensize: pensize
    :return:
    '''

    turtle.color(color, fill)
    turtle.begin_fill()
    turtle.pensize()
    turtle.pu()
    turtle.goto(x, y)
    turtle.rt(45)
    turtle.pd()

    for i in range(2):
        turtle.circle(a, 90)
        turtle.circle(b, 90)
    turtle.lt(45)
    turtle.end_fill()


def parallelogram(x, y, a, b, angle_1, angle_2, color, fill):
    '''
    Function for draw parallelogram.
    :param x: x start coordinate
    :param y: y start coordinate
    :param a: length of side parallel to x-axis
    :param b: length of side parallel to y-axis
    :param angle_1: bottom right and top left angles
    :param angle_2: top right and bottom left angles
    :param color: stroke color
    :param fill: fill color
    :return:
    '''

    turtle.color(color, fill)
    turtle.begin_fill()
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()

    for i in range(2):
        turtle.fd(a)
        turtle.lt(angle_1)
        turtle.fd(b)
        turtle.lt(angle_2)

    turtle.end_fill()


def draw_fox():
    '''Drawing fox on big ball.'''


def draw_clown():
    '''Drawing clown with balls.'''


    ellipse(-200, -110, 25, 60, 'maroon', 'maroon4', 5)
    turtle.seth(0)
    ellipse(-130, -50, 35, 2, 'peachpuff', 'peachpuff', 5)
    turtle.seth(0)
    ellipse(-280, -53, 35, 2, 'peachpuff', 'peachpuff', 5)
    turtle.seth(-45)
    triangle(-172, -20, 70, 40, 100, 197, 'cornflowerblue', 'cornflowerblue')
    triangle(-192, -20, 70, 40, 100, 0, 'cornflowerblue', 'cornflowerblue')
    turtle.seth(180)
    triangle(-163, -20, 35, 35, 120, 0, 'mediumorchid4', 'mediumorchid4')
    ellipse(-270, -167, 45, 2, 'darkgrey', 'darkgrey', 5)
    turtle.seth(0)
    ellipse(-163, -167, 45, 2, 'darkgrey', 'darkgrey', 5)
    turtle.seth(275)
    triangle(-174, -95, 70, 40, 100, 235, 'cornflowerblue', 'cornflowerblue')
    triangle(-195, -95, 70, 40, 100, 0, 'cornflowerblue', 'cornflowerblue')
    ellipse(-200, -15, 28, 28, 'peachpuff', 'peachpuff', 5)
    ellipse(-182, -4, 5, 5, 'red3', 'red3', 5)
    ellipse(-173, 10, 5, 5, 'black', 'white', 5)
    ellipse(-170, 13, 2, 2, 'black', 'black', 5)
    ellipse(-193, 10, 5, 5, 'black', 'white', 5)
    ellipse(-191, 13, 2, 2, 'black', 'black', 5)
    turtle.seth(360)
    triangle(-210, 22, 60, 60, 120, 0, 'maroon', 'maroon4')
    ellipse(-183, 73, 5, 5, 'cornflowerblue', 'cornflowerblue', 5)
    parallelogram(-179, 50, 7, 7, 90, 90, 'black', 'yellow')
    triangle(-195, 40, 7, 8, 120, 0, 'black', 'orangered')
    parallelogram(-175, 30, 7, 7, 90, 90, 'black', 'moccasin')
    ellipse(-90, -10, 25, 25, 'black', 'yellow', 5)
    ellipse(-130, 80, 25, 25, 'black', 'green', 5)
    ellipse(-190, 160, 25, 25, 'black', 'blue', 5)
    ellipse(-250, 100, 25, 25, 'black', 'red', 5)
    ellipse(-280, 20, 25, 25, 'black', 'orange', 5)


def main():
    '''Main function.'''

    draw_fox()
    draw_clown()


if __name__ == '__main__':
    main()
