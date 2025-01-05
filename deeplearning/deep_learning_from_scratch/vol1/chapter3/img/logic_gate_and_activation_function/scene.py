from manim import *

class main(Scene):
    def construct(self):
        x_values = [ValueTracker(1), ValueTracker(0), ValueTracker(0)]
        w_values = [ValueTracker(0.7), ValueTracker(0.5), ValueTracker(0.5)]
        y_init = self.y_value(x_values, w_values)
        y_tracker = ValueTracker(y_init)
        
        y_tracker.add_updater(lambda m: m.set_value(
            self.y_value(
                x_values, w_values
            )
        ))
        self.add(y_tracker, *x_values, *w_values)
        self.nn(x_values, w_values, y_tracker)
        self.activation_function(x_values, w_values, y_tracker)
        self.equation(x_values, w_values, y_tracker)
        
        self.wait()
        self.play(x_values[1].animate.set_value(1))
        self.play(x_values[2].animate.set_value(1))
        self.play(x_values[1].animate.set_value(0.5), x_values[2].animate.set_value(0.5))
        self.play(x_values[1].animate.set_value(0))
        self.play(x_values[1].animate.set_value(1), x_values[2].animate.set_value(0))
        self.play(x_values[1].animate.set_value(0))
    
    def y_value(self, x_values, w_values):
        return sum([x.get_value() * w.get_value() for x, w in zip(x_values, w_values)])

    def nn(self, x_values, w_values, y_tracker):

        X = VGroup()
        W = VGroup()
        Y = VGroup()
        
        def get_label_updater(x_value, circle):
            def updater_func(m):
                val = x_value.get_value()
                new_tex = MathTex(f"{val:0.1f}").move_to(circle.get_center()).scale(1.5)
                m.become(new_tex)
            return updater_func
        
        for i in range(3):
            circle = Circle(radius=1)
            label = MathTex(f"{x_values[i].get_value():0.1f}").move_to(circle.get_center()).scale(3)
            label.add_updater(get_label_updater(x_values[i], circle))
            combo = VGroup(circle, label)
            X.add(combo)
            
        for i in range(1):
            circle = Circle(radius=2)
            circle.add_updater(lambda m: m.become(circle.copy().move_to(Y[0].get_center()).set_color(BLUE if y_tracker.get_value() > 1 else RED)))
            label = MathTex(r"{%0.1f}" % (y_tracker.get_value())).move_to(circle.get_center()).scale(3)
            label.add_updater(get_label_updater(y_tracker, circle))
            combo = VGroup(circle, label)
            Y.add(combo)

        X.arrange(DOWN, buff=1)
        Y.arrange(UP, buff=1)
        nn = VGroup(X, Y).arrange(RIGHT, buff=5)
        nn.add(W)
        for i in range(3):
            direction = Y[0].get_center() - X[i].get_center()
            dist = np.linalg.norm(direction)
            direction /= dist
            perp_direction = np.array([-direction[1], direction[0], 0])
            start = X[i].get_center() + direction * 1
            end = Y[0].get_center() - direction * 2
            arrow = Arrow(start=start, end=end, buff=0.5)
            brace = Brace(arrow, perp_direction, buff=-0.2)
            label = brace.get_text(f"{w_values[i].get_value():0.1f}")
            combo = VGroup(arrow, label)
            W.add(combo)
            
        

        nn.scale(0.5)
        nn.shift(LEFT*3.5)
        self.add(nn)
        pass
    
    def activation_function(self, x_values, w_values, y_values):
        ax = Axes(x_range=[-4, 4], y_range=[-0.5, 1.5])
        graph = ax.plot(lambda x: self.sigmoid(x), color=BLUE, x_range=[-4, 4])
        moving_dot = Dot(ax.i2gp(y_values.get_value(), graph), color=RED).scale(1.5)
        moving_dot.add_updater(lambda m: m.move_to(ax.i2gp(y_values.get_value(), graph)))
        activation_line = ax.plot(lambda x: self.sigmoid(1), color=ORANGE, x_range=[-4, 4])
        group = VGroup(ax, graph, moving_dot, activation_line)
        group.scale(1/2)
        group.shift(RIGHT*3.5)
        self.add(ax, graph, moving_dot, activation_line)
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def equation(self, x_values, w_values, y_values):
        def get_values():
            values = []
            for x, w in zip(x_values, w_values):
                values.extend([x.get_value(), w.get_value()])
            return tuple(values)
        
        text = MathTex(r"%0.1f* %0.1f + %0.1f* %0.1f + %0.1f* %0.1f=%0.1f" % (*get_values(), y_values.get_value())).scale(1.5)
        eq = VGroup(text)
        eq.shift(DOWN*3)
        text.add_updater(lambda m: m.become(MathTex(r"%0.1f* %0.1f + %0.1f* %0.1f + %0.1f* %0.1f=%0.1f" % (*get_values(), y_values.get_value(), )).scale(1.5).move_to(m)))
        self.add(text)
        
    