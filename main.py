import numpy as np
from cube import get_cube_vertices, get_cube_edges
from rotations import rotation_x, rotation_y, rotation_z, combined_rotation

def main():
    print("3D OBJECT ROTATION USING ORTHOGONAL MATRICES - COMPUTATION MODULE")
    try:
        x = float(input("Rotation about X axis (degrees): "))
        y = float(input("Rotation about Y axis (degrees): "))
        z = float(input("Rotation about Z axis (degrees): "))
    except ValueError:
        print("Please enter numeric angles, such as 30 or -45.")
        return
    
    rx, ry, rz = rotation_x(x), rotation_y(y), rotation_z(z)
    R = combined_rotation(x, y, z)
    original = get_cube_vertices()
    
    # Vertices are stored as row vectors, so transform via R.T
    rotated = original @ R.T
    
    for name, matrix in [("Rx", rx), ("Ry", ry), ("Rz", rz), ("Combined R = Rz @ Ry @ Rx", R)]:
        print(f"\n{name}:\n{np.array2string(matrix, precision=4, suppress_small=True)}")
        
    print("\nTransformed vertices:")
    for i, p in enumerate(rotated, start=1):
        print(f"Vertex {i}: ({p[0]:.4f}, {p[1]:.4f}, {p[2]:.4f})")

if __name__ == "__main__":
    main()
