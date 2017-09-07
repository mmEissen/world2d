# World2D

A widget that implements a 2d world space, which can be dragged and zoomed.

## Requirements

Because this package builds on PyQt5 you will need to use at least Python 3.5.

## Installation

This package is listed on PyPI, simply run:
```
pip install world2d
```

Or, if you want to install the module in edit mode, clone this repository and from it's root directory run:
```
pip install -e .
```

## Usage

*Check out `example.py` for an example usage.*

Subclass `world2d.widgets.World2D` and override the paintEvent method. Instead of instantiating a new `QPainter` use the `World2D.world_painter()` method to create a world painter whith the necessary transformations.

Anything you draw with the painter will be transformed into world space. You can move your view by draging and zoom using the scroll wheel (or your touch pads scroll function).

## TODO

- A center function to center the view on a `QRect`
-
