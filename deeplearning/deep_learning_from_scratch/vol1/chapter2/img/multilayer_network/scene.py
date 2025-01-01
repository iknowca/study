from manim import *

class main(Scene):
    def construct(self):
        title = Text("Multilayer Network").shift(3*UP)
        self.play(Write(title))
        
        x1 = Circle(radius=0.5)
        x2 = Circle(radius=0.5)
        s1 = Circle(radius=0.5)
        s2 = Circle(radius=0.5)
        y = Circle(radius=0.5)
        
        x1.shift(2*LEFT + 1*UP)
        x2.shift(2*LEFT + 1*DOWN)
        s1.shift(0*LEFT + 1*UP)
        s2.shift(0*LEFT + 1*DOWN)
        y.shift(2*RIGHT)
        
        self.play(Create(x1), Create(x2), Create(s1), Create(s2), Create(y))
        
        x1_label = Tex("$x_1$").move_to(x1.get_center())
        x2_label = Tex("$x_2$").move_to(x2.get_center())
        s1_label = Tex("$s_1$").move_to(s1.get_center())
        s2_label = Tex("$s_2$").move_to(s2.get_center())
        y_label = Tex("$y$").move_to(y.get_center())
        
        self.play(Write(x1_label), Write(x2_label), Write(s1_label), Write(s2_label), Write(y_label))
        
        w11 = Arrow(x1.get_center(), s1.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        w12 = Arrow(x1.get_center(), s2.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        w21 = Arrow(x2.get_center(), s1.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        w22 = Arrow(x2.get_center(), s2.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        
        self.play(Create(w11), Create(w12), Create(w21), Create(w22))
        
        w23 = Arrow(s2.get_center(), y.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        w13 = Arrow(s1.get_center(), y.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        
        self.play(Create(w13), Create(w23))
        self.wait(2)
        
        
        