"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Tyrique Jackson
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------

    window = rg.RoseWindow()

    sam = rg.Circle(rg.Point(100, 40), 21)
    sam.fill_color = 'green'
    sam.attach_to(window)

    sarge = rg.Circle(rg.Point(167, 89), 17)
    sarge.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------

    window2 = rg.RoseWindow()

    gordan = rg.Circle(rg.Point(145, 79), 5)
    gordan.fill_color = 'blue'
    gordan.attach_to(window2)

    garfield = rg.Rectangle(rg.Point(132, 45), rg.Point(76, 184))
    garfield.attach_to(window2)

    window2.render()
    window2.close_on_mouse_click()

    print('The thickness of the circle is:', gordan.outline_thickness)
    print('The fill color is', gordan.outline_color)
    print('The Point is', gordan.center)
    print('X coordinate is', gordan.center.x)
    print('Y coordinate is', gordan.center.y)
    print('The thickness of the square is', garfield.outline_thickness)
    print('The fill color is', garfield.fill_color)
    print('The Point is', garfield.corner_1)
    print('X coordinate', garfield.corner_1.x)
    print('Y coordinate', garfield.corner_2.y)

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.

    window3 = rg.RoseWindow()

    dave = rg.Line(rg.Point(123, 184), rg.Point(100, 200))
    dan = rg.Line(rg.Point(174, 147), rg.Point(170, 230))
    dan.thickness = 10
    dave.attach_to(window3)
    dan.attach_to(window3)
    window3.render()
    window3.close_on_mouse_click()
    print(rg.Line.get_midpoint(dan))
    print('X coordinate', rg.Line.get_midpoint(dan).x)
    print('Y coordinate', rg.Line.get_midpoint(dan).y)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
