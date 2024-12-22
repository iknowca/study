from manim import *

class TwoTransforms(Scene):
    def transform(self):
        a = Circle().shift(LEFT)
        b = Square().shift(LEFT)
        c = Triangle().shift(LEFT)
        return [Transform(a, b), Transform(a, c), FadeOut(c)]

    def replacement_transform(self):
        a = Circle().shift(RIGHT)
        b = Square().shift(RIGHT)
        c = Triangle().shift(RIGHT)
        return [ReplacementTransform(a, b), ReplacementTransform(b, c), FadeOut(c)]

    def construct(self):
        self.play(AnimationGroup(
            *self.transform(),
            *self.replacement_transform(),
            lag_ratio=0  # 동시에 진행하고 싶다면 0, 순차적으로 조금씩 어긋나게 하고 싶으면 숫자
        ))
        self.wait(0.5)  # wait for 0.5 seconds