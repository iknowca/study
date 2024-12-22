# 00_a_circle
## Create a circle
The first thing made by manim is a circle. The following code creates a blue circle with a white background.

```python
from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.camera.background_color = WHITE

        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(circle))
```

## Render the animation

To render the animation, run the following command in the terminal:

```bash
manim -pql 00_a_circle.py CreateCircle
```
* -p: Preview the animation once it's done rendering
* -ql: Low quality

## Render the animation as a GIF

To render the animation as a GIF, run the following command in the terminal:

```bash
manim -pql --format gif a_circle.py CreateCircle
```

## Result of the animation
![result](a_circle.gif)

## About the code
* ```class CreateCircle(Scene):```
* ```def construct(self):``` The construct method is used to construct the scene in Manim.
* ```circle = Circle()``` Creates a Circle object.
* ```self.camera.background_color = WHITE``` Sets the background color of the camera to white.
* ```circle.set_fill(BLUE, opacity=0.5)``` Fills the circle with blue color and sets the opacity to 0.5.
* ```self.play(Create(circle))``` Plays the animation to create the circle.

> Function code for auxiliary functions or math can be placed outside the class, but all animations must be inside the construct() method of the class that inherits from Scene.