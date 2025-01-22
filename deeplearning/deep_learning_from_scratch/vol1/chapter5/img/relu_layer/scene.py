from manim import *

class main(Scene):
    def construct(self):
        title = Text("Backpropagation - ReLU").scale(1.5).shift(UP*3)
        self.add(title)
        
        subtitle = MathTex(r"x>0").scale(1).shift(UP*2)
        self.add(subtitle)
        
        node = Circle()
        node_label = Text("ReLU").move_to(node.get_center())
        
        self.add(node, node_label)
        
        guide_arrow_left = Line(node.get_center()+LEFT*6, node.get_center(), buff=1.5)
        guide_arrow_right = Line(node.get_center(), node.get_center()+RIGHT*6, buff=1.5)
        
        forward_arrow_0 = Arrow(guide_arrow_left.get_start(), guide_arrow_left.get_end(), buff=0).shift(UP*0.2)
        backward_arrow_0 = Arrow(guide_arrow_left.get_end(), guide_arrow_left.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        
        forward0_label = MathTex("x").next_to(forward_arrow_0, UP)
        backward0_label = MathTex(r"\frac{\partial L}{\partial y}").next_to(backward_arrow_0, DOWN).set_color(BLUE)
        
        self.add(forward_arrow_0, backward_arrow_0)
        self.add(forward0_label, backward0_label)
        
        forward_arrow_1 = Arrow(guide_arrow_right.get_start(), guide_arrow_right.get_end(), buff=0).shift(UP*0.2)
        backward_arrow_1 = Arrow(guide_arrow_right.get_end(), guide_arrow_right.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        
        forward1_label = MathTex("y").next_to(forward_arrow_1, UP)
        backward1_label = MathTex(r"\frac{\partial L}{\partial y}").next_to(backward_arrow_1, DOWN).set_color(BLUE)
        
        self.add(forward_arrow_1, backward_arrow_1)
        self.add(forward1_label, backward1_label)
        
        self.wait(2)
        
        subtitle2 = MathTex(r"x\le 0").move_to(subtitle).scale(1)
        backward0_label2 = MathTex(r"0").move_to(backward0_label).set_color(BLUE)
        
        self.play(Transform(subtitle, subtitle2), Transform(backward0_label, backward0_label2))
        self.wait(2)
        self.play(subtitle.animate.become(MathTex(r"x>0").scale(1).shift(UP*2).move_to(subtitle)),
                    backward0_label.animate.become(MathTex(r"\frac{\partial L}{\partial y}").next_to(backward_arrow_0, DOWN).set_color(BLUE).move_to(backward0_label)))
        self.wait(2)
        self.play(subtitle.animate.become(MathTex(r"x\le 0").move_to(subtitle).scale(1),
                    backward0_label.animate.become(MathTex(r"0").move_to(backward0_label).set_color(BLUE))))