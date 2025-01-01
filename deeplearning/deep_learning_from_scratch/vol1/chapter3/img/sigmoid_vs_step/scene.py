from manim import *

class main(Scene):
    def construct(self):
        title = Text("Step Function vs Sigmoid Function").shift(3*UP)
        self.add(title)
        
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-0.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes.shift(0.7* DOWN)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        step_graph_left = axes.plot(lambda x: 0, x_range=[-5, 0], color=ORANGE, use_smoothing=False)
        step_graph_right = axes.plot(lambda x: 1, x_range=[0, 5], color=ORANGE, use_smoothing=False)
        step_vertical_line = Line(
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            color=ORANGE
        )
        step_graph_label_text = Tex(r"""$
            h(x) = \begin{cases}
            0 & (x \leq 0) \\
            1 & (x > 0)
            \end{cases}
            $""")
        step_graph_label = axes.get_graph_label(step_graph_left, label=step_graph_label_text, x_val=-2, direction=UP, buff=1)
        
        sigmoid_graph = axes.plot(lambda x: 1/(1+np.exp(-x)), x_range=[-5, 5], color=RED, use_smoothing=False)
        sigmoid_graph_label_text = Tex(r"""$
            h(x) = \frac{1}{1 + e^{-x}}
            $""")
        sigmoid_graph_label = axes.get_graph_label(sigmoid_graph, label=sigmoid_graph_label_text, x_val=2, direction=DOWN, buff=1)
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(step_graph_left))
        self.play(Create(step_vertical_line))
        self.play(Create(step_graph_right), Write(step_graph_label))
        self.play(Create(sigmoid_graph), Write(sigmoid_graph_label))
        self.wait(3)
        
        self.play(FadeOut(step_graph_left), FadeOut(step_graph_right), FadeOut(step_vertical_line), FadeOut(step_graph_label), FadeOut(axes), FadeOut(axes_labels), FadeOut(sigmoid_graph), FadeOut(sigmoid_graph_label))
        self.wait(2)
