from manim import *


class main(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        
        title = MathTex("f(x_0, x_1) = x^2_0 + x^2_1").scale(1.5).shift(UP*3)
        self.add_fixed_in_frame_mobjects(title)
        
                
        axes = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[0, 18],
            z_length=3  # Optional: adjust z-axis length
        ).move_to(ORIGIN)
        
        surface = Surface(
            lambda u, v: axes.c2p(u, v, self.function(np.array([u, v]))),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(resolution_fa, resolution_fa),
        )
        

        axes.add(surface)
        
        surface.set_style(fill_opacity=1,stroke_color=GREEN)
        surface.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        self.add(axes)
        self.begin_3dillusion_camera_rotation(rate=1)
        self.wait(2*PI)
    
    def function(self, x):
        return np.sum(x**2)
        