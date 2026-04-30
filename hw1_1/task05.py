from hw1_1.utils import *

from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex


square_pts = create_unit_square()

translated = transform_points(square_pts, translation_matrix(1, -1))
log_points("Переміщення (1,-1)", translated)

scaled = transform_points(translated, scale_matrix(2, 2))
log_points("Масштабування x2", scaled)


run_animation([
    TranslationAnimation(end=vertex(1, -1), frames=20, channel=FIGURE_ID),
    ScaleAnimation(end=vertex(2, 2), frames=20, channel=FIGURE_ID)
], "Task 5: Translation (1,-1) then Scale x2")