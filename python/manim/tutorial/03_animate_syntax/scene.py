from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle()
        square = Square(color=RED)
        
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(BLUE, opacity=0.3))
        self.play(square.animate.flip(RIGHT))
        self.play(square.animate.shift(UP))
        
class DifferentRotations(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        left_square = Square(color=RED).shift(LEFT*2)
        right_square = Square(color=BLUE).shift(RIGHT*2)
        self.play(left_square.animate.rotate(PI/2), Rotate(right_square, PI/2), run_time=2)
        self.wait()