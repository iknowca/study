from manim import *

class main(Scene):
    def construct(self):
        title = Text("Backpropagation - Sigmoid").shift(UP*3)
        self.add(title)
        
        node0 = Circle().scale(0.5)
        node1 = Circle().scale(0.5)
        node2 = Circle().scale(0.5)
        node3 = Circle().scale(0.5)
        

        node_g = VGroup(node0, node1, node2, node3).arrange(RIGHT, buff=2)
        
        node0_label = MathTex(r"\times").move_to(node0.get_center())
        node1_label = MathTex(r"\exp").move_to(node1.get_center())
        node2_label = MathTex("+").move_to(node2.get_center())
        node3_label = MathTex("\div").move_to(node3.get_center())
        
        self.add(node_g)
        self.add(node0_label, node1_label, node2_label, node3_label)
        
        guide_line_0 = Line(node0.get_center()+LEFT*3, node0.get_center(), buff=0.8)
        guide_line_1 = Line(node0.get_center(), node1.get_center(), buff=0.8)
        guide_line_2 = Line(node1.get_center(), node2.get_center(), buff=0.8)
        guide_line_3 = Line(node2.get_center(), node3.get_center(), buff=0.8)
        guide_line_4 = Line(node3.get_center(), node3.get_center()+RIGHT*3, buff=0.8)
        
        guide_line_0_add = Line(node0.get_center()+LEFT*3, node0.get_center(), buff=0.8).shift(DOWN*2)
        guide_line_0_bent = Line(guide_line_0_add.get_end(), node0.get_center(), buff=0.8)
        guide_line_2_add = Line(node1.get_center(), node2.get_center(), buff=0.8).shift(DOWN*2)
        guide_line_2_bent = Line(guide_line_2_add.get_end(), node2.get_center(), buff=0.8)
        
        # self.add(guide_line_0, guide_line_1, guide_line_2, guide_line_3, guide_line_4)
        # self.add(guide_line_0_add, guide_line_2_add, guide_line_0_bent, guide_line_2_bent)
        
        arrow_0 = Arrow(guide_line_0.get_start(), guide_line_0.get_end(), buff=0).shift(UP*0.2)
        arrow_1 = Arrow(guide_line_1.get_start(), guide_line_1.get_end(), buff=0).shift(UP*0.2)
        arrow_2 = Arrow(guide_line_2.get_start(), guide_line_2.get_end(), buff=0).shift(UP*0.2)
        arrow_3 = Arrow(guide_line_3.get_start(), guide_line_3.get_end(), buff=0).shift(UP*0.2)
        arrow_4 = Arrow(guide_line_4.get_start(), guide_line_4.get_end(), buff=0).shift(UP*0.2)
        
        arrow_0_bent_line = Line(guide_line_0_add.get_start(), guide_line_0_add.get_end(), buff=0).shift(UP*0.2)
        arrow_0_bent_arrow = Arrow(guide_line_0_add.get_end(), guide_line_0_bent.get_end(), buff=0).shift(UP*0.2)
        arrow_2_bent_line = Line(guide_line_2_add.get_start(), guide_line_2_add.get_end(), buff=0).shift(UP*0.2)
        arrow_2_bent_arrow = Arrow(guide_line_2_add.get_end(), guide_line_2_bent.get_end(), buff=0).shift(UP*0.2)
        
        self.add(arrow_0, arrow_1, arrow_2, arrow_3, arrow_4)
        self.add(arrow_0_bent_line, arrow_0_bent_arrow, arrow_2_bent_line, arrow_2_bent_arrow)
        
        arrow_0_label = MathTex("x").next_to(arrow_0, UP, buff=0)
        arrow_1_label = MathTex("-x").next_to(arrow_1, UP, buff=0)
        arrow_2_label = MathTex("\exp(-x)").scale(0.5).next_to(arrow_2, UP, buff=0)
        arrow_3_label = MathTex("1+\exp(-x)").scale(0.5).next_to(arrow_3, UP, buff=0)
        arrow_4_label = MathTex(r"\frac{1}{1+\exp(-x)}").scale(0.5).next_to(arrow_4, UP, buff=0)
        
        arrow_0_bent_label = MathTex("-1").next_to(arrow_0_bent_line, UP, buff=0.1)
        arrow_2_bent_label = MathTex("1").next_to(arrow_2_bent_line, UP, buff=0.1)        
        self.add(arrow_0_label, arrow_1_label, arrow_2_label, arrow_3_label, arrow_4_label)
        self.add(arrow_0_bent_label, arrow_2_bent_label)
        
        arrow_back_0 = Arrow(guide_line_4.get_end(), guide_line_4.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        arrow_back_1 = Arrow(guide_line_3.get_end(), guide_line_3.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        arrow_back_2 = Arrow(guide_line_2.get_end(), guide_line_2.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        arrow_back_3 = Arrow(guide_line_1.get_end(), guide_line_1.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        arrow_back_4 = Arrow(guide_line_0.get_end(), guide_line_0.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        
        self.add(arrow_back_0, arrow_back_1, arrow_back_2, arrow_back_3, arrow_back_4)
        
        arrow_back_0_label = MathTex(r"\frac{\partial L}{\partial y}").scale(0.5).next_to(arrow_back_0, DOWN, buff=0).set_color(BLUE)
        arrow_back_1_label = MathTex(r"-\frac{\partial L}{\partial y}y^2").scale(0.5).next_to(arrow_back_1, DOWN, buff=0).set_color(BLUE)
        arrow_back_2_label = MathTex(r"-\frac{\partial L}{\partial y}y^2").scale(0.5).next_to(arrow_back_2, DOWN, buff=0).set_color(BLUE)
        arrow_back_3_label = MathTex(r"-\frac{\partial L}{\partial y}y^2\exp(-x)").scale(0.5).next_to(arrow_back_3, DOWN, buff=0).set_color(BLUE)
        arrow_back_4_label = MathTex(r"\frac{\partial L}{\partial y}y^2\exp(-x)").scale(0.5).next_to(arrow_back_4, DOWN, buff=0).set_color(BLUE)

        self.add(arrow_back_0_label, arrow_back_1_label, arrow_back_2_label, arrow_back_3_label, arrow_back_4_label)