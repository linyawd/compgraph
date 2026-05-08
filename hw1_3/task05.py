from hw1_3.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)
obj.show_local_frame()


cube = cube_points()

OX = Vec4(1, 0, 0)
OY = Vec4(0, 1, 0)
OZ = Vec4(0, 0, 1)

R1 = rot_x(30) @ rot_y(90) @ rot_z(45)
tr1 = apply(cube, R1)
print_points("Rotate (30, 90, 45)", tr1)

R2 = rot_x(40) @ rot_y(90) @ rot_z(35)
tr2 = apply(cube, R2)
print_points("Rotate (40, 90, 35)", tr2)

obj_ref = Cube(alpha=0.2, color=(0, 0, 1))
obj_ref.transformation = R2

animation_x = RotationAnimation(
    end=np.radians(30),
    axis=OX,
    channel="object",
)

Rx = rot_x(30)
OY1 = apply(np.array([[OY.x, OY.y, OY.z, 0]]), Rx)[0][:3]
OY1 = Vec4(OY1[0], OY1[1], OY1[2])

animation_y = RotationAnimation(
    end=np.radians(90),
    axis=OY1,
    channel="object",
)

rot_y = rot_axis(90, (OY1.x, OY1.y, OY1.z))
OZ1 = apply(np.array([[OZ.x, OZ.y, OZ.z, 0]]), rot_x(30))[0][:3]
OZ2 = apply(np.array([[OZ1[0], OZ1[1], OZ1[2], 0]]), rot_y)[0][:3]
OZ2 = Vec4(OZ2[0], OZ2[1], OZ2[2])

animation_z = RotationAnimation(
    end=np.radians(45),
    axis=OZ2,
    channel="object",
)

scene = AnimatedScene(
    title="Task 5",
    image_size=(8, 8),
    coordinate_rect=(-1, -1, -1, 5, 5, 5),
)

scene["object"] = obj
scene["ref_cube"] = obj_ref

scene.add_animations(animation_x, animation_y, animation_z)
scene.show()