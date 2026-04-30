from hw1_1.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

square_pts = create_unit_square()

scale_mat = scale_matrix(2, 1)
rotation_mat = rotation_matrix(45)

scaled = transform_points(square_pts, scale_mat)
log_points("Scale", scaled)

rotated = transform_points(scaled, rotation_mat)
log_points("Rotation 45°", rotated)


run_animation([
    ScaleAnimation(end=vertex(2, 1), frames=20, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(45), frames=20, channel=FIGURE_ID)
], "Task 2: Scale x2 then Rotate 45°")