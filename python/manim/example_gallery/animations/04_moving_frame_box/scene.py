from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)", "=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)"
        ).set_color(BLACK)
        self.play(Write(text))
        
        framebox0 = SurroundingRectangle(text[0], buff=0.1).set_color(BLUE)
        framebox1 = SurroundingRectangle(text[2], buff=0.1).set_color(RED)
        framebox2 = SurroundingRectangle(text[4], buff=0.1).set_color(GREEN)
        self.play(Create(framebox0))
        
        self.wait()
        self.play(ReplacementTransform(framebox0, framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()