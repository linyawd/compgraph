import numpy as np
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4
from hw1_2.utils import *

cube = cube_points()

R_external = rot_z(60) @ rot_y(45) @ rot_x(30)
R_internal = rot_x(60) @ rot_y(45) @ rot_z(30)

print("External rotation matrix:")
print(R_external)
print("\nInternal rotation matrix:")
print(R_internal)
print("\nMatrices are equal:", np.allclose(R_external, R_internal))

tr_external = apply(cube, R_external)
tr_internal = apply(cube, R_internal)

print_points("Final coordinates (External)", tr_external)
print_points("Final coordinates (Internal)", tr_internal)
print("\nCoordinates match:", np.allclose(tr_external, tr_internal))

obj = Cube(alpha=0.5, color=(1, 0, 0))
obj_ref = Cube(alpha=0.3, color=(0, 0, 1))
obj_ref.transformation = R_internal

animations = [
    RotationAnimation(end=np.radians(30), axis=Vec4(1, 0, 0), channel="cube"),
    RotationAnimation(end=np.radians(45), axis=Vec4(0, 1, 0), channel="cube"),
    RotationAnimation(end=np.radians(60), axis=Vec4(0, 0, 1), channel="cube")
]

scene = AnimatedScene(title="Task 11", image_size=(10, 10), coordinate_rect=(-2, -2, -2, 3, 3, 3))
scene["cube"] = obj
scene["ref"] = obj_ref
scene.add_animations(*animations)
scene.show()