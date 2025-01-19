from manim import *

class main(Scene):
    def construct(self):
        title = Text("Backpropagation - division").scale(1.5).shift(UP*3)
        self.add(title)
        
        node = Circle()
        node_label = MathTex("\div").scale(0.8).move_to(node.get_center())
        
        self.add(node, node_label)
        
        guide_arrow_left = Line(node.get_center()+LEFT*6, node.get_center(), buff=1.5)
        guide_arrow_right = Line(node.get_center(), node.get_center()+RIGHT*6, buff=1.5)
        
        forward_arrow_0 = Arrow(guide_arrow_left.get_start(), guide_arrow_left.get_end(), buff=0).shift(UP*0.2)
        backward_arrow_0 = Arrow(guide_arrow_left.get_end(), guide_arrow_left.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        
        forward0_label = MathTex("x").next_to(forward_arrow_0, UP)
        backward0_label = MathTex(r"-\frac{\partial L}{\partial y}y^2").next_to(backward_arrow_0, DOWN).set_color(BLUE)
        self.add(forward_arrow_0, backward_arrow_0)
        self.add(forward0_label, backward0_label)
        
        forward_arrow_1 = Arrow(guide_arrow_right.get_start(), guide_arrow_right.get_end(), buff=0).shift(UP*0.2)
        backward_arrow_1 = Arrow(guide_arrow_right.get_end(), guide_arrow_right.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        
        forward1_label = MathTex("y").next_to(forward_arrow_1, UP)
        backward1_label = MathTex(r"\frac{\partial L}{\partial y}").next_to(backward_arrow_1, DOWN).set_color(BLUE)
        
        self.add(forward_arrow_1, backward_arrow_1)
        self.add(forward1_label, backward1_label)