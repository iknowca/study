from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)
        square.set_fill(BLUE, opacity=0.5)
        self.camera.background_color = WHITE

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.wait()