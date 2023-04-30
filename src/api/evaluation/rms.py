import open3d as o3d
import math
import numpy as np


# Calculate the RMSE
def calculate_rms_distance(subject, atlas):
    source = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(subject[:, :3])

    target = o3d.geometry.PointCloud()
    target.points = o3d.utility.Vector3dVector(atlas[:, :3])

    dists = source.compute_point_cloud_distance(target)
    dists = np.asarray(dists)
    sq_dists = np.square(dists)
    mean_dist = np.mean(sq_dists)
    rmsd = math.sqrt(mean_dist)

    return rmsd
