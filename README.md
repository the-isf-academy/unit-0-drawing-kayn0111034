# Unit 0 Project: Drawing

This is the starter code for [Project 0: Drawing](http://cs.fablearn.org/projects/0-drawing%20project.html). 
Here's what is included:

- `README.md` You're looking at it, or at least the formatted version. (Click "raw" to see the unformatted version.) Every project has a README explaining what it is.
- `project.py` When this is run, it should draw your project. (If your project is well-organized, there might not be much code in `project.py`. Instead, it might import functions from other modules.)
- `planning.md` This is where you will write your project proposal.
- `assessment.md` This is where you will write your self-assessment of your project.
- `helpers.py` This module contains some useful helper functions you might want to use. See the description below.

## Helpers

### no_delay

`no_delay` allows you to run a code block instantly. This is helpful 
when you have a complicated drawing. For example:

    from turtle import *
    from helpers import no_delay

    with no_delay():
        for i in range(1000):
            forward(100)
            right(178)

### animate
(coming soon) `animate` creates an animation by calling a drawing function over and over. 

`animate` takes a single argument, a drawing function. 
You heard that right: you'll be passing a function to a function as an argument. 
The drawing function should take one argument, an integer representing time. The time
step increases by one every time the function is called.

    from turtle import *
    from helpers import animate

    def draw_ball(time_step):
        y = time_step % 100
        sety(y)
        circle(50)

    animate(draw_project)
