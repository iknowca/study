from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.camera.background_color = WHITE

        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(circle))