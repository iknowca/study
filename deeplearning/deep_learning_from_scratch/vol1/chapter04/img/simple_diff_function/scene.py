from manim import *

class main(Scene):
    def construct(self):
        title = Text("Simple Difference Function", font="Consolas").shift(UP*3.5)
        function_text = MathTex("f(x) = 0.01 x^2 + 0.1x").next_to(title, DOWN)
        
        h = 1e-4
        x = ValueTracker(10)
        
        x_text = MathTex("x = 10").next_to(function_text, DOWN)
        x_text.add_updater(lambda m: m.become(MathTex("x = " + str(round(x.get_value(), 2))).next_to(function_text, DOWN)))
        slope_text = MathTex("f'(x) = " + str(round(self.fp(x.get_value(), h), 2))).next_to(x_text, DOWN)
        slope_text.add_updater(lambda m: m.become(MathTex("f'(x) = " + str(round(self.fp(x.get_value(), h), 2))).next_to(x_text, DOWN)))
        
        self.add(x_text, slope_text)
        
        ax = Axes(
            x_range=[0, 20],
            y_range=[-1, 7],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True},
        )

        graph = ax.plot(
            lambda x: self.f(x),
            color=GRAY,
            x_range=[0, 20.0, 0.01],
            use_smoothing=False,
        )
        
        def get_t_from_x(x_val):
            return x_val / 20.0 
        tangent = TangentLine(graph, alpha=get_t_from_x(x.get_value()), color=ORANGE, length=8)
        tangent.add_updater(lambda m: m.become(TangentLine(graph, alpha=get_t_from_x(x.get_value()), color=ORANGE, length=8)))

        
        dot = Dot(ax.i2gp(x.get_value(), graph), color=RED)
        dot.add_updater(lambda m: m.move_to(ax.i2gp(x.get_value(), graph)))
        self.add(title, function_text, ax, graph)
        self.add(dot, tangent)
        
        self.play(x.animate.set_value(5), run_time=3, rate_func=smooth)
        self.wait()
        self.play(x.animate.set_value(0), run_time=1, rate_func=smooth)
        self.wait()
        self.play(x.animate.set_value(15), run_time=2, rate_func=smooth)
        self.wait()
        self.play(x.animate.set_value(10), run_time=1, rate_func=smooth)
        self.wait()
        
    def f(self, x):
        return 0.01*x**2 + 0.1*x
    
    def fp(self, x, h=1e-4):
        return (self.f(x + h) - self.f(x-h)) / (2*h)