from manim import *

class main(Scene):
    def construct(self):
        x = ValueTracker(0)
        y = ValueTracker(0)
        self.add(x, y)
        y.add_updater(lambda m: m.set_value(x.get_value()**2))
        
        x_text = MathTex("x = {%f}" % x.get_value()).to_edge(UP).scale(1.5)
        y_text = MathTex("y = {%f}" % y.get_value()).next_to(x_text, DOWN).scale(1.5)
        
        x_text.add_updater(lambda m: m.become(
            MathTex("x = {%.2f}" % x.get_value()).to_edge(UP).scale(1.5)
        ))
        y_text.add_updater(lambda m: m.become(
            MathTex("y = {%.2f}" % y.get_value()).next_to(x_text, DOWN).scale(1.5)
        ))
        
        self.add(x_text, y_text)
        self.play(x.animate.set_value(2))
        self.wait()
        self.play(x.animate.set_value(3))
        self.wait()