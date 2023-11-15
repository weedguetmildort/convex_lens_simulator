# Weedguet Mildort
# convex_lens_simulator.py

# Program summary:
# This program will imitate the property of convex lenses,
# and display an animation of the interaction
# of light rays and the lenses.

# Import necessary libraries
import turtle
import math

# Set up the screen size
turtle.setup(1200, 400)

# Display welcome message
print('Welcome to the lens simulator program!!\n')
print('This program is still a prototype.')
print('It can only simulate convex lenses.\n')

# Hide the drawing tool
turtle.hideturtle()

# Declare variables
lens_type = ''
k = 300
r = 0
d = 0


# The codes for the diameter function
def change_diameter():
    print('The lens material has a refractive index of 2.')
    print('This theoretical index facilitates calculations.')
    print('The lens thickness is measured on a scale from 1 to 5.\n')

    # Instruction message
    global d
    while True:

        try:
            d = input('Select the thickness of the simulated lens:')
            # Read the chosen thickness from the input of the user
            d = float(d)

            # Input validation for thickness input
            while d < 1 or d > 5:
                print('Invalid choice. Choose a value between 1 to 5.\n')
                d = input('Diameter: ')
                d = float(d)
            break
        except ValueError:
            print('Invalid choice. Enter a numeric value between 1 to 5.\n')

    global r
    # Limits the radius of the circle that makes the lens by 150 <= r <= 1500
    r = 1500 - ((d - 1) * 150)

    # The equation make the thickness of the lens more relevant,
    # since the measurement are in pixel
    # In other words, expand the numbers to visually different sizes

    r = float(r)


# Draw lens
def convex(r):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()

    # Formula for the arc length
    p = (2 * (math.asin(k / (2 * r)))) * (180 / math.pi)

    # y = (0.0102*(d**6) - 0.2603*(d**5) + 2.5016*(d**4) - 11.006*(d**3) + 21.727*(d**2) - 13.705*d + 10.764)
    # y = 0.0102x6 - 0.2603x5 + 2.5016x4 - 11.006x3 + 21.727x2 - 13.705x + 10.764

    turtle.setheading(90 - (p / 2))
    turtle.circle(r, p)
    turtle.left(180 - p)
    turtle.circle(r, p)


# Codes for the drawing of the light rays
def light_source():
    turtle.speed(9)

    # Lens maker formula for the focal point
    focal_point = 1 / (2 / r)

    print('\nThe light source is depicted as rays.')
    ray_number = int(input('Select the number of rays to be displayed:'))
    # Change the number of rays displayed based on user input
    ray_distance = 200 / ray_number
    ray_distance = int(ray_distance)

    # Draw the light rays
    for n in range(-100, 101, ray_distance):

        turtle.penup()
        turtle.goto(-750, n)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(750)

        # Formulas to offset the angle of the light rays so they can go through the focal point
        if n == 0:
            turtle.setheading(0)
        elif n > 0:
            m = ((n ** 2) ** 0.5)
            deviation_angle = 90 - (math.atan(focal_point / m)) * (180 / (math.pi))
            turtle.setheading(-deviation_angle)
        else:
            m = ((n ** 2) ** 0.5)
            deviation_angle = 90 - (math.atan(focal_point / m)) * (180 / (math.pi))
            turtle.setheading(deviation_angle)

        # print(deviation_angle)
        # print(n)

        turtle.forward(750)


# Program main code
def simulator():
    program = True

    while program == True:
        turtle.clearscreen()
        change_diameter()
        convex(r)
        light_source()
        input('Press enter to simulate another lens.')
        print('\n')


simulator()
# turtle.done()
