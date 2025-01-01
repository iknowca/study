from manim import *

class main(Scene):
    def construct(self):
        title = Text("Neural Network").shift(3*UP)
        self.play(Write(title))
        
        input_text = Text("Input Layer", font_size=24).shift(3*LEFT + 3*DOWN)
        i1 = Circle(radius=0.5).shift(3*LEFT + 1*UP)
        i2 = Circle(radius=0.5).shift(3*LEFT + 1*DOWN)
        
        self.play(Create(i1), Create(i2))
        self.play(Write(input_text))
        h1 = Circle(radius=0.5).shift(0*LEFT + 2*UP)
        h2 = Circle(radius=0.5).shift(0*LEFT + 2*DOWN)
        h3 = Circle(radius=0.5).shift(0*LEFT)
        hidden_text = Text("Hidden Layer", font_size=24).shift(0*LEFT + 3*DOWN)
        
        a11 = Arrow(i1.get_center(), h1.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a12 = Arrow(i1.get_center(), h2.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a13 = Arrow(i1.get_center(), h3.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a21 = Arrow(i2.get_center(), h1.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a22 = Arrow(i2.get_center(), h2.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a23 = Arrow(i2.get_center(), h3.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        
        self.play(Create(a11), Create(a12), Create(a13), Create(a21), Create(a22), Create(a23))
        self.play(Create(h1), Create(h2), Create(h3))
        self.play(Write(hidden_text))
        
        o1 = Circle(radius=0.5).shift(3*RIGHT + 1*UP)
        o2 = Circle(radius=0.5).shift(3*RIGHT + 1*DOWN)
        output_text = Text("Output Layer", font_size=24).shift(3*RIGHT + 3*DOWN)
        a31 = Arrow(h1.get_center(), o1.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a32 = Arrow(h1.get_center(), o2.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a33 = Arrow(h2.get_center(), o1.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a34 = Arrow(h2.get_center(), o2.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a35 = Arrow(h3.get_center(), o1.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        a36 = Arrow(h3.get_center(), o2.get_center(), stroke_width=3, buff=MED_LARGE_BUFF)
        
        self.play(Create(a31), Create(a32), Create(a33), Create(a34), Create(a35), Create(a36))
        self.play(Create(o1), Create(o2))
        self.play(Write(output_text))
        self.wait(3)