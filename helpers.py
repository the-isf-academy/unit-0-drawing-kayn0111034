# Helers
# Author: Chris Proctor

# This module is a collection of functions that might be useful in your drawing project.
# Some of these functions are probably a little too complicated for students to understand... yet!

from turtle import tracer, delay, update

class no_delay:
    """
    A context manager which runs drawing code instantly. 
    """
    def __enter__(self):
        self.n = tracer()
        self.delay = delay()
        tracer(0, 0)

    def __exit__(self, exc_type, exc_value, traceback):
        update()
        tracer(self.n, self.delay)

