import turtle

screen = turtle.Screen()

screen.setup(width=1000, height=600)


def getMouseClickCoor(x, y):
    print(f'X={x}, Y={y}')


turtle.onscreenclick(getMouseClickCoor)

turtle.mainloop()

screen.exitonclick()
