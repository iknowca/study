from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        dot = Dot(ORIGIN, color=BLACK)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0).set_color(BLACK)
        numberplane = NumberPlane().set_color(BLUE)
        origin_text = Text('(0, 0)').next_to(dot, DOWN).set_color(BLACK)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT).set_color(BLACK)
        self.add(numberplane, dot, arrow, origin_text, tip_text)