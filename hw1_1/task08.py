from hw1_1.utils import *
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

square_pts = create_unit_square()

pivots = [(0.5, 0.5), (0, 1), (1, 1), (2, 2)]
sx, sy = 2, 3


for pivot in pivots:
    print(f"\n--- Pivot: {pivot} ---")

    scale_mat = scale_matrix(sx, sy)
    transform_mat = around_point(scale_mat, pivot)

    transformed = transform_points(square_pts, transform_mat)

    log_points(f"Після розтягу sx={sx}, sy={sy} навколо {pivot}", transformed)

    run_animation([
        ScaleAnimation(end=vertex(sx, sy), frames=30, channel=FIGURE_ID)
    ], f"Task 8: Scale sx={sx}, sy={sy} around pivot {pivot}", pivot=pivot)