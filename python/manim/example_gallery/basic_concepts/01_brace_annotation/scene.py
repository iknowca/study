from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        dot = Dot([-2, -1, 0]).set_color(BLACK)
        dot2 = Dot([2, 1, 0]).set_color(BLACK)
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line).set_color(BLACK)
        b1text = b1.get_text("Horizontal distance").set_color(BLACK)
        
        b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector()).set_color(BLACK)
        b2text = b2.get_text("$x-x_1$").set_color(BLACK)
        self.add(dot, dot2, line, b1, b2, b1text, b2text)