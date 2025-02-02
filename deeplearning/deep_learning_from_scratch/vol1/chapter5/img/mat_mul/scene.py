from manim import *

class main(Scene):
    def construct(self):
        title = Text("Affine layer (Matrix Multiplication)").scale(1).shift(UP*3)
        self.add(title)
        
        node_dot = Circle()
        node_dot_label = Text("Dot").move_to(node_dot.get_center())
        node_dot_combo = VGroup(node_dot, node_dot_label).scale(0.5)
        node_plus = Circle()
        node_plus_label = Text("+").move_to(node_plus.get_center())
        node_plus_combo = VGroup(node_plus, node_plus_label).scale(0.5)
        
        nodes = VGroup(node_dot_combo, node_plus_combo).arrange(RIGHT, buff=5)
        
        self.add(nodes)
        
        arrow_x_guide_line = Line(node_dot.get_center()+UP*2+LEFT*4, node_dot.get_center(), buff=0.6)
        arrow_w_guide_line = Line(node_dot.get_center()+DOWN*2+LEFT*4, node_dot.get_center(), buff=0.6)
        arrow_xw_guide_line = Line(node_dot.get_center(), node_plus.get_center(), buff=0.6)
        arrow_b_guide_line0 = Line(node_dot.get_center()+DOWN*3+LEFT*2, node_dot.get_center()+DOWN*3+RIGHT*2, buff=0.6)
        arrow_b_guide_line1 = Line(arrow_b_guide_line0.get_end(), node_plus.get_center(), buff=0.6)
        arrow_y_guide_line = Line(node_plus.get_center(), node_plus.get_center()+RIGHT*4, buff=0.6)
        
        # self.add(arrow_x_guide_line, arrow_w_guide_line, arrow_xw_guide_line, arrow_b_guide_line0, arrow_b_guide_line1, arrow_y_guide_line)
        
        arrow_x = Arrow(arrow_x_guide_line.get_start(), arrow_x_guide_line.get_end(), buff=0)
        arrow_w = Arrow(arrow_w_guide_line.get_start(), arrow_w_guide_line.get_end(), buff=0)
        arrow_xw = Arrow(arrow_xw_guide_line.get_start(), arrow_xw_guide_line.get_end(), buff=0)
        arrow_b_line = Line(arrow_b_guide_line0.get_start(), arrow_b_guide_line0.get_end(), buff=0)
        arrow_b = Arrow(arrow_b_guide_line0.get_end(), arrow_b_guide_line1.get_end(), buff=0)
        arrow_y = Arrow(arrow_y_guide_line.get_start(), arrow_y_guide_line.get_end(), buff=0)
        
        arrow_forward = VGroup(arrow_x, arrow_w, arrow_xw, arrow_b_line, arrow_b, arrow_y)
        arrow_forward.shift(UP*0.2)
        
        self.add(arrow_x, arrow_w, arrow_xw, arrow_b_line, arrow_b, arrow_y)
        
        label_x = MathTex("X").next_to(arrow_x, UP, buff=0).shift(DOWN*0.5)
        label_x_shape = MathTex(r"N\times D").next_to(label_x, UP, buff=0).scale(0.5)
        label_w = MathTex("W").next_to(arrow_w, UP, buff=0).shift(DOWN*0.5)
        label_w_shape = MathTex(r"D\times M").next_to(label_w, UP, buff=0).scale(0.5)
        label_xw = MathTex(r"X\cdot W").next_to(arrow_xw, UP, buff=0)
        label_xw_shape = MathTex(r"N\times M").next_to(label_xw, UP, buff=0).scale(0.5)
        label_b = MathTex("B").next_to(arrow_b_line, UP, buff=0).shift(UP*0.1)
        label_b_shape = MathTex(r"1\times M").next_to(label_b, UP, buff=0).scale(0.5)
        label_y = MathTex("Y").next_to(arrow_y, UP, buff=0)
        label_y_shape = MathTex(r"N\times M").next_to(label_y, UP, buff=0).scale(0.5)
        
        label_forward = VGroup(label_x, label_x_shape, label_w, label_w_shape, label_xw, label_xw_shape, label_b, label_b_shape, label_y, label_y_shape)
        label_forward.shift(UP*0.2)
        
        self.add(label_x, label_x_shape, label_w, label_w_shape, label_xw, label_xw_shape, label_b, label_b_shape, label_y, label_y_shape)
        
        arrow_py = Arrow(arrow_y_guide_line.get_end(), arrow_y_guide_line.get_start(), buff=0).set_color(BLUE).shift(DOWN*0.2)
        label_py = MathTex(r"\frac{\partial L}{\partial Y}").scale(0.5).next_to(arrow_py, DOWN, buff=0)
        self.play(Create(arrow_py))
        self.play(Create(label_py))
        
        arrow_pb_line = Line(arrow_b_guide_line1.get_end(), arrow_b_guide_line0.get_end(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        arrow_pb = Arrow(arrow_b_guide_line0.get_end(), arrow_b_guide_line0.get_start(), buff=0).shift(DOWN*0.2).set_color(BLUE)
        label_pb = MathTex(r"\frac{\partial L}{\partial Y}").scale(0.5).next_to(arrow_pb, DOWN, buff=0).set_color(BLUE)
        
        self.play(Create(arrow_pb_line))
        self.play(Create(arrow_pb))
        self.play(Create(label_pb))
        
        arrow_pxw = Arrow(arrow_xw_guide_line.get_end(), arrow_xw_guide_line.get_start(), buff=0).set_color(BLUE).shift(DOWN*0.2)
        label_pxw = MathTex(r"\frac{\partial L}{\partial Y}").scale(0.5).next_to(arrow_pxw, DOWN, buff=0).set_color(BLUE)
        self.play(Create(arrow_pxw))
        self.play(Create(label_pxw))
        
        arrow_px = Arrow(arrow_x_guide_line.get_end(), arrow_x_guide_line.get_start(), buff=0).set_color(BLUE).shift(DOWN*0.2)
        label_px = MathTex(r"\frac{\partial L}{\partial X}").scale(0.5).next_to(arrow_px, DOWN, buff=0).set_color(BLUE).shift(LEFT*1+UP*0.5)
        
        self.play(Create(arrow_px))
        self.play(Create(label_px))
        self.wait()
        self.play(label_px.animate.become(MathTex(r"\frac{\partial L}{\partial Y}\cdot W^T").scale(0.5).next_to(arrow_px, DOWN, buff=0).set_color(BLUE).shift(LEFT*1+UP*0.5)))
        self.wait()
        arrow_pw = Arrow(arrow_w_guide_line.get_end(), arrow_w_guide_line.get_start(), buff=0).set_color(BLUE).shift(DOWN*0.2)
        label_pw = MathTex(r"\frac{\partial L}{\partial W}").scale(0.5).next_to(arrow_pw, DOWN, buff=0).set_color(BLUE).shift(UP*0.5)
        
        self.play(Create(arrow_pw))
        self.play(Create(label_pw))
        self.wait()
        self.play(label_pw.animate.become(MathTex(r"X^T\cdot\frac{\partial L}{\partial Y}").scale(0.5).next_to(arrow_pw, DOWN, buff=0).set_color(BLUE).shift(UP*0.5)))
        self.wait()
        
        