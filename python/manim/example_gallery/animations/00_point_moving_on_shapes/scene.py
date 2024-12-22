from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        circle = Circle(radius=1, color=BLUE)
        dot = Dot().set_color(BLACK)
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)
        
        line = Line([3, 0, 0], [5, 0, 0]).set_color(BLACK)
        self.add(line)
        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_functions=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0], radians=PI), run_time=1)
        self.wait(1)
        self.play(Rotating(dot, about_point=[4, 0, 0], radians=-PI), run_time=1)
        self.wait(1)