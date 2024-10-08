# draw squares 

# import package
import turtle

# main function
def main():
    turtle.hideturtle()
    square(100,0,50,'red')
    square(-150,-100,200,'blue')
    square(-200,150,75,'green')

# square function
def square (x,y,width,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

# Call the main function.
if __name__ == '__main__':
    main()

# close program 
turtle.done()