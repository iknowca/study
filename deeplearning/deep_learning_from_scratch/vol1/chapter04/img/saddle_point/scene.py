from manim import *

class main(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        
        title = Text("Saddle Point").to_corner(UL)
        eq = MathTex("z = x^2 - y^2").next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(title, eq)
        
        axes = ThreeDAxes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            z_range=[-3, 3],
            z_length=3  # Optional: adjust z-axis length
        ).move_to(ORIGIN)
        surface = Surface(
            lambda u, v: axes.c2p(u, v, self.function(u, v)),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(resolution_fa, resolution_fa),
        )
        
        axes.add(surface)
        
        surface.set_style(fill_opacity=1,stroke_color=GREEN)
        surface.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        self.add(axes)
        self.begin_3dillusion_camera_rotation(rate=1)
        self.wait(2*PI)
        
    def function(self, x, y):
        return x**2 - y**2