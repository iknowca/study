from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        d1, d2 = Dot(color=BLUE).set_z_index(1), Dot(color=GREEN).set_z_index(1)
        dg = VGroup(d1, d2).arrange(RIGHT, buff=1)
        l1 = Line(d1.get_center(), d2.get_center()).set_color(RED).set_z_index(0)
        x = ValueTracker(0)
        y = ValueTracker(0)
        
        d1.add_updater(lambda z: z.set_x(x.get_value()))
        d2.add_updater(lambda z: z.set_y(y.get_value()))
        l1.add_updater(lambda z: z.become(Line(d1.get_center(), d2.get_center()).set_color(BLACK).set_z_index(0)))
        
        self.add(d1, d2, l1)
        self.play(x.animate.set_value(5))
        self.play(y.animate.set_value(4))
        self.wait()