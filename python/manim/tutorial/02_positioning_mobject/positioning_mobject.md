# Positioning Mobjects

A description of the PositioningMobjects animation code created using Manim.
This code covers how to use the next_to method to set the relative position between shapes.

```python
class PositioningMobject(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, LEFT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
```

Use the next_to() method to place the squre to the left of the circle.
The buff parameter is used to set the distance between the two shapes.
and to change the position, change the LEFT parameter to RIGHT, UP, or DOWN.

# Result of the animation
![result](PositioningMobject_ManimCE_v0.18.1.gif)