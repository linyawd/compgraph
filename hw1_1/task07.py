from hw1_1.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation

square_pts = create_unit_square()

pivots = [(0.5, 0.5), (0, 1), (1, 1), (2, 2)]
angle = 60


for pivot in pivots:
    print(f"\n--- Pivot: {pivot} ---")

    rotation_mat = rotation_matrix(angle)
    transform_mat = around_point(rotation_mat, pivot)

    transformed = transform_points(square_pts, transform_mat)

    log_points(f"Після повороту на {angle}° навколо {pivot}", transformed)

    run_animation([
        RotationAnimation(end=np.radians(angle), frames=30, channel=FIGURE_ID)
    ], f"Task 7: Rotate {angle}° around pivot {pivot}", pivot=pivot)