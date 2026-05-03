import numpy as np
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec4 import Vec4
from src.engine.model.Cube import Cube
from hw1_2.utils import *

obj = Cube(alpha=0.2)

cube = cube_points()

angle_x, angle_y, angle_z = 30, 45, 60

S = scale(2, 0.5, 1)
R = euler_xyz(angle_x, angle_y, angle_z)
T = translate(-3, 2, 5)

tr1 = apply(cube, S)
print_points("Scale", tr1)

tr2 = apply(cube, compose(S, R))
print_points("Scale + Rotate", tr2)

tr3 = apply(cube, compose(S, R, T))
print_points("Final", tr3)

animations = [
    ScaleAnimation(end=Vec4(2, 0.5, 1), channel="object"),
    RotationAnimation(end=np.radians(angle_x), axis=Vec4(1, 0, 0), channel="object"),
    RotationAnimation(end=np.radians(angle_y), axis=Vec4(0, 1, 0), channel="object"),
    RotationAnimation(end=np.radians(angle_z), axis=Vec4(0, 0, 1), channel="object"),
    TranslationAnimation(end=Vec4(-3, 2, 5), channel="object")
]

run_animations(animations, "Task 2", obj)