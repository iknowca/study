from manim import *
class main(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])
        
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot1 = Dot(ax.i2gp(graph.t_min, graph))
        dot2 = Dot(ax.i2gp(graph.t_max, graph))
        
        self.add(ax, graph, dot1, dot2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))  # Corrected line
        
        def update_curve(mob):
            mob.move_to(moving_dot.get_center())
            
        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)
        
        self.play(Restore(self.camera.frame))

