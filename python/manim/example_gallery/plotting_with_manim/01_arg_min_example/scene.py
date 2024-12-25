from manim import *

class main(Scene):
    def func(self, x):
        return 2*(x-5)**2
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        axes = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False},
        )
        axes.get_axes().set_color(BLACK)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
        t = ValueTracker(0)
        
        graph = axes.plot(self.func, color=MAROON)
        
        initial_point = [axes.coords_to_point(t.get_value(), self.func(t.get_value()))]
        dot = Dot(point=initial_point, color=BLUE)

        dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), self.func(t.get_value()))))
        x_space = np.linspace(*axes.x_range[:2], 200)
        minimum_index = self.func(x_space).argmin()
        
        self.add(axes, labels, graph, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()
