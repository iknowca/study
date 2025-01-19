from manim import *
import urllib.request
from pathlib import Path


class EmojiSVGMobject(SVGMobject):
    def __init__(self, emoji, **kwargs):
        emoji_code = "-".join(f"{ord(c):x}" for c in emoji)
        url = f"https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{emoji_code}.svg"
        path_svg = Path.cwd() / f"{emoji_code}.svg"
        urllib.request.urlretrieve(url, path_svg)
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally
        
class main(Scene):
    def construct(self):
        
        title = Text("Computational Graph").scale(1.5).shift(UP*3)
        self.add(title)
        
        apple = EmojiSVGMobject("🍎")
        node_x2 = Circle()
        node_x1_1 = Circle()
        money = EmojiSVGMobject("💵")
        nodes = VGroup(apple, node_x2, node_x1_1, money).arrange(RIGHT, buff=2)

        edge0 = Arrow(apple.get_center(), node_x2.get_center(), buff=1.5).set_color(GREY)
        edge1 = Arrow(node_x2.get_center(), node_x1_1.get_center(), buff=1.5).set_color(GREY)
        edge2 = Arrow(node_x1_1.get_center(), money.get_center(), buff=1.5).set_color(GREY)
        edges = VGroup(edge0, edge1, edge2)

        label_node_x2 = MathTex(r"\times 2").set_color(GREY)
        label_edge0 = MathTex("\$100").set_color(GREY)
        label_edge1 = MathTex("\$200").set_color(GREY)
        label_edge2 = MathTex("\$220").set_color(GREY)
        labels = VGroup(label_node_x2, label_edge0, label_edge1, label_edge2).arrange(DOWN, buff=1)

        self.add(apple)
        self.add(edge0, label_edge0.next_to(edge0, UP))
        self.add((node_x2))
        self.add((edge1), (label_edge1.next_to(edge1, UP)))
        self.add((node_x1_1))
        self.add((edge2), (label_edge2.next_to(edge2, UP)))
        self.add((money), )

        apple_value_label = MathTex("2")
        tax_value_label = MathTex("1.1")
        
        self.add(MathTex(r"\times").move_to(node_x2), (apple_value_label.move_to(label_node_x2.get_center())))
        
        apple_label = Text("num Apple").next_to(apple, DOWN).scale(0.5)
        tax_label = Text("tax rate").next_to(apple_label, DOWN).scale(0.5)
        
        apple_label_arrow_line = Line(apple_label.get_center(), [node_x2.get_center()[0], apple_label.get_center()[1], 0], buff=1.5)
        
        apple_label_arrow_guide = Line(apple_label_arrow_line.get_end(), node_x2.get_center(), buff=1)
        apple_label_arrow = Arrow(apple_label_arrow_line.get_end(), apple_label_arrow_guide.get_end(), buff=0)
        self.add((apple_label), (apple_label_arrow_line), apple_value_label.next_to(apple_label_arrow_line, UP))
        self.add((apple_label_arrow))
        
        self.add(MathTex(r"\times").move_to(node_x1_1))
        
        tax_label_arrow_line = Line(tax_label.get_center(), [node_x1_1.get_center()[0], tax_label.get_center()[1], 0], buff=1.5)
        tax_label_arrow_guide = Line(tax_label_arrow_line.get_end(), node_x1_1.get_center(), buff=1)
        tax_label_arrow = Arrow(tax_label_arrow_line.get_end(), tax_label_arrow_guide.get_end(), buff=0)
        self.add((tax_label), (tax_label_arrow_line), tax_value_label.next_to(tax_label_arrow_line, UP))
        self.add((tax_label_arrow))
        
        backward_arrow = Arrow(money.get_center(), node_x1_1.get_center(), buff=1.5).shift(DOWN*0.2).set_color(BLUE)
        backward_arrow2 = Arrow(node_x1_1.get_center(), node_x2.get_center(), buff=1.5).shift(DOWN*0.2).set_color(BLUE)
        backward_arrow3 = Arrow(node_x2.get_center(), apple.get_center(), buff=1.5).shift(DOWN*0.2).set_color(BLUE)
        
        self.add(backward_arrow, backward_arrow2, backward_arrow3)
        
        backward_label = MathTex(r"1").next_to(backward_arrow, DOWN).set_color(BLUE)
        backward_label2 = MathTex(r"1.1").next_to(backward_arrow2, DOWN).set_color(BLUE)
        backward_label3 = MathTex(r"2.2").next_to(backward_arrow3, DOWN).set_color(BLUE)
        
        self.add(backward_label, backward_label2, backward_label3)