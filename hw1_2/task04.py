import numpy as np
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec4 import Vec4
from src.engine.model.Cube import Cube
from hw1_2.utils import *

obj = Cube(alpha=0.2)

cube = cube_points()

angle_z, angle_y, angle_x = 20, 35, 50

R = euler_zyx(angle_z, angle_y, angle_x)
T = translate(1, 3, -2)

tr1 = apply(cube, R)
print_points("Rotate", tr1)

tr2 = apply(cube, compose(R, T))
print_points("Final", tr2)

animations = [
    RotationAnimation(end=np.radians(angle_z), axis=Vec4(0, 0, 1), channel="object"),
    RotationAnimation(end=np.radians(angle_y), axis=Vec4(0, 1, 0), channel="object"),
    RotationAnimation(end=np.radians(angle_x), axis=Vec4(1, 0, 0), channel="object"),
    TranslationAnimation(end=Vec4(1, 3, -2), channel="object")
]

run_animations(animations, "Task 4", obj)