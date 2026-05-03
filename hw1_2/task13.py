import numpy as np
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4
from hw1_2.task05 import Tetrahedron
from hw1_2.utils import *

obj = Tetrahedron(alpha=0.2)
tetra = tetra_points()
print_points("Initial", tetra)

M = np.eye(4)
M = M @ rot_x(45)
tr1 = apply(tetra, M)
print_points("Rotate X 45°", tr1)

local_y = M[:3, 1] / np.linalg.norm(M[:3, 1])
T = translate(local_y[0] * 2, local_y[1] * 2, local_y[2] * 2)
M = M @ T
tr2 = apply(tetra, M)
print_points("Move along local Y 2 units", tr2)

local_z = M[:3, 2] / np.linalg.norm(M[:3, 2])
R = rot_axis(30, local_z)
M = M @ R
tr3 = apply(tetra, M)
print_points("Rotate around local Z 30°", tr3)

animations = [
    RotationAnimation(end=np.radians(45), axis=Vec4(1, 0, 0), channel="object"),
    TranslationAnimation(end=Vec4(local_y[0] * 2, local_y[1] * 2, local_y[2] * 2), channel="object"),
    RotationAnimation(end=np.radians(30), axis=Vec4(local_z[0], local_z[1], local_z[2]), channel="object")
]

run_animations(animations, "Task 13", obj)