import open3d as o3d
import numpy as np
from pathlib import Path

if __name__ == "__main__":
    ROOT = Path(__file__).parent.parent
    DATA_PATH = ROOT / "data" / "bunny" / "reconstruction" / "bun_zipper.ply"

    point_cloud = o3d.io.read_point_cloud(DATA_PATH)
    print(point_cloud)
