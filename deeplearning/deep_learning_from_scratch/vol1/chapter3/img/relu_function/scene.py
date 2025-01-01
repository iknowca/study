from manim import *

class main(Scene):
    def construct(self):
        title = Text("ReLU Function").shift(3*UP)
        self.add(title)
        
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-0.5, 5],
            axis_config={"color": BLUE},
        )
        axes.shift(0.7* DOWN)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph_left = axes.plot(lambda x: 0, x_range=[-5, 0], color=ORANGE, use_smoothing=False)
        graph_right = axes.plot(lambda x: x, x_range=[0, 5], color=ORANGE, use_smoothing=False)

        graph_label_text = Tex(r"""$
            h(x) = \begin{cases}
            0 & (x \leq 0) \\
            x & (x > 0)
            \end{cases}
            $""")
        graph_label = axes.get_graph_label(graph_left, label=graph_label_text, x_val=-2, direction=UP, buff=3)
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_left))
        self.play(Create(graph_right), Write(graph_label))
        self.wait(3)
        
        self.play(FadeOut(graph_left), FadeOut(graph_right), FadeOut(graph_label), FadeOut(axes), FadeOut(axes_labels))
        self.wait(2)
