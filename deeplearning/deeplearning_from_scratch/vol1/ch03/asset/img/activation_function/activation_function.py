from manim import *
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(ROOT))
import env.light_theme
# manim -p -qm -s activation_function.py

class ActivationFunction(Scene):
    def construct(self):
        title = Tex(r"Perceptron", color=BLACK).scale(2).to_edge(UP)
        self.add(title)

        x1 = Circle(radius=0.7, color=BLUE)
        x2 = Circle(radius=0.7, color=BLUE)
        x0 = Circle(radius=0.7, color=GRAY)

        x = VGroup(x1, x2, x0).arrange(UP, buff=0.5).next_to(ORIGIN, LEFT, buff=2)
        x.shift(DOWN*0.5)
        x1_label = Tex(r"$x_1$", color=BLUE).move_to(x1.get_center())
        x2_label = Tex(r"$x_2$", color=BLUE).move_to(x2.get_center())
        x0_label = Tex(r"$1$", color=GRAY).move_to(x0.get_center())

        x_labels = VGroup(x1_label, x2_label, x0_label)

        y = Circle(radius=1, color=GREEN).next_to(ORIGIN, RIGHT, buff=2)
        y.shift(DOWN*0.5)
        arrow0 = Arrow(x0.get_center(), y.get_center(), color=GRAY, buff=1)
        arrow1 = Arrow(x1.get_center(), y.get_center(), color=GRAY, buff=1)
        arrow2 = Arrow(x2.get_center(), y.get_center(), color=GRAY, buff=1)

        arrows = VGroup(arrow0, arrow1, arrow2)

        arrow_labels = VGroup()
        arrow0_label = Tex(r"$b$", color=GRAY).move_to(arrow0.get_center())
        arrow1_label = Tex(r"$w_1$", color=GRAY).move_to(arrow1.get_center())
        arrow2_label = Tex(r"$w_2$", color=GRAY).move_to(arrow2.get_center())
        arrow_labels.add(arrow0_label, arrow1_label, arrow2_label)
        arrow_labels.shift(UP*0.3)

        a_circle = Circle(radius=0.3, color=GREEN).move_to(y.get_center()).shift(LEFT*0.7)
        y_circle = Circle(radius=0.3, color=RED).move_to(y.get_center()).shift(RIGHT*0.7)
        a_label = Tex(r"$a$", color=GREEN).move_to(a_circle.get_center())
        y_label = Tex(r"$y$", color=RED).move_to(y_circle.get_center())

        ay_arrow = Arrow(a_circle.get_center(), y_circle.get_center(), color=GRAY, buff=0.3)
        ay_label = Tex(r"$h()$", color=GRAY, font_size=36).move_to(ay_arrow.get_center()).shift(UP*0.2)
        self.add(arrows)
        self.add(arrow_labels)
        self.add(a_circle, a_label, y_circle, y_label)
        self.add(ay_arrow, ay_label)
        self.add(x, y)
        self.add(x_labels)
