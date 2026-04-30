from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex


square_pts = create_unit_square()

rotated = transform_points(square_pts, rotation_matrix(90))
log_points("Поворот 90°", rotated)

translated = transform_points(rotated, translation_matrix(2, 3))
log_points("Переміщення (2,3)", translated)


run_animation([
    RotationAnimation(end=np.radians(90), frames=20, channel=FIGURE_ID),
    TranslationAnimation(end=vertex(2, 3), frames=20, channel=FIGURE_ID)
], "Task 3: Rotation 90° then Translation (2,3)")