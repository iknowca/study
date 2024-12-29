from manim import *

class main(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        circle2 = Circle().rotate(PI/2, axis=RIGHT).set_color(GREEN)
        circle3 = Circle().rotate(PI/2, axis=UP).set_color(BLUE)
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        self.add(circle, axes, circle2, circle3)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()
        self.move_camera(phi=75*DEGREES, theta=30*DEGREES)
        self.wait()