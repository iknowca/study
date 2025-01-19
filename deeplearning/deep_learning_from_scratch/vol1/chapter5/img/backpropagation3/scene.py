from manim import *

class main(Scene):
    def construct(self):
        title = Text("Backpropagation").scale(1).shift(UP*3)
        self.add(title)
        
        node_plus = Circle().shift(LEFT*2)
        node_pow = Circle().shift(RIGHT*3)
        
        label_plus = MathTex("+").move_to(node_plus.get_center())
        label_pow = MathTex("**2").move_to(node_pow.get_center())
        
        self.add(node_plus, node_pow)
        self.add(label_plus, label_pow)
        
        arrow_guide_line_forward_x = Line(node_plus.get_center()+LEFT*6+UP*3, node_plus.get_center(), buff=1)
        arrow_guide_line_forward_y = Line(node_plus.get_center()+LEFT*6+DOWN*3, node_plus.get_center(), buff=1)
        # self.add(arrow_guide_line_forward_x, arrow_guide_line_forward_y)

        arrow_forward_x = Arrow(arrow_guide_line_forward_x.get_start(), arrow_guide_line_forward_x.get_end(), buff=0).shift(UP*0.2)
        arrow_forward_y = Arrow(arrow_guide_line_forward_y.get_start(), arrow_guide_line_forward_y.get_end(), buff=0).shift(UP*0.2)
        arrow_backward_x = Arrow(arrow_guide_line_forward_x.get_end(), arrow_guide_line_forward_x.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        arrow_backward_y = Arrow(arrow_guide_line_forward_y.get_end(), arrow_guide_line_forward_y.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        self.add(arrow_forward_x, arrow_forward_y, arrow_backward_x, arrow_backward_y)
        
        label_forward_x = MathTex("x").next_to(arrow_forward_x, UP, buff=0).shift(DOWN*0.5)
        label_forward_y = MathTex("y").next_to(arrow_forward_y, UP, buff=0).shift(DOWN*0.5)
        label_backward_x = MathTex(r"\frac{\partial z}{\partial z}\frac{\partial z}{\partial t}\frac{\partial t}{\partial x}").scale(0.7).next_to(arrow_backward_x, DOWN, buff=0).shift(LEFT+UP).set_color(BLUE)
        label_backward_y = MathTex(r"\frac{\partial z}{\partial z}\frac{\partial z}{\partial t}\frac{\partial t}{\partial y}").scale(0.7).next_to(arrow_backward_y, DOWN, buff=0).shift(LEFT).set_color(BLUE)
        self.add(label_forward_x, label_forward_y, label_backward_x, label_backward_y)
        
        arrow_guide_line_t = Line(node_plus.get_center(), node_pow.get_center(), buff=1)
        # self.add(arrow_guide_line_t)
        
        arrow_forward_t = Arrow(arrow_guide_line_t.get_start(), arrow_guide_line_t.get_end(), buff=0).shift(UP*0.2)
        arrow_backward_t = Arrow(arrow_guide_line_t.get_end(), arrow_guide_line_t.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        self.add(arrow_forward_t, arrow_backward_t)
        
        label_forward_t = MathTex("t").next_to(arrow_forward_t, UP, buff=0)
        label_backward_t = MathTex(r"\frac{\partial z}{\partial z}\frac{\partial z}{\partial t}").next_to(arrow_backward_t, DOWN, buff=0).scale(0.7).set_color(BLUE)
        self.add(label_forward_t, label_backward_t)
        
        arrow_guide_line_z = Line(node_pow.get_center(), node_pow.get_center()+RIGHT*5, buff=1)
        # self.add(arrow_guide_line_z)
        
        arrow_forward_z = Arrow(arrow_guide_line_z.get_start(), arrow_guide_line_z.get_end(), buff=0).shift(UP*0.2)
        arrow_backward_z = Arrow(arrow_guide_line_z.get_end(), arrow_guide_line_z.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        self.add(arrow_forward_z, arrow_backward_z)
        
        label_forward_z = MathTex("z").next_to(arrow_forward_z, UP, buff=0)
        label_backward_z = MathTex(r"\frac{\partial z}{\partial z}").next_to(arrow_backward_z, DOWN, buff=0).scale(0.7).set_color(BLUE)
        self.add(label_forward_z, label_backward_z)