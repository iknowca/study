from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.camera.background_color = WHITE  # 배경색을 하얗게 설정

        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(circle))