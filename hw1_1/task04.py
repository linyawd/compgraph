from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex


square_pts = create_unit_square()

scaled = transform_points(square_pts, scale_matrix(1, 3))
log_points("Розтяг по y у 3 рази", scaled)

rotated = transform_points(scaled, rotation_matrix(60))
log_points("Поворот 60°", rotated)


run_animation([
    ScaleAnimation(end=vertex(1, 3), frames=20, channel=FIGURE_ID),
    RotationAnimation(end=np.radians(60), frames=20, channel=FIGURE_ID)
], "Task 4: Scale y3 then Rotate 60°")