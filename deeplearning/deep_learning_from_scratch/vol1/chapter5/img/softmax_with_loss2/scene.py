from manim import *

class main(Scene):
    def construct(self):
        text = Text("Softmax with Cross-Entropy Loss", font="Montserrat").scale(1.2).to_edge(UP)
        self.add(text)
        

        node_width = 2
        node_height = 6
        softmax_node = Rectangle(height=node_height, width=node_width, color=GREY).shift(LEFT*3+DOWN*0.5)
        self.add(softmax_node)
        
        softmax_title = Text("Softmax", font="Montserrat").scale(0.5).move_to(softmax_node.get_top())
        self.add(softmax_title)
        
        cee_node = Rectangle(height=node_height, width=node_width, color=GREY).shift(RIGHT*3+DOWN*0.5)
        self.add(cee_node)
        
        cee_title = Text("Cross-Entropy Loss", font="Montserrat").scale(0.5).move_to(cee_node.get_top())
        self.add(cee_title)
        
        input_softmax_guide1 = Line(start=softmax_node.get_left()+LEFT*3, end=softmax_node.get_left(), buff=0.5).shift(UP*2)
        input_softmax_guide2 = Line(start=softmax_node.get_left()+LEFT*3, end=softmax_node.get_left(), buff=0.5)
        input_softmax_guide3 = Line(start=softmax_node.get_left()+LEFT*3, end=softmax_node.get_left(), buff=0.5).shift(DOWN*2)

        input_softmax_guide_group = VGroup(input_softmax_guide1, input_softmax_guide2, input_softmax_guide3)
        # self.add(input_softmax_guide_group)
        
        softmax_cee_guide1 = Line(start=softmax_node.get_right(), end=cee_node.get_left(), buff=0.5).shift(UP*2)
        softmax_cee_guide2 = Line(start=softmax_node.get_right(), end=cee_node.get_left(), buff=0.5)
        softmax_cee_guide3 = Line(start=softmax_node.get_right(), end=cee_node.get_left(), buff=0.5).shift(DOWN*2)
        
        softmax_cee_guide_group = VGroup(softmax_cee_guide1, softmax_cee_guide2, softmax_cee_guide3)
        # self.add(softmax_cee_guide_group)
        
        cee_output_guide1 = Line(start=cee_node.get_right(), end=cee_node.get_right()+RIGHT*3, buff=0.5)
        # self.add(cee_output_guide1)
        
        pro_input_softmax_arrow1 = Arrow(start=input_softmax_guide1.get_start(), end=input_softmax_guide1.get_end(), buff=0)
        pro_input_softmax_arrow2 = Arrow(start=input_softmax_guide2.get_start(), end=input_softmax_guide2.get_end(), buff=0)
        pro_input_softmax_arrow3 = Arrow(start=input_softmax_guide3.get_start(), end=input_softmax_guide3.get_end(), buff=0)
        pro_input_softmax_arrow_group = VGroup(pro_input_softmax_arrow1, pro_input_softmax_arrow2, pro_input_softmax_arrow3)
        pro_input_softmax_arrow_group.shift(UP*0.3)
        self.add(pro_input_softmax_arrow_group)
        
        pro_input_softmax_label1 = MathTex("a_1").next_to(pro_input_softmax_arrow1, UP*0.5)
        pro_input_softmax_label2 = MathTex("a_2").next_to(pro_input_softmax_arrow2, UP*0.5)
        pro_input_softmax_label3 = MathTex("a_3").next_to(pro_input_softmax_arrow3, UP*0.5)
        self.add(pro_input_softmax_label1, pro_input_softmax_label2, pro_input_softmax_label3)
        
        back_input_softmax_arrow1 = Arrow(start=input_softmax_guide1.get_end(), end=input_softmax_guide1.get_start(), buff=0)
        back_input_softmax_arrow2 = Arrow(start=input_softmax_guide2.get_end(), end=input_softmax_guide2.get_start(), buff=0)
        back_input_softmax_arrow3 = Arrow(start=input_softmax_guide3.get_end(), end=input_softmax_guide3.get_start(), buff=0)
        back_input_softmax_arrow_group = VGroup(back_input_softmax_arrow1, back_input_softmax_arrow2, back_input_softmax_arrow3)
        back_input_softmax_arrow_group.shift(DOWN*0.3).set_color(BLUE)
        self.add(back_input_softmax_arrow_group)
        
        back_input_softmax_label1 = MathTex("y_1-t_1").next_to(back_input_softmax_arrow1, DOWN*0.5).set_color(BLUE)
        back_input_softmax_label2 = MathTex("y_2-t_2").next_to(back_input_softmax_arrow2, DOWN*0.5).set_color(BLUE)
        back_input_softmax_label3 = MathTex("y_3-t_3").next_to(back_input_softmax_arrow3, DOWN*0.5).set_color(BLUE)
        self.add(back_input_softmax_label1, back_input_softmax_label2, back_input_softmax_label3)
        
        pro_softmax_cee_arrow1 = Arrow(start=softmax_cee_guide1.get_start(), end=softmax_cee_guide1.get_end(), buff=0)
        pro_softmax_cee_arrow2 = Arrow(start=softmax_cee_guide2.get_start(), end=softmax_cee_guide2.get_end(), buff=0)
        pro_softmax_cee_arrow3 = Arrow(start=softmax_cee_guide3.get_start(), end=softmax_cee_guide3.get_end(), buff=0)
        pro_softmax_cee_arrow_group = VGroup(pro_softmax_cee_arrow1, pro_softmax_cee_arrow2, pro_softmax_cee_arrow3)
        pro_softmax_cee_arrow_group.shift(UP*0.3)
        self.add(pro_softmax_cee_arrow_group)
        
        pro_softmax_cee_label1 = MathTex("y_1").next_to(pro_softmax_cee_arrow1, UP*0.5)
        pro_softmax_cee_label2 = MathTex("y_2").next_to(pro_softmax_cee_arrow2, UP*0.5)
        pro_softmax_cee_label3 = MathTex("y_3").next_to(pro_softmax_cee_arrow3, UP*0.5)
        self.add(pro_softmax_cee_label1, pro_softmax_cee_label2, pro_softmax_cee_label3)
        
        back_softmax_cee_arrow1 = Arrow(start=softmax_cee_guide1.get_end(), end=softmax_cee_guide1.get_start(), buff=0)
        back_softmax_cee_arrow2 = Arrow(start=softmax_cee_guide2.get_end(), end=softmax_cee_guide2.get_start(), buff=0)
        back_softmax_cee_arrow3 = Arrow(start=softmax_cee_guide3.get_end(), end=softmax_cee_guide3.get_start(), buff=0)
        back_softmax_cee_arrow_group = VGroup(back_softmax_cee_arrow1, back_softmax_cee_arrow2, back_softmax_cee_arrow3)
        back_softmax_cee_arrow_group.shift(DOWN*0.3).set_color(BLUE)
        self.add(back_softmax_cee_arrow_group)
        
        t1 = MathTex("t_1").move_to(pro_softmax_cee_arrow1.get_end()).shift(LEFT+UP*0.8)
        t2 = MathTex("t_2").move_to(pro_softmax_cee_arrow2.get_end()).shift(LEFT+UP)
        t3 = MathTex("t_3").move_to(pro_softmax_cee_arrow3.get_end()).shift(LEFT+UP)
        self.add(t1, t2, t3)
        
        t1_arrow = Arrow(start=t1.get_center(), end=pro_softmax_cee_arrow1.get_end(), buff=0.2)
        t2_arrow = Arrow(start=t2.get_center(), end=pro_softmax_cee_arrow2.get_end(), buff=0.2)
        t3_arrow = Arrow(start=t3.get_center(), end=pro_softmax_cee_arrow3.get_end(), buff=0.2)
        self.add(t1_arrow, t2_arrow, t3_arrow)
        
        pro_cee_output_arrow1 = Arrow(start=cee_output_guide1.get_start(), end=cee_output_guide1.get_end(), buff=0).shift(UP*0.3)
        pro_cee_output_label = MathTex("L").next_to(pro_cee_output_arrow1, UP*0.5)
        self.add(pro_cee_output_arrow1, pro_cee_output_label)

        back_cee_output_arrow1 = Arrow(start=cee_output_guide1.get_end(), end=cee_output_guide1.get_start(), buff=0).shift(DOWN*0.3)
        back_cee_output_arrow1.set_color(BLUE)
        back_cee_output_label = MathTex("1").next_to(back_cee_output_arrow1, DOWN*0.5).set_color(BLUE)
        self.add(back_cee_output_arrow1, back_cee_output_label)