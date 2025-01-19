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
        self.wait(1)
        self.play(FadeOut(VGroup(nodes, edges, labels)))
        
        
        
    
