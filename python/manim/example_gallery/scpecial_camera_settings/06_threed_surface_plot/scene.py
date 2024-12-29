from manim import *

class main(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)
        
        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0., 0.]
            d = np.linalg.norm(np.array([x-mu[0], y-mu[1]]))
            z = np.exp(-d**2/(2.0*sigma**2))
            return np.array([x, y, z])
    
        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, 2],
            u_range=[-2, 2],
        )
        
        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1, stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(BLUE, GREEN, opacity=0.5)
        
        axes = ThreeDAxes()
        self.add(gauss_plane, axes)
        
        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait(2)