from hw1_1.utils import *
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex

square_pts = create_unit_square()

pivot = (0.5, 0.5)
sx, sy = 2, 2
angle = 30
dx, dy = 1, -1

scale_mat = scale_matrix(sx, sy)
rotation_mat = rotation_matrix(angle)
translation_mat = translation_matrix(dx, dy)

scale_around_pivot = around_point(scale_mat, pivot)
rotation_around_pivot = around_point(rotation_mat, pivot)

matrix_order1 = compose(translation_mat, rotation_around_pivot, scale_around_pivot)
transformed_order1 = transform_points(square_pts, matrix_order1)

log_points("Масштабування → Обертання → Зсув", transformed_order1)

translated_pivot = (pivot[0] + dx, pivot[1] + dy)
scale_around_translated_pivot = around_point(scale_mat, translated_pivot)
rotation_around_translated_pivot = around_point(rotation_mat, translated_pivot)

matrix_order2 = compose(rotation_around_translated_pivot, scale_around_translated_pivot, translation_mat)
transformed_order2 = transform_points(square_pts, matrix_order2)

log_points("Зсув → Масштабування → Обертання", transformed_order2)

translated_pivot_for_rot = (pivot[0] + dx, pivot[1] + dy)
rotation_around_final_pivot = around_point(rotation_mat, translated_pivot_for_rot)

matrix_order3 = compose(rotation_around_final_pivot, translation_mat, scale_around_pivot)
transformed_order3 = transform_points(square_pts, matrix_order3)

log_points("Масштабування → Зсув → Обертання", transformed_order3)

run_animation([
    ScaleAnimation(end=vertex(sx, sy), frames=15, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(angle), frames=15, channel=FIGURE_ID),
    TranslationAnimation(end=vertex(dx, dy), frames=15, channel=FIGURE_ID)
], "Task 10 Order 1: Scale → Rotate → Translate", pivot=pivot)

run_animation([
    TranslationAnimation(end=vertex(dx, dy), frames=15, channel=FIGURE_ID),
    ScaleAnimation(end=vertex(sx, sy), frames=15, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(angle), frames=15, channel=FIGURE_ID)
], f"Task 10 Order 2: Translate → Scale → Rotate (pivot={translated_pivot})", pivot=pivot)

run_animation([
    ScaleAnimation(end=vertex(sx, sy), frames=15, channel=FIGURE_ID),
    TranslationAnimation(end=vertex(dx, dy), frames=15, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(angle), frames=15, channel=FIGURE_ID)
], f"Task 10 Order 3: Scale → Translate → Rotate (pivot={translated_pivot_for_rot})", pivot=pivot)