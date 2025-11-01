from manim import *
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(ROOT))
import env.light_theme
# manim -p -qm -s neuralnet.py

class NeuralNet(Scene):
    def construct(self):
        # Create layers
        input_layer = VGroup(*[Circle(radius=0.2, color=BLUE) for i in range(2)]).arrange(DOWN, buff=0.5)
        hidden_layer = VGroup(*[Circle(radius=0.2, color=GREEN) for i in range(3)]).arrange(DOWN, buff=0.5)
        output_layer = VGroup(*[Circle(radius=0.2, color=RED) for i in range(2)]).arrange(DOWN, buff=0.5)

        # Position layers
        input_layer.next_to(ORIGIN, LEFT, buff=1)
        output_layer.next_to(ORIGIN, RIGHT, buff=1) 
        # Create connections
        connections = VGroup()
        for input_neuron in input_layer:
            for hidden_neuron in hidden_layer:
                connections.add(Arrow(input_neuron.get_right(), hidden_neuron.get_left(), color=GRAY, stroke_width=2, tip_length=0.1, buff=0.1))
        for hidden_neuron in hidden_layer:
            for output_neuron in output_layer:
                connections.add(Arrow(hidden_neuron.get_right(), output_neuron.get_left(), color=GRAY, stroke_width=2, tip_length=0.1, buff=0.1))
                
        # Create Labels
        input_label = Text("Input Layer", color=BLUE, font_size=14).next_to(input_layer, UP)
        hidden_label = Text("Hidden Layer", color=GREEN, font_size=14).next_to(hidden_layer, UP)
        output_label = Text("Output Layer", color=RED, font_size=14).next_to(output_layer, UP)

        input_label.set_y(hidden_label.get_y())
        output_label.set_y(hidden_label.get_y())

        # Add layers and connections to the scene
        self.add(input_layer, hidden_layer, output_layer, connections, input_label, hidden_label, output_label)
        self.wait(2)