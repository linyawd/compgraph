import numpy as np
from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex


TRS = np.array([
    [2.934, -0.416, 2.000],
    [0.624,  1.956, 3.400],
    [0.0,    0.0,   1.0]
])

points_global = np.array([
    [2,   3.4, 1],
    [4.9, 4,   1],
    [4.5, 6,   1],
    [1.6, 5.4, 1]
])

T_inv = np.linalg.inv(TRS)
print("Inverse matrix:\n", T_inv)

points_local = transform_points(points_global, T_inv)
log_points("Local points", points_local)


translation = TRS[0:2, 2]

sx = np.linalg.norm(TRS[0:2, 0])
sy = np.linalg.norm(TRS[0:2, 1])

angle = np.degrees(np.arctan2(TRS[1, 0], TRS[0, 0]))


run_animation([
    TranslationAnimation(end=vertex(*translation), frames=20, channel=FIGURE_ID),
    RotationAnimation(end=angle, frames=20, channel=FIGURE_ID),
    ScaleAnimation(end=(sx, sy), frames=20, channel=FIGURE_ID),
], "Task 11")