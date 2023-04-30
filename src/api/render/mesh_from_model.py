from preprocess.point_cloud import subject_10_cp as pc
import open3d as o3d
import numpy as np
import pprint

# Open3D methods for generating meshes

subject_pc = o3d.geometry.PointCloud()
subject_pc.points = o3d.utility.Vector3dVector(pc[:, :3])


# Produce 3D scatter point visualisation from Cloud Points
def render_points():
    # subject_pc.colors = o3d.utility.Vector3dVector(point_cloud[:, 3:6] / 255)
    # subject_pc.normals = o3d.utility.Vector3dVector(point_cloud[:, 6:9])
    o3d.visualization.draw_geometries([subject_pc])


# Produce a Triangle Mesh from Cloud Points using the Ball-Pivoting Algorithm
def render_mesh_BPA():
    #Compute distance of every point to nearest neighbours
    distances = subject_pc.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 5 * avg_dist  #Choose a radius larger than the average distance

    #Generate normals from Cloud Points
    subject_pc.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamRadius(radius=100)
    )  #radius needs to be bigger than the average space between points

    #this points everything towards 0,0,0
    subject_pc.orient_normals_towards_camera_location()
    #point everything otward so triangles are visible
    subject_pc.normals = o3d.utility.Vector3dVector(
        np.asarray(subject_pc.normals) * -1)

    #Computes a triangle mesh from a oriented PointCloud. This implements the Ball Pivoting Algorithm
    bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        subject_pc,
        o3d.utility.DoubleVector([
            radius, radius * 1.1, radius * 1.2, radius * 1.3, radius * 1.4,
            radius * 1.5, radius * 1.6, radius * 1.7
        ]))

    #Simplify mesh using Quadric Error Metric Decimation by Garland and Heckbert
    NUM_TRIANGLES = 100000  #not guaranteed that this number will be reached
    dec_mesh = bpa_mesh.simplify_quadric_decimation(NUM_TRIANGLES)
    dec_mesh = dec_mesh.subdivide_loop(number_of_iterations=2)

    smooth_mesh = dec_mesh.filter_smooth_simple(number_of_iterations=10)
    print(type(smooth_mesh))
    smooth_mesh.compute_vertex_normals()
    smooth_mesh.paint_uniform_color([0.706, 0.706, 0.706])
    dec_mesh.paint_uniform_color([0.706, 0.706, 0.706])
    print(dec_mesh.has_vertex_colors())

    smooth_cloud = o3d.geometry.PointCloud()
    smooth_cloud.points = o3d.utility.Vector3dVector(
        np.asarray(smooth_mesh.vertices)[:, :3])

    # o3d.visualization.draw_geometries([dec_mesh])
    # o3d.visualization.draw_geometries([smooth_mesh])
    o3d.visualization.draw_geometries([subject_pc])


def get_mesh_from_point_cloud(pc):
    #Compute distance of every point to nearest neighbours
    distances = pc.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 5 * avg_dist  #Choose a radius larger than the average distance

    #Generate normals from Cloud Points
    pc.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamRadius(radius=100)
    )  #radius needs to be bigger than the average space between points
    #this points everything towards 0,0,0
    pc.orient_normals_towards_camera_location()
    #point everything otward so triangles are visible
    pc.normals = o3d.utility.Vector3dVector(np.asarray(pc.normals) * -1)

    #Computes a triangle mesh from a oriented PointCloud. This implements the Ball Pivoting Algorithm
    bpa_triangle_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        pc,
        o3d.utility.DoubleVector([
            radius, radius * 1.1, radius * 1.2, radius * 1.3, radius * 1.4,
            radius * 1.5, radius * 1.6, radius * 1.7
        ]))

    return bpa_triangle_mesh


# Smooth a mesh
def get_smooth_mesh_from_triangle_mesh(mesh, iterations):
    smooth_mesh = mesh.filter_smooth_simple(number_of_iterations=iterations)
    smooth_mesh.compute_vertex_normals()
    return smooth_mesh.remove_unreferenced_vertices()


def render(model):
    o3d.visualization.draw_geometries([model])


# Get points from mesh
def get_point_cloud_from_mesh(mesh):
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(
        np.asarray(mesh.vertices)[:, :3])
    return point_cloud


def compute_point_cloud_distance(control_cp, target_cp):
    return control_cp.compute_point_cloud_distance(target_cp)


# Find points with a distance larger than a constant from their closest point pair
def find_constant_points(control_cp, d):
    dists = np.asarray(d)
    ind = np.where(dists > 5)[0]
    constant_points = control_cp.select_by_index(ind)
    return constant_points


# Automatically extract landmarks as centroid of clusters extracted by Open3D
def cluster(pc):
    labels = pc.cluster_dbscan(10.5, 3)
    labels_arr = np.asarray(labels)
    pc_arr = np.asarray(pc.points)

    # Cluster points based on label
    point_dict = {}
    for i in range(labels_arr.size):
        if labels_arr[i] in point_dict:
            point_dict[labels_arr[i]].append(pc_arr[i])
        else:
            point_dict[labels_arr[i]] = [pc_arr[i]]

    #calculate mean of each cluster
    means_dict = {}
    for key in point_dict:
        means_dict[key] = np.array(point_dict[key]).mean(0)

    #generate new point cloud from means
    cluster_points_cloud_list = []
    for point in means_dict.values():
        cluster_points_cloud_list.append(point)
    cluster_points_cloud = np.array(cluster_points_cloud_list)
    pprint.pprint(cluster_points_cloud)

    cluster_pc = o3d.geometry.PointCloud()
    cluster_pc.points = o3d.utility.Vector3dVector(cluster_points_cloud[:, :3])
    cluster_pc.colors = o3d.utility.Vector3dVector(
        np.array([
            [1, 0, 0],
        ] * len(cluster_points_cloud_list)))
    return cluster_pc
