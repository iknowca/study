from manim import *

class main(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        self.rotation_updater()
        
    def rotation_updater(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
            
        line_ref = Line(ORIGIN, LEFT).set_color(BLACK)
        line_moving = Line(ORIGIN, LEFT).set_color(BLUE)
        line_moving.add_updater(updater_forth)
        
        self.add(line_ref, line_moving)
        self.wait(2*PI)
        
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(PI)
        line_moving.remove_updater(updater_back)
        line_moving.add_updater(updater_forth)
        self.wait(PI)
        line_moving.remove_updater(updater_forth)
        
        self.wait(0.5)