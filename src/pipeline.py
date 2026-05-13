import open3d as o3d
import numpy as np
from pathlib import Path

if __name__ == "__main__":
    ROOT = Path(__file__).parent.parent
    DATA_PATH = ROOT / "data" / "bunny" / "reconstruction" / "bun_zipper.ply"

    pcd = o3d.io.read_point_cloud(DATA_PATH)
    print(pcd)

    voxel_size = 0.005
    downsampled_pcd = pcd.voxel_down_sample(voxel_size)
    print(downsampled_pcd)

    nb_neighbors = 20
    std_ratio = 2.0
    clean_pcd, indices = downsampled_pcd.remove_statistical_outlier(nb_neighbors, std_ratio)
    print(clean_pcd)

    radius = 2 * voxel_size
    max_nn = 30
    clean_pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius, max_nn))
    clean_pcd.orient_normals_consistent_tangent_plane(10)
    print(len(clean_pcd.normals))

    radius = 5 * voxel_size
    max_nn = 100
    fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        clean_pcd,
        o3d.geometry.KDTreeSearchParamHybrid(radius, max_nn)
    )
    print(fpfh.data.shape)
