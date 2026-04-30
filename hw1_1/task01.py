from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex


square_pts = create_unit_square()

rotated = transform_points(square_pts, rotation_matrix(30))
log_points("Поворот 30°", rotated)

translated = transform_points(rotated, translation_matrix(2, 3))
log_points("Переміщення (2,3)", translated)


run_animation([
    RotationAnimation(end=np.radians(30), frames=20, channel=FIGURE_ID),
    TranslationAnimation(end=vertex(2, 3), frames=20, channel=FIGURE_ID)
], "Task 1")