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
```

[]: # (END)

[]: # (BEGIN)[]
