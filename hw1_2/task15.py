import numpy as np
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4
from hw1_2.utils import *

obj = Cube(alpha=0.2)
cube = cube_points()
pivot = (1, 1, 1)

S = around_point(scale(2, 2, 2), pivot)
scaled_cube = apply(cube, S)
new_origin = scaled_cube[0]
new_pivot = (new_origin[0], new_origin[1], new_origin[2])

R = around_point(rot_y(90), new_pivot)
T = translate(-3, 4, 2)

M = T @ R @ S

tr = apply(cube, M)
print_points("Final coordinates", tr)

def decompose_affine(M):
    t = M[:3, 3]
    sx = np.linalg.norm(M[:3, 0])
    sy = np.linalg.norm(M[:3, 1])
    sz = np.linalg.norm(M[:3, 2])
    R_pure = M[:3, :3] / np.array([sx, sy, sz])
    trace = np.trace(R_pure)
    angle_rad = np.arccos(np.clip((trace - 1) / 2, -1, 1))
    angle_deg = np.degrees(angle_rad)
    axis = np.array([
        R_pure[2, 1] - R_pure[1, 2],
        R_pure[0, 2] - R_pure[2, 0],
        R_pure[1, 0] - R_pure[0, 1]
    ]) / (2 * np.sin(angle_rad))
    return t, (sx, sy, sz), axis, angle_deg

t, scale_factors, rot_axis, rot_angle = decompose_affine(M)
print(f"\nDecomposed:\nTranslation: {t}\nScale: {scale_factors}\nRotation axis: {rot_axis}\nRotation angle: {rot_angle:.2f}°")

animations = [
    ScaleAnimation(end=Vec4(2, 2, 2), channel="object"),
    RotationAnimation(end=np.radians(90), axis=Vec4(0, 1, 0), channel="object"),
    TranslationAnimation(end=Vec4(-3, 4, 2), channel="object")
]

run_animations(animations, "Task 15", obj)