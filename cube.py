import numpy as np

def get_cube_vertices():
    """Return the 8 vertices of a cube centered at the origin."""
    return np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ], dtype=float)

def get_cube_edges():
    """Return pairs of vertex indices for the 12 cube edges."""
    return [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
            (0,4),(1,5),(2,6),(3,7)]
