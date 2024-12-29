from manim import *

class main(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        circle2 = Circle().rotate(PI/2, axis=RIGHT).set_color(GREEN)
        circle3 = Circle().rotate(PI/2, axis=UP).set_color(BLUE)
    
        x_label = Tex("X").next_to(axes.x_axis.get_end(), 0.25*RIGHT)
        y_label = Tex("Y").next_to(axes.y_axis.get_end(), 0.25*UP)
        z_label = Tex("Z").next_to(axes.z_axis.get_end(), 0.25*OUT)
    
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        self.add(axes, circle, circle2, circle3, x_label, y_label, z_label)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES, theta=30*DEGREES)
        self.wait()