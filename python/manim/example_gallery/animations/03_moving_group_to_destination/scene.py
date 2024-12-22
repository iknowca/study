from manim import *

class main(Scene):
    
    def createDots(self, num, origin_num):
        dots = []
        for i in range(num):
            if i == origin_num:
                dots.append(Dot(ORIGIN, color=RED).scale(1.5))
            else:
                dots.append(Dot(RIGHT*(i-origin_num), color=BLACK))
        return dots

    def construct(self):
        self.camera.background_color = "#FFFFFF"
        group = VGroup(*self.createDots(5, 3))
        dest = Dot([4, 3, 0], color=GREEN)
        self.add(group, dest)
        self.play(group.animate.shift(dest.get_center()))
        self.wait(1)