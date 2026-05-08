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

S = scale(2, 0.5, 1)
tr1 = apply(cube, S)
print_points("Scale", tr1)

R = rot_x(30) @ rot_y(45) @ rot_z(60)
tr2 = apply(cube, compose(S, R))
print_points("Scale + Rotate (30, 45, 60)", tr2)

T = translate(-3, 2, 5)
tr3 = apply(cube, compose(S, R, T))
print_points("Final", tr3)

animation_x = RotationAnimation(
    end=np.radians(30),
    axis=OX,
    channel="object",
)

Rx = rot_x(30)
OY1 = apply(np.array([[OY.x, OY.y, OY.z, 0]]), Rx)[0][:3]
OY1 = Vec4(OY1[0], OY1[1], OY1[2])

animation_y = RotationAnimation(
    end=np.radians(45),
    axis=OY1,
    channel="object",
)

rot_y = rot_axis(45, (OY1.x, OY1.y, OY1.z))
OZ1 = apply(np.array([[OZ.x, OZ.y, OZ.z, 0]]), rot_x(30))[0][:3]
OZ2 = apply(np.array([[OZ1[0], OZ1[1], OZ1[2], 0]]), rot_y)[0][:3]
OZ2 = Vec4(OZ2[0], OZ2[1], OZ2[2])

animation_z = RotationAnimation(
    end=np.radians(60),
    axis=OZ2,
    channel="object",
)

animations = [
    ScaleAnimation(end=Vec4(2,0.5,1), channel="object"),
    animation_x, animation_y, animation_z,
    TranslationAnimation(end=Vec4(-3,2,5), channel="object")
]

run_animations(animations, "Task 1", obj)