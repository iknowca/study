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
        
        for i in range(784):
            circle = Dot(color=BLUE)
            combo = VGroup(circle)
            iLayer.add(combo)
        iLayer.arrange(DOWN)
        
        for i in range(50):
            circle = Dot(color=BLUE)
            hLayer0.add(circle)
        hLayer0.arrange(DOWN)
            
        for i in range(100):
            circle = Dot(color=BLUE)
            hLayer1.add(circle)
        hLayer1.arrange(DOWN)
        
        
        for i in range(10):
            circle = Dot(color=BLUE)
            oLayer.add(circle)
        oLayer.arrange(DOWN)
        
        layers.arrange(RIGHT, buff=3)        
        self.add(layers)
        
        bias = Circle(radius=0.5, color=GREEN).next_to(iLayer, UP+RIGHT)
        label = MathTex("b^0").move_to(bias)
        combo = VGroup(bias, label)
        biases.add(combo)
        self.add(biases)
        
        for i, a in enumerate(hLayer0):
            arrows = VGroup()
            for j, x in enumerate(iLayer.add(bias)):
                arrow = Arrow(x.get_center(), a.get_center())
                arrows.add(arrow)
                weights0.add(arrow)
                self.play([Create(arrow) for arrow in arrows], run_time=0.1)
                self.play(FadeToColor(arrows, GREY), run_time=0.1)
    
        bias = Circle(radius=0.5, color=GREEN).next_to(hLayer0, UP+RIGHT)
        label = MathTex("b^1").move_to(bias)
        combo = VGroup(bias, label)
        biases.add(combo)
        self.play(Create(combo))
        
        for i, a in enumerate(hLayer1):
            arrows = VGroup()
            for j, x in enumerate(hLayer0.add(bias)):
                arrow = Arrow(x.get_center(), a.get_center())
                arrows.add(arrow)
                weights0.add(arrow)

                self.play([Create(arrow) for arrow in arrows], run_time=0.1)
                self.play(FadeToColor(arrows, GREY), run_time=0.1)
        
        bias = Circle(radius=0.5, color=GREEN).next_to(hLayer1, UP+RIGHT)
        label = MathTex("b^2").move_to(bias)
        combo = VGroup(bias, label)
        biases.add(combo)
        self.play(Create(combo))
        
        for i, a in enumerate(oLayer):
            arrows = VGroup()
            for j, x in enumerate(hLayer1.add(bias)):
                arrow = Arrow(x.get_center(), a.get_center())
                arrows.add(arrow)
                weights0.add(arrow)
                self.play([Create(arrow) for arrow in arrows], run_time=0.1)
                self.play(FadeToColor(arrows, GREY), run_time=0.1)
        pass