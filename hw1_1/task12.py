import numpy as np
from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex


TRS = np.array([
    [0.866, 0.5, 4.000],
    [0.5,   0.866, 3.000],
    [0.0,   0.0,   1.0]
])

translation = TRS[0:2, 2]

sx = np.linalg.norm(TRS[0:2, 0])
sy = np.linalg.norm(TRS[0:2, 1])

angle = np.degrees(np.arctan2(TRS[1, 0], TRS[0, 0]))


run_animation([
    TranslationAnimation(end=vertex(*translation), frames=20, channel=FIGURE_ID),
    RotationAnimation(end=angle, frames=20, channel=FIGURE_ID),
    ScaleAnimation(end=(sx, sy), frames=20, channel=FIGURE_ID),
], "Task 12")