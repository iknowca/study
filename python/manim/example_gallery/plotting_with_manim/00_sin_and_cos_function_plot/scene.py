from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-1, 1.01, 1),
                "numbers_with_elongated_ticks": np.arange(-1, 1.01, 1),
            },
            tips=False
        )
        axes.get_x_axis().set_color(BLACK)
        axes.get_y_axis().set_color(BLACK)
        axes_labels = axes.get_axis_labels()
        
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)", x_val=-10, direction=UP/2)
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")
        
        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=BLACK, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=BLACK
        )
        plot=VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        
        self.add(plot, labels)