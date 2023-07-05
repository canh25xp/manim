from manimlib import *

class test(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_stroke(RED, width=4)

        square = Square()
        square.set_stroke(BLUE, width=4)
        
        self.play(ShowCreationThenFadeAround(circle))
        self.wait()
        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))