from manim import *

class main(Scene):
    def construct(self):
        title = Text("Perceptron").shift(3*UP)
        
        bias = Circle(radius=0.5).shift(3*LEFT + 2*UP)
        input1 = Circle(radius=0.5).shift(3*LEFT)
        input2 = Circle(radius=0.5).shift(3*LEFT + 2*DOWN)
        
        self.add(title)
        self.add(bias, input1, input2)
        
        bias_label = Tex("$1$").move_to(bias.get_center())
        input1_label = Tex("$x_1$").move_to(input1.get_center())
        input2_label = Tex("$x_2$").move_to(input2.get_center())
        
        self.add(bias_label, input1_label, input2_label)
        
        output = Circle(radius=0.5).shift(3*RIGHT )
        output_label = Tex("$y$").move_to(output.get_center())
        self.add(output, output_label)
        
        w1 = Arrow(input1.get_center(), output.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        w2 = Arrow(input2.get_center(), output.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        w3 = Arrow(bias.get_center(), output.get_center(), buff=MED_LARGE_BUFF, stroke_width=3)
        
        self.add(w1, w2, w3)
        
        w1_label = Tex("$w_1$").move_to(w1.get_center()+0.5*UP)
        w2_label = Tex("$w_2$").move_to(w2.get_center()+0.5*UP)
        w3_label = Tex("$b$").move_to(w3.get_center()+0.5*UP)
        
        self.add(w1_label, w2_label, w3_label)