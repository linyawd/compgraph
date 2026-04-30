from hw1_1.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

square_pts = create_unit_square()

scale_mat = scale_matrix(1, 3)
rotation_mat = rotation_matrix(60)
translation_mat = translation_matrix(2, 3)

# Розтяг → Поворот → Переміщення
matrix_order1 = compose(translation_mat, rotation_mat, scale_mat)
transformed_order1 = transform_points(square_pts, matrix_order1)

log_points("Розтяг → Поворот → Переміщення", transformed_order1)

# Переміщення → Розтяг → Поворот
matrix_order2 = compose(rotation_mat, scale_mat, translation_mat)
transformed_order2 = transform_points(square_pts, matrix_order2)

log_points("Переміщення → Розтяг → Поворот", transformed_order2)

# Візуалізація (окремо для кожного порядку)

run_animation([
    ScaleAnimation(end=vertex(1, 3), frames=15, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(60), frames=15, channel=FIGURE_ID),
    TranslationAnimation(end=vertex(2, 3), frames=15, channel=FIGURE_ID)
], "Task 6 Order 1: Scale → Rotate → Translate")

run_animation([
    TranslationAnimation(end=vertex(2, 3), frames=15, channel=FIGURE_ID),
    ScaleAnimation(end=vertex(1, 3), frames=15, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(60), frames=15, channel=FIGURE_ID)
], "Task 6 Order 2: Translate → Scale → Rotate")