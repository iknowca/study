from manim import *

class main(Scene):
    def construct(self):
        text = Text("Softmax with Cross-Entropy Loss", font="Montserrat").scale(1.2).to_edge(UP)
        self.add(text)
        
        node_r = 0.2
        
        softmax_node = Rectangle(height=6, width=6, color=GREY).shift(LEFT*3+DOWN*0.5)
        self.add(softmax_node)
        
        softmax_title = Text("Softmax", font="Montserrat").scale(0.5).move_to(softmax_node.get_top())
        self.add(softmax_title)
        
        exp_node1 = Circle(radius=node_r, color=BLUE)
        exp_node2 = Circle(radius=node_r, color=BLUE)
        exp_node3 = Circle(radius=node_r, color=BLUE)
        softmax_exp_group = VGroup(exp_node1, exp_node2, exp_node3)
        softmax_exp_group.arrange(DOWN, buff=1).move_to(softmax_node.get_center()).shift(LEFT*2+DOWN)
        self.add(softmax_exp_group)
        
        exp_node1_label = Text("exp", font="Montserrat").scale(0.3).move_to(exp_node1.get_center())
        exp_node2_label = Text("exp", font="Montserrat").scale(0.3).move_to(exp_node2.get_center())
        exp_node3_label = Text("exp", font="Montserrat").scale(0.3).move_to(exp_node3.get_center())
        self.add(exp_node1_label, exp_node2_label, exp_node3_label)
        
        input_line1 = Line(start=exp_node1.get_center()+LEFT*3, end=exp_node1.get_center(), buff=node_r)
        input_line2 = Line(start=exp_node2.get_center()+LEFT*3, end=exp_node2.get_center(), buff=node_r)
        input_line3 = Line(start=exp_node3.get_center()+LEFT*3, end=exp_node3.get_center(), buff=node_r)
        self.add(input_line1, input_line2, input_line3)
        
        plus_node1 = Circle(radius=node_r, color=RED)
        plus_node1.move_to(softmax_node.get_center()).shift(UP*2+LEFT)
        self.add(plus_node1)
        
        plus_node1_label = Text("+", font="Montserrat").scale(0.3).move_to(plus_node1.get_center())
        self.add(plus_node1_label)
        
        input_plus_line1 = Line(start=exp_node1.get_center(), end=plus_node1.get_center(), buff=node_r)
        input_plus_line2 = Line(start=exp_node2.get_center(), end=plus_node1.get_center(), buff=node_r)
        input_plus_line3 = Line(start=exp_node3.get_center(), end=plus_node1.get_center(), buff=node_r)
        input_plus_line_group = VGroup(input_plus_line1, input_plus_line2, input_plus_line3)
        self.add(input_plus_line_group)
        
        div_node1 = Circle(radius=node_r, color=GREEN)
        div_node1.move_to(softmax_node.get_center()).shift(UP*2+RIGHT)
        self.add(div_node1)
        
        div_node1_label = Text("/", font="Montserrat").scale(0.3).move_to(div_node1.get_center())
        self.add(div_node1_label)
        
        plus_div_line1 = Line(start=plus_node1.get_center(), end=div_node1.get_center(), buff=node_r)
        self.add(plus_div_line1)
        
        times_node1 = Circle(radius=node_r, color=ORANGE)
        times_node2 = Circle(radius=node_r, color=ORANGE)
        times_node3 = Circle(radius=node_r, color=ORANGE)
        softmax_times_group = VGroup(times_node1, times_node2, times_node3)
        softmax_times_group.arrange(DOWN, buff=1).move_to(softmax_node.get_center()).shift(RIGHT*2+DOWN)
        self.add(softmax_times_group)
        
        times_node1_label = MathTex(r"\times").scale(0.4).move_to(times_node1.get_center())
        times_node2_label = MathTex(r"\times").scale(0.4).move_to(times_node2.get_center())
        times_node3_label = MathTex(r"\times").scale(0.4).move_to(times_node3.get_center())
        self.add(times_node1_label, times_node2_label, times_node3_label)
        
        div_times_line1 = Line(start=div_node1.get_center(), end=times_node1.get_center(), buff=node_r)
        div_times_line2 = Line(start=div_node1.get_center(), end=times_node2.get_center(), buff=node_r)
        div_times_line3 = Line(start=div_node1.get_center(), end=times_node3.get_center(), buff=node_r)
        div_times_line_group = VGroup(div_times_line1, div_times_line2, div_times_line3)
        self.add(div_times_line_group)
        
        exp_times_line1 = Line(start=exp_node1.get_center(), end=times_node1.get_center(), buff=node_r)
        exp_times_line2 = Line(start=exp_node2.get_center(), end=times_node2.get_center(), buff=node_r)
        exp_times_line3 = Line(start=exp_node3.get_center(), end=times_node3.get_center(), buff=node_r)
        exp_times_line_group = VGroup(exp_times_line1, exp_times_line2, exp_times_line3)
        self.add(exp_times_line_group)
        
        cross_entropy_node = Rectangle(height=6, width=6, color=GREY).shift(RIGHT*3+DOWN*0.5)
        self.add(cross_entropy_node)
        
        cross_entropy_title = Text("Cross-Entropy Loss", font="Montserrat").scale(0.5).move_to(cross_entropy_node.get_top())
        self.add(cross_entropy_title)
        
        log_node1 = Circle(radius=node_r, color=YELLOW)
        log_node2 = Circle(radius=node_r, color=YELLOW)
        log_node3 = Circle(radius=node_r, color=YELLOW)
        log_node_group = VGroup(log_node1, log_node2, log_node3)
        log_node_group.arrange(DOWN, buff=1).move_to(cross_entropy_node.get_center()).shift(LEFT*2+DOWN)
        self.add(log_node_group)
        
        log_node1_label = MathTex(r"\log").scale(0.4).move_to(log_node1.get_center())
        log_node2_label = MathTex(r"\log").scale(0.4).move_to(log_node2.get_center())
        log_node3_label = MathTex(r"\log").scale(0.4).move_to(log_node3.get_center())
        self.add(log_node1_label, log_node2_label, log_node3_label)
        
        times_log_line1 = Line(start=times_node1.get_center(), end=log_node1.get_center(), buff=node_r)
        times_log_line2 = Line(start=times_node2.get_center(), end=log_node2.get_center(), buff=node_r)
        times_log_line3 = Line(start=times_node3.get_center(), end=log_node3.get_center(), buff=node_r)
        times_log_line_group = VGroup(times_log_line1, times_log_line2, times_log_line3)
        self.add(times_log_line_group)
        
        times_node4 = Circle(radius=node_r, color=ORANGE)
        times_node5 = Circle(radius=node_r, color=ORANGE)
        times_node6 = Circle(radius=node_r, color=ORANGE)
        crr_times_group = VGroup(times_node4, times_node5, times_node6)
        crr_times_group.arrange(DOWN, buff=1).next_to(log_node_group, RIGHT, buff=1)
        self.add(crr_times_group)
        
        times_node4_label = MathTex(r"\times").scale(0.4).move_to(times_node4.get_center())
        times_node5_label = MathTex(r"\times").scale(0.4).move_to(times_node5.get_center())
        times_node6_label = MathTex(r"\times").scale(0.4).move_to(times_node6.get_center())
        self.add(times_node4_label, times_node5_label, times_node6_label)
        
        t1_node = MathTex("t_1").scale(0.5).next_to(times_node4, LEFT+UP, buff=0.5)
        t2_node = MathTex("t_2").scale(0.5).next_to(times_node5, LEFT+UP, buff=0.5)
        t3_node = MathTex("t_3").scale(0.5).next_to(times_node6, LEFT+UP, buff=0.5)
        self.add(t1_node, t2_node, t3_node)
        
        t1_times_line = Line(start=t1_node.get_center(), end=times_node4.get_center(), buff=node_r)
        t2_times_line = Line(start=t2_node.get_center(), end=times_node5.get_center(), buff=node_r)
        t3_times_line = Line(start=t3_node.get_center(), end=times_node6.get_center(), buff=node_r)
        t_times_line_group = VGroup(t1_times_line, t2_times_line, t3_times_line)
        self.add(t_times_line_group)
               
        log_times_line1 = Line(start=log_node1.get_center(), end=times_node4.get_center(), buff=node_r)
        log_times_line2 = Line(start=log_node2.get_center(), end=times_node5.get_center(), buff=node_r)
        log_times_line3 = Line(start=log_node3.get_center(), end=times_node6.get_center(), buff=node_r)
        log_times_line_group = VGroup(log_times_line1, log_times_line2, log_times_line3)
        self.add(log_times_line_group)
        
        plus_node2 = Circle(radius=node_r, color=RED)
        plus_node2.next_to(crr_times_group.get_center(), RIGHT, buff=1)
        self.add(plus_node2)
        
        plus_node2_label = Text("+", font="Montserrat").scale(0.3).move_to(plus_node2.get_center())
        self.add(plus_node2_label)
        
        log_plus_line1 = Line(start=times_node4.get_center(), end=plus_node2.get_center(), buff=node_r)
        log_plus_line2 = Line(start=times_node5.get_center(), end=plus_node2.get_center(), buff=node_r)
        log_plus_line3 = Line(start=times_node6.get_center(), end=plus_node2.get_center(), buff=node_r)
        log_plus_line_group = VGroup(log_plus_line1, log_plus_line2, log_plus_line3)
        self.add(log_plus_line_group)
        
        times_node7 = Circle(radius=node_r, color=ORANGE)
        times_node7.next_to(plus_node2, RIGHT, buff=1)
        self.add(times_node7)
        
        times_node7_label = MathTex(r"\times").scale(0.4).move_to(times_node7.get_center())
        self.add(times_node7_label)
        
        plus_times_line1 = Line(start=plus_node2.get_center(), end=times_node7.get_center(), buff=node_r)
        self.add(plus_times_line1)
        
        times_output_line1 = Line(start=times_node7.get_center(), end=times_node7.get_center()+RIGHT*3, buff=node_r)
        self.add(times_output_line1)
        
        