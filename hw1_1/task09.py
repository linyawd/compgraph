from hw1_1.utils import *
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex

square_pts = create_unit_square()

pivot = (1, 1)
sx, sy = 2, 1
dx, dy = 3, -2

scale_mat = scale_matrix(sx, sy)
translation_mat = translation_matrix(dx, dy)

# Розтяг (відносно pivot) → Переміщення
scale_around_pivot = around_point(scale_mat, pivot)
matrix_order1 = compose(translation_mat, scale_around_pivot)
transformed_order1 = transform_points(square_pts, matrix_order1)

log_points("Розтяг навколо pivot → Переміщення", transformed_order1)

run_animation([
    ScaleAnimation(end=vertex(sx, sy), frames=20, channel=FIGURE_ID),
    TranslationAnimation(end=vertex(dx, dy), frames=20, channel=FIGURE_ID)
], f"Task 9 Order 1: Scale around {pivot} → Translate ({dx},{dy})", pivot=pivot)

# Переміщення → Розтяг (відносно pivot)
translated_pivot = (pivot[0] + dx, pivot[1] + dy)
scale_around_translated_pivot = around_point(scale_mat, translated_pivot)
matrix_order2 = compose(scale_around_translated_pivot, translation_mat)
transformed_order2 = transform_points(square_pts, matrix_order2)

log_points("Переміщення → Розтяг навколо pivot", transformed_order2)

run_animation([
    TranslationAnimation(end=vertex(dx, dy), frames=20, channel=FIGURE_ID),
    ScaleAnimation(end=vertex(sx, sy), frames=20, channel=FIGURE_ID)
], f"Task 9 Order 2: Translate ({dx},{dy}) → Scale around {pivot}", pivot=pivot)