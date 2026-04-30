import numpy as np
from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex


TRS = np.array([
    [1.732, -1, 5],
    [1, 1.732, -3],
    [0, 0, 1]
])

pivot = (1, 1)

T_no_pivot = compose(
    translation_matrix(-pivot[0], -pivot[1]),
    TRS,
    translation_matrix(pivot[0], pivot[1])
)

translation = T_no_pivot[0:2, 2]

sx = np.linalg.norm(T_no_pivot[0:2, 0])
sy = np.linalg.norm(T_no_pivot[0:2, 1])

angle = np.degrees(np.arctan2(T_no_pivot[1, 0], T_no_pivot[0, 0]))


run_animation([
    TranslationAnimation(end=vertex(*translation), frames=20, channel=FIGURE_ID),
    RotationAnimation(end=angle, frames=20, channel=FIGURE_ID),
    ScaleAnimation(end=(sx, sy), frames=20, channel=FIGURE_ID),
], "Task 14", pivot=pivot)