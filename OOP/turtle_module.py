from turtle import Turtle, Screen

# method ---> objects ----> atributes
# Turtle, Screen ---> rambo, my_screen

# object.method 
# car.stop()

rambo = Turtle()
print(rambo)
rambo.shape("turtle")
rambo.color("Cyan", "Green")
rambo.forward(200)

my_screen = Screen()
print(my_screen.canvheight)

# object.method 
my_screen.exitonclick()