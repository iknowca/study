from manim import *

class main(Scene):
    def construct(self):
        
        layers = VGroup()
        iLayer = VGroup()
        hLayer0 = VGroup()
        hLayer1 = VGroup()
        oLayer = VGroup()
        layers.add(iLayer, hLayer0, hLayer1, oLayer)
        biases = VGroup()
        
        weights = VGroup()
        weights0 = VGroup()
        weights1 = VGroup()
        weights2 = VGroup()
        weights.add(weights0, weights1, weights2)
        
        for i in range(2):
            circle = Circle(radius=0.5, color=BLUE)
            label = MathTex("x_{}".format(i)).move_to(circle)
            combo = VGroup(circle, label)
            iLayer.add(combo)
        iLayer.arrange(DOWN, buff=2)
        
        for i in range(3):
            circle = Circle(radius=0.5, color=BLUE)
            hLayer0.add(circle)
        hLayer0.arrange(DOWN, buff=1.5)
            
        for i in range(2):
            circle = Circle(radius=0.5, color=BLUE)
            hLayer1.add(circle)
        hLayer1.arrange(DOWN, buff=2)
        
        
        for i in range(2):
            circle = Circle(radius=0.5, color=BLUE)
            oLayer.add(circle)
        oLayer.arrange(DOWN, buff=2)
        
        layers.arrange(RIGHT, buff=3)        
        self.add(layers)
        
        bias = Circle(radius=0.5, color=GREEN).next_to(iLayer, UP+RIGHT)
        label = MathTex("b^0_0").move_to(bias)
        combo = VGroup(bias, label)
        biases.add(combo)
        self.add(biases)
        
        for i, a in enumerate(hLayer0):
            arrows = VGroup()
            for j, x in enumerate(iLayer.add(bias)):
                arrow = Arrow(x.get_center(), a.get_center(), buff=1)
                arrows.add(arrow)
                weights0.add(arrow)
            self.play([Create(arrow) for arrow in arrows])
            text = MathTex("a^0_{}".format(i)).move_to(a)
            self.play(Write(text), a.animate.set_color(RED), FadeToColor(arrows, GREY))
        
        bias = Circle(radius=0.5, color=GREEN).next_to(hLayer0, UP+RIGHT)
        label = MathTex("b^1_0").move_to(bias)
        combo = VGroup(bias, label)
        biases.add(combo)
        self.play(Create(combo))
        
        for i, a in enumerate(hLayer1):
            arrows = VGroup()
            for j, x in enumerate(hLayer0.add(bias)):
                arrow = Arrow(x.get_center(), a.get_center(), buff=1)
                arrows.add(arrow)
                weights0.add(arrow)
            self.play([Create(arrow) for arrow in arrows])
            text = MathTex("a^1_{}".format(i)).move_to(a)
            self.play(Write(text), a.animate.set_color(RED), FadeToColor(arrows, GREY))
                   
        bias = Circle(radius=0.5, color=GREEN).next_to(hLayer1, UP+RIGHT)
        label = MathTex("b^2_0").move_to(bias)
        combo = VGroup(bias, label)
        biases.add(combo)
        self.play(Create(combo))
        
        for i, a in enumerate(oLayer):
            arrows = VGroup()
            for j, x in enumerate(hLayer1.add(bias)):
                arrow = Arrow(x.get_center(), a.get_center(), buff=1)
                arrows.add(arrow)
                weights0.add(arrow)
            self.play([Create(arrow) for arrow in arrows])
            text = MathTex("y_{}".format(i)).move_to(a)
            self.play(Write(text), a.animate.set_color(RED), FadeToColor(arrows, GREY))
        pass