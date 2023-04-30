import numpy as np
import open3d as o3d

# Methods for the API


# Generate only the point cloud from the user input PLY file for registration
def get_point_cloud_from_user_input():
    ply_file = "./data/user_input/read_ply_file.ply"
    ptCloud = o3d.io.read_point_cloud(ply_file)
    ptCloud_numpy = np.asarray(ptCloud.points)
    return ptCloud_numpy


# Get only top of head for the haemodynamics visualisation section
def get_top_of_head_from_user_input():
    whole_head = get_point_cloud_from_user_input()
    rows = np.where(whole_head[:, 2] > -70)
    top_of_head_cp = whole_head[rows]
    return top_of_head_cp


# Write registered subject into the file
def write_registered_points(reg_pc):
    ply_file = "./data/user_input/read_ply_file.ply"
    ptCloud = o3d.io.read_point_cloud(ply_file)
    ptCloud.points = o3d.utility.Vector3dVector(reg_pc)
    o3d.io.write_point_cloud("./data/user_input/reg_ply_file.ply",
                             ptCloud,
                             write_ascii=True)
