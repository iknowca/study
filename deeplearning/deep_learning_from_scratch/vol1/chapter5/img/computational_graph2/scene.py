from manim import *
from PIL import Image
import numpy as np
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

        edge0 = Arrow(apple.get_center(), node_x2.get_center(), buff=1.5)
        edge1 = Arrow(node_x2.get_center(), node_x1_1.get_center(), buff=1.5)
        edge2 = Arrow(node_x1_1.get_center(), money.get_center(), buff=1.5)
        edges = VGroup(edge0, edge1, edge2)

        label_node_x2 = MathTex(r"\times 2")
        label_node_x1_1 = MathTex(r"\times 1.1")
        label_edge0 = MathTex("\$100")
        label_edge1 = MathTex("\$200")
        label_edge2 = MathTex("\$220")
        labels = VGroup(label_node_x2, label_edge0, label_node_x1_1, label_edge1, label_edge2).arrange(DOWN, buff=1)

        self.play(DrawBorderThenFill(apple))
        self.play(Create(edge0), Create(label_edge0.next_to(edge0, UP)))
        self.play(DrawBorderThenFill(node_x2), Create(label_node_x2.move_to(node_x2.get_center())))
        self.play(Create(edge1), Create(label_edge1.next_to(edge1, UP)))
        self.play(DrawBorderThenFill(node_x1_1), Create(label_node_x1_1.move_to(node_x1_1.get_center())))
        self.play(Create(edge2), Create(label_edge2.next_to(edge2, UP)))
        self.play(DrawBorderThenFill(money), )

        apple_value_label = MathTex("2")
        tax_value_label = MathTex("1.1")
        
        self.play(animate_change_tex(label_node_x2, MathTex(r"\times")), Create(apple_value_label.move_to(label_node_x2.get_center())))
        
        apple_label = Text("num Apple").next_to(apple, DOWN).scale(0.5)
        tax_label = Text("tax").next_to(apple_label, DOWN).scale(0.5)
        
        apple_label_arrow_line = Line(apple_label.get_center(), [node_x2.get_center()[0], apple_label.get_center()[1], 0], buff=1.5)
        
        apple_label_arrow_guide = Line(apple_label_arrow_line.get_end(), node_x2.get_center(), buff=1)
        apple_label_arrow = Arrow(apple_label_arrow_line.get_end(), apple_label_arrow_guide.get_end(), buff=0)
        self.play(Write(apple_label), Create(apple_label_arrow_line), apple_value_label.animate.next_to(apple_label_arrow_line, UP))
        self.play(Create(apple_label_arrow))
        
        
        self.play(animate_change_tex(label_node_x1_1, MathTex(r"\times")), Create(tax_value_label.move_to(label_node_x1_1.get_center())))
        
        
        tax_label_arrow_line = Line(tax_label.get_center(), [node_x1_1.get_center()[0], tax_label.get_center()[1], 0], buff=1.5)
        tax_label_arrow_guide = Line(tax_label_arrow_line.get_end(), node_x1_1.get_center(), buff=1)
        tax_label_arrow = Arrow(tax_label_arrow_line.get_end(), tax_label_arrow_guide.get_end(), buff=0)
        self.play(Write(tax_label), Create(tax_label_arrow_line), tax_value_label.animate.next_to(tax_label_arrow_line, UP))
        self.play(Create(tax_label_arrow))
        
        self.wait(3)
        self.play(FadeOut(VGroup(nodes, edges, labels, apple_label, tax_label, apple_label_arrow, tax_label_arrow, apple_label_arrow_line, tax_label_arrow_line, apple_value_label, tax_value_label)))
        
        
def animate_change_tex(old, new):
    return old.animate.become(new.move_to(old.get_center()))
    
