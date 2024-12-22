# transform_square_to_circle
A description of the SqureToCircle animation code created using Manim.
```python
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)
        square.set_fill(BLUE, opacity=0.5)
        self.camera.background_color = WHITE

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.wait()
```
1. using Squre(), squre is created. and rotate() is used to rotated the squre by PI/4.

2. using Create() to run an animation that draws a squre.

3. using Transform() to transform the squre into a circle.

4. using wait() to pause the animation at the end.

# Result of the animation
![result](SquareToCircle_ManimCE_v0.18.1.gif)

This example shows that complex, mathematical changes can be implemented in just a few lines.