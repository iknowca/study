from manim import *

class main(Scene):
    def construct(self):

        title = Text("Softmax-with-Loss Layer")
        title.to_edge(UP)
        self.add(title)
        
        
        sample = ImageMobject("./mnist_sample.png")
        sample.scale(2)
        
        node_width = 0.8
        node_height = 5
        input_node = Rectangle(height=node_height, width=node_width)
        affine1_node = Rectangle(height=node_height, width=node_width)
        affine2_node = Rectangle(height=node_height, width=node_width)
        affine3_node = Rectangle(height=node_height, width=node_width)
        relu1_node = Rectangle(height=node_height, width=node_width)
        relu2_node = Rectangle(height=node_height, width=node_width)
        softmax_node = Rectangle(height=node_height, width=node_width)
        
        hidden_group = VGroup(input_node, affine1_node, relu1_node,affine2_node, relu2_node,affine3_node, softmax_node)
        hidden_group.arrange(RIGHT, buff=1).shift(DOWN)
        sample.move_to(input_node.get_center())
        self.add(sample)
        
        affine1_label = Text("Affine").move_to(affine1_node.get_center()).scale(0.5)
        affine2_label = Text("Affine").move_to(affine2_node.get_center()).scale(0.5)
        affine3_label = Text("Affine").move_to(affine3_node.get_center()).scale(0.5)
        relu1_label = Text("ReLU").move_to(relu1_node.get_center()).scale(0.5)
        relu2_label = Text("ReLU").move_to(relu2_node.get_center()).scale(0.5)
        softmax_label = Text("Softmax").move_to(softmax_node.get_center()).scale(0.3)
        label_group = VGroup(affine1_label, affine2_label, affine3_label, relu1_label, relu2_label, softmax_label)

        self.add(label_group)        
        self.add(hidden_group)
        
        guide0 = Line(input_node.get_center()+UP*2.2, softmax_node.get_center()+UP*2.2)
        guide1 = guide0.copy().shift(DOWN*0.5)
        guide2 = guide1.copy().shift(DOWN*0.5)
        guide3 = guide2.copy().shift(DOWN*0.5)
        guide4 = guide3.copy().shift(DOWN*0.5)
        guide5 = guide4.copy().shift(DOWN*0.5)
        guide6 = guide5.copy().shift(DOWN*0.5)
        guide7 = guide6.copy().shift(DOWN*0.5)
        guide8 = guide7.copy().shift(DOWN*0.5)
        guide9 = guide8.copy().shift(DOWN*0.5)
        
        guide_group = VGroup(guide0, guide1, guide2, guide3, guide4, guide5, guide6, guide7, guide8, guide9)
        guide_group.set_color(GREEN)
        # self.add(guide_group)
        
        input_arrow0 = Arrow(input_node.get_right()+guide0.get_top(), affine1_node.get_left()+guide0.get_top(), buff=0)
        input_arrow1 = Arrow(input_node.get_right()+guide1.get_top(), affine1_node.get_left()+guide1.get_top(), buff=0)
        input_arrow2 = Arrow(input_node.get_right()+guide2.get_top(), affine1_node.get_left()+guide2.get_top(), buff=0)
        input_arrow8 = Arrow(input_node.get_right()+guide8.get_top(), affine1_node.get_left()+guide8.get_top(), buff=0)
        input_arrow9 = Arrow(input_node.get_right()+guide9.get_top(), affine1_node.get_left()+guide9.get_top(), buff=0)
        input_dots = Text("...").move_to(input_node.get_right()+guide5.get_top()).shift(RIGHT*0.5).rotate(PI/2)
        
        input_arrow_group = VGroup(input_arrow0, input_arrow1, input_arrow2, input_arrow8, input_arrow9, input_dots)
        input_arrow_group.shift(UP)
        
        self.add(input_arrow_group)
        
        affine1_arrow0 = Arrow(affine1_node.get_right()+guide0.get_top(), relu1_node.get_left()+guide0.get_top(), buff=0)
        affine1_arrow1 = Arrow(affine1_node.get_right()+guide1.get_top(), relu1_node.get_left()+guide1.get_top(), buff=0)
        affine1_arrow2 = Arrow(affine1_node.get_right()+guide2.get_top(), relu1_node.get_left()+guide2.get_top(), buff=0)
        affine1_arrow8 = Arrow(affine1_node.get_right()+guide8.get_top(), relu1_node.get_left()+guide8.get_top(), buff=0)
        affine1_arrow9 = Arrow(affine1_node.get_right()+guide9.get_top(), relu1_node.get_left()+guide9.get_top(), buff=0)
        
        affine1_dots = Text("...").move_to(affine1_node.get_right()+guide5.get_top()).shift(RIGHT*0.5).rotate(PI/2)
        
        affine1_arrow_group = VGroup(affine1_arrow0, affine1_arrow1, affine1_arrow2, affine1_arrow8, affine1_arrow9, affine1_dots)
        affine1_arrow_group.shift(UP)
        self.add(affine1_arrow_group)
        
        relu1_arrow00 = Arrow(relu1_node.get_right()+guide0.get_top(), affine2_node.get_left()+guide0.get_top(), buff=0)
        relu1_arrow01 = Arrow(relu1_node.get_right()+guide0.get_top(), affine2_node.get_left()+guide1.get_top(), buff=0)
        relu1_arrow02 = Arrow(relu1_node.get_right()+guide0.get_top(), affine2_node.get_left()+guide2.get_top(), buff=0)
        relu1_arrow09 = Arrow(relu1_node.get_right()+guide0.get_top(), affine2_node.get_left()+guide9.get_top(), buff=0)
        relu1_arrow10 = Arrow(relu1_node.get_right()+guide1.get_top(), affine2_node.get_left()+guide0.get_top(), buff=0)
        relu1_arrow20 = Arrow(relu1_node.get_right()+guide2.get_top(), affine2_node.get_left()+guide0.get_top(), buff=0)
        relu1_arrow79 = Arrow(relu1_node.get_right()+guide7.get_top(), affine2_node.get_left()+guide9.get_top(), buff=0)
        relu1_arrow89 = Arrow(relu1_node.get_right()+guide8.get_top(), affine2_node.get_left()+guide9.get_top(), buff=0)
        relu1_arrow90 = Arrow(relu1_node.get_right()+guide9.get_top(), affine2_node.get_left()+guide0.get_top(), buff=0)
        relu1_arrow99 = Arrow(relu1_node.get_right()+guide9.get_top(), affine2_node.get_left()+guide9.get_top(), buff=0)        
        relu1_dots = Text("...").move_to(relu1_node.get_right()+guide5.get_top()).shift(RIGHT*0.3).rotate(PI/2)
        relu1_arrow_group = VGroup(relu1_arrow00, relu1_arrow01, relu1_arrow02, relu1_arrow09, relu1_arrow10, relu1_arrow20, relu1_arrow79, relu1_arrow89, relu1_arrow90, relu1_arrow99, relu1_dots)
        relu1_arrow_group.shift(UP)
        self.add(relu1_arrow_group)
        
        affine2_arrow0 = Arrow(affine2_node.get_right()+guide0.get_top(), relu2_node.get_left()+guide0.get_top(), buff=0)
        affine2_arrow1 = Arrow(affine2_node.get_right()+guide1.get_top(), relu2_node.get_left()+guide1.get_top(), buff=0)
        affine2_arrow2 = Arrow(affine2_node.get_right()+guide2.get_top(), relu2_node.get_left()+guide2.get_top(), buff=0)
        affine2_arrow8 = Arrow(affine2_node.get_right()+guide8.get_top(), relu2_node.get_left()+guide8.get_top(), buff=0)
        affine2_arrow9 = Arrow(affine2_node.get_right()+guide9.get_top(), relu2_node.get_left()+guide9.get_top(), buff=0)
        
        affine2_dots = Text("...").move_to(affine2_node.get_right()+guide5.get_top()).shift(RIGHT*0.5).rotate(PI/2)
        
        affine2_arrow_group = VGroup(affine2_arrow0, affine2_arrow1, affine2_arrow2, affine2_arrow8, affine2_arrow9, affine2_dots)
        affine2_arrow_group.shift(UP)
        self.add(affine2_arrow_group)
        
        relu2_arrow00 = Arrow(relu2_node.get_right()+guide0.get_top(), affine3_node.get_left()+guide0.get_top(), buff=0)
        relu2_arrow01 = Arrow(relu2_node.get_right()+guide0.get_top(), affine3_node.get_left()+guide1.get_top(), buff=0)
        relu2_arrow02 = Arrow(relu2_node.get_right()+guide0.get_top(), affine3_node.get_left()+guide2.get_top(), buff=0)
        relu2_arrow09 = Arrow(relu2_node.get_right()+guide0.get_top(), affine3_node.get_left()+guide9.get_top(), buff=0)
        relu2_arrow10 = Arrow(relu2_node.get_right()+guide1.get_top(), affine3_node.get_left()+guide0.get_top(), buff=0)
        relu2_arrow20 = Arrow(relu2_node.get_right()+guide2.get_top(), affine3_node.get_left()+guide0.get_top(), buff=0)
        relu2_arrow79 = Arrow(relu2_node.get_right()+guide7.get_top(), affine3_node.get_left()+guide9.get_top(), buff=0)
        relu2_arrow89 = Arrow(relu2_node.get_right()+guide8.get_top(), affine3_node.get_left()+guide9.get_top(), buff=0)
        relu2_arrow90 = Arrow(relu2_node.get_right()+guide9.get_top(), affine3_node.get_left()+guide0.get_top(), buff=0)
        relu2_arrow99 = Arrow(relu2_node.get_right()+guide9.get_top(), affine3_node.get_left()+guide9.get_top(), buff=0)
        relu2_dots = Text("...").move_to(relu2_node.get_right()+guide5.get_top()).shift(RIGHT*0.3).rotate(PI/2)
        
        relu2_arrow_group = VGroup(relu2_arrow00, relu2_arrow01, relu2_arrow02, relu2_arrow09, relu2_arrow10, relu2_arrow20, relu2_arrow79, relu2_arrow89, relu2_arrow90, relu2_arrow99, relu2_dots)
        relu2_arrow_group.shift(UP)
        self.add(relu2_arrow_group)
        
        affine3_arrow0 = Arrow(affine3_node.get_right()+guide0.get_top(), softmax_node.get_left()+guide0.get_top(), buff=0)
        affine3_arrow1 = Arrow(affine3_node.get_right()+guide1.get_top(), softmax_node.get_left()+guide1.get_top(), buff=0)
        affine3_arrow2 = Arrow(affine3_node.get_right()+guide2.get_top(), softmax_node.get_left()+guide2.get_top(), buff=0)
        
        affine3_arrow9 = Arrow(affine3_node.get_right()+guide9.get_top(), softmax_node.get_left()+guide9.get_top(), buff=0)
        arrine3_dots = Text("...").move_to(affine3_node.get_right()+guide5.get_top()).shift(RIGHT*0.5).rotate(PI/2)
        
        affine3_arrow_group = VGroup(affine3_arrow0, affine3_arrow1, affine3_arrow2, affine3_arrow9, arrine3_dots)
        affine3_arrow_group.shift(UP)
        self.add(affine3_arrow_group)
        
        affine3_arrow0_label = Text("5.3").next_to(affine3_arrow0, UP, buff=0).scale(0.4)
        affine3_arrow1_label = Text("0.3").next_to(affine3_arrow1, UP, buff=0).scale(0.4)
        affine3_arrow2_label = Text("10.1").next_to(affine3_arrow2, UP, buff=0).scale(0.4)
        affine3_arrow9_label = Text("0.01").next_to(affine3_arrow9, UP, buff=0).scale(0.4)
        
        affine3_arrow_label_group = VGroup(affine3_arrow0_label, affine3_arrow1_label, affine3_arrow2_label, affine3_arrow9_label)
        affine3_arrow_label_group.shift(DOWN*0.1)
        self.add(affine3_arrow_label_group)
        
        score_label = Text("Score").next_to(affine3_arrow_label_group, UP, buff=0.5)
        self.add(score_label)
        
        softmax_label0 = Text("0.008").next_to(affine3_arrow0, RIGHT, buff=0.4).scale(0.4)
        softmax_label1 = Text("0.001").next_to(affine3_arrow1, RIGHT, buff=0.4).scale(0.4)
        softmax_label2 = Text("0.991").next_to(affine3_arrow2, RIGHT, buff=0.4).scale(0.4).set_color(RED)
        softmax_label9 = Text("0.004").next_to(affine3_arrow9, RIGHT, buff=0.4).scale(0.4)
        
        self.add(softmax_label0, softmax_label1, softmax_label2, softmax_label9)
        