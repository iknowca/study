from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        square = Square(color=BLUE, fill_opacity=1)
        
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_color(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(PI/4))