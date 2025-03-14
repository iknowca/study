from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include":[2, 3]},
            axis_config={"color": BLACK},
            tips=False
        )
        
        labels=ax.get_axis_labels()
        labels.set_color(BLACK)
        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.plot(lambda x: 0.8 * x ** 2 - 3 * x + 4, x_range=[0, 4], color=GREEN_B)
        
        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=RED)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=RED)
        
        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0.3, 0.6], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [2, 3], bounded_graph=curve_1, color=GREY, opacity=0.5)
        
        self.add(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)
        
        
        