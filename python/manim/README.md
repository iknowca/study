# Manim

A Python package for math animation created by YouTuber 3Blue1Brown. Manim is a powerful tool for creating animations to help visualize mathematical concepts.

Short for "Mathematical Animation Engine", Manim is a Python library that allows you to create animations programmatically. It is particularly well-suited for creating animations that help visualize mathematical concepts.

It has FFmpeg, OpenGL, and Latex dependencies.

## why use manim?


## Installation

It's an official repository maintained by the original author, but since it's for his own use, the README recommends that users use the community version for backwards compatibility, documentation, testing, community interaction, and more.


### in Mac OS:
```bash
brew install py3cairo ffmpeg

# According to the documentation, additional dependencies are required for Apple silicon.
brew install pango pkg-config scipy

# Optional Dependencies 
# If you want to render equations, you'll also need to install LaTeX.
# The LaTeX distribution recommended by the official documentation is MacTex.
brew install --cask mactex-no-gui

# 

pip3 install manim
```
* py3cairo: A Python 3 binding for the Cairo graphics library.
* ffmpeg: A complete, cross-platform solution to record, convert, and stream audio and video.
* pango: A library for laying out and rendering text, with an emphasis on internationalization.
* pkg-config: A helper tool used when compiling applications and libraries.
* scipy: A Python library for scientific and technical computing.

# index
## tutorials
* [00_a_circle](tutorial/00_a_circle/00_a_circle.md)
* [01_transform_square_to_circle](tutorial/01_transform_square_to_circle/01_transform_squre_to_circle.md)
* [02_positioning_mobject](tutorial/02_positioning_mobject/positioning_mobject.md)
* [03_animate_syntax](tutorial/03_animate_syntax/animate_syntax.md)

## examples
* [basic_concepts](example_gallery/basic_concepts/basic_concepts.md)