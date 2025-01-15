from manim import *

class main(Scene):
    def construct(self):
        title = MathTex("f(x, y) = 2x \hat{e_x} + 2y \hat{e_y}")
        func = lambda pos: np.array([-pos[0], -pos[1], -self.function(np.array(pos))])
        self.add(ArrowVectorField(func, length_func=lambda norm: 0.05* norm, max_color_scheme_value=40, min_color_scheme_value=10 ))
        self.add(title)
        
    def function(self, x):
        return np.sum(x**2)
    
    def function_derivative(self, x):
        return 2*x
        