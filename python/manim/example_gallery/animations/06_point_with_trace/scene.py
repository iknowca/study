from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        self.point_with_trace()
        
    def point_with_trace(self):
        path = VMobject().set_color(BLUE)
        
        dot = Dot(color=BLACK)
        
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        
        def update_path(path):
            prev_path = path.copy()
            prev_path.add_points_as_corners([dot.get_center()])
            path.become(prev_path)
            
        path.add_updater(update_path)
        
        self.add(path, dot)
        
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()
        self.play(dot.animate.shift(DOWN))
        self.play(dot.animate.shift(LEFT))
        self.wait()