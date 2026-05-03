import numpy as np
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec4 import Vec4
from src.engine.model.Cube import Cube
from hw1_2.utils import *

obj = Cube(alpha=0.2)
obj.pivot(1, 2, 3)
obj.show_pivot()

cube = cube_points()
pivot = (1, 2, 3)

S = around_point(scale(1, 1, 3), pivot)
R = around_point(rot_axis(30, (1, 0, 0)), pivot)

tr1 = apply(cube, S)
print_points("Scale", tr1)

tr2 = apply(cube, compose(S, R))
print_points("Final", tr2)

animations = [
    ScaleAnimation(end=Vec4(1, 1, 3), channel="object"),
    RotationAnimation(end=np.radians(30), axis=Vec4(1, 0, 0), channel="object")
]

run_animations(animations, "Task 7", obj)