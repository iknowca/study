from manim import *

class main(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1])
        ]
    
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip":False, "color":BLACK}
        )
        
        t = ValueTracker(5)
        k = 25
        
        graph = ax.plot(lambda x: k / x, color=GREEN, x_range=[k/10, 10.0, 0.01], use_smoothing=False)
        
        def get_rectangle():
            polygon = Polygon(*[ax.c2p(*i) for i in self.get_rectangle_corners((0, 0), (t.get_value(), k/t.get_value()))])
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(BLACK)
            return polygon
        
        polygon = always_redraw(get_rectangle)
        
        dot = Dot().set_color(BLACK)
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k/t.get_value())))
        dot.set_z_index(10)
        
        self.add(ax, graph, dot)
        self.play(Create(polygon))
        self.play(t.animate.set_value(10))
        self.play(t.animate.set_value(k/10))
        self.play(t.animate.set_value(5))
        