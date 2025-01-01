from manim import *

class main(Scene):
    def construct(self):
        title = Text("Sigmoid Function").shift(3*UP)
        self.add(title)
        
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-0.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes.shift(0.7* DOWN)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: 1/(1+np.exp(-x)), x_range=[-5, 5], color=ORANGE, use_smoothing=False)

        graph_label_text = Tex(r"""$
            h(x) = \frac{1}{1 + e^{-x}}
            $""")
        graph_label = axes.get_graph_label(graph, label=graph_label_text, x_val=-2, direction=UP*2)
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(3)
        
        self.play(FadeOut(graph), FadeOut(graph_label), FadeOut(axes), FadeOut(axes_labels))
        self.wait(2)
