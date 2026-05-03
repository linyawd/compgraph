import numpy as np
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4
from hw1_2.utils import *

M = compose(
    scale(1.5, 2, 0.5),
    rot_axis(60, (1, 0, 1)),
    translate(4, -1, 3)
)

print("Matrix:\n", M)

t = M[:3, 3]
print("\n1. Translation vector:", t)

sx = np.linalg.norm(M[:3, 0])
sy = np.linalg.norm(M[:3, 1])
sz = np.linalg.norm(M[:3, 2])
print("\n2. Scale factors:", (sx, sy, sz))

R = M[:3, :3] / np.array([sx, sy, sz])
print("\n3. Pure rotation matrix:\n", R)

is_orthogonal = np.allclose(R @ R.T, np.eye(3))
print(f"\nRotation matrix is orthogonal: {is_orthogonal}")
print(f"Determinant: {np.linalg.det(R):.3f}")

angle = np.arccos((np.trace(R) - 1) / 2)
angle_deg = np.degrees(angle)
print(f"\n4. Rotation angle: {angle_deg:.3f}°")

axis = np.array([
    R[2, 1] - R[1, 2],
    R[0, 2] - R[2, 0],
    R[1, 0] - R[0, 1]
]) / (2 * np.sin(angle))
print(f"   Rotation axis: ({axis[0]:.3f}, {axis[1]:.3f}, {axis[2]:.3f})")

obj = Cube(alpha=0.5, color=(1, 0, 0))
obj.transformation = M

cube_points_obj = cube_points()
transformed_points = apply(cube_points_obj, M)
print_points("\nFinal cube coordinates", transformed_points)

scene = AnimatedScene(title="Task 12 - Matrix Decomposition", image_size=(10, 10), coordinate_rect=(-2, -2, -2, 6, 6, 6))
scene["cube"] = obj
scene.show()