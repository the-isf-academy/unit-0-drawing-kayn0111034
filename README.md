# Unit 0 Project: Drawing

This is the starter code for [Project 0: Drawing](http://cs.fablearn.org/projects/0-drawing project.html). You 

## Helpers
You are also given a module of helper functions. 

### no_delay

`no_delay` allows you to run a code block instantly. This is helpful 
when you have a complicated drawing. For example:

    from turtle import *
    from helpers import no_delay

    with no_delay():
        for i in range(1000):
            forward(100)
            right(178)
