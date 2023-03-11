'''
"Circus"
Group:
Fishchukova Sofia
Tsvykh Viktoria
'''

import turtle


def triangle(x, y, a, b, angle, color, fill):
    '''
    Function for draw triangle.
    :param x: x start coordinate
    :param y: y start coordinate
    :param a: lengths of equal sides
    :param b: length of side
    :param angle: angle between equal sides
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
    turtle.left(angle)
    turtle.forward(b)
    turtle.goto(x, y)
    turtle.end_fill()


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

    pass

def main():
    '''Main function.'''

    draw_fox()
    draw_clown()

if __name__ == '__main__':
    main()