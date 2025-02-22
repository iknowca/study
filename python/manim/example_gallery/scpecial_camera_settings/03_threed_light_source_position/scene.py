from manim import *

class main(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            v_range=[0, TAU], u_range=[-PI/2, PI/2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(3*IN)
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        self.add(axes, sphere)
        self.wait()
        
        self.play(self.renderer.camera.light_source.animate.move_to(1*OUT), run_time=2)
        self.wait()