import numpy as np

def rotation_x(angle_deg):
    """Generate 3D rotation matrix about the X-axis for a given angle in degrees."""
    rad = np.radians(angle_deg)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([
        [1.0, 0.0, 0.0],
        [0.0,  c,  -s],
        [0.0,  s,   c]
    ], dtype=float)

def rotation_y(angle_deg):
    """Generate 3D rotation matrix about the Y-axis for a given angle in degrees."""
    rad = np.radians(angle_deg)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([
        [ c, 0.0,  s],
        [0.0, 1.0, 0.0],
        [-s, 0.0,  c]
    ], dtype=float)

def rotation_z(angle_deg):
    """Generate 3D rotation matrix about the Z-axis for a given angle in degrees."""
    rad = np.radians(angle_deg)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([
        [ c, -s, 0.0],
        [ s,  c, 0.0],
        [0.0, 0.0, 1.0]
    ], dtype=float)

def combined_rotation(x_deg, y_deg, z_deg):
    """Compute the combined rotation matrix R = Rz @ Ry @ Rx."""
    Rx = rotation_x(x_deg)
    Ry = rotation_y(y_deg)
    Rz = rotation_z(z_deg)
    return Rz @ Ry @ Rx
