from manim import *

class main(Scene):
    def construct(self):
        title = Text("Step Function").shift(3*UP)
        self.add(title)
        
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-0.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes.shift(0.7* DOWN)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph_left = axes.plot(lambda x: 0, x_range=[-5, 0], color=ORANGE, use_smoothing=False)
        graph_right = axes.plot(lambda x: 1, x_range=[0, 5], color=ORANGE, use_smoothing=False)
        vertical_line = Line(
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            color=ORANGE
        )
        graph_label_text = Tex(r"""$
            h(x) = \begin{cases}
            0 & (x \leq 0) \\
            1 & (x > 0)
            \end{cases}
            $""")
        graph_label = axes.get_graph_label(graph_left, label=graph_label_text, x_val=-2, direction=UP)
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_left))
        self.play(Create(vertical_line))
        self.play(Create(graph_right), Write(graph_label))
        self.wait(3)
        
        self.play(FadeOut(graph_left), FadeOut(vertical_line), FadeOut(graph_right), FadeOut(graph_label), FadeOut(axes), FadeOut(axes_labels))
        self.wait(2)
