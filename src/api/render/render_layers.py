from preprocess.layers import skin_layer, skull_layer, CSF_layer
import open3d as o3d
import numpy as np
import pprint

# Initial experimentation with using Open3D as the visualisation tool
# for the second part of the project


# Get the atlas layers
def get_layers_pc():
    layers = []

    pc_skin = o3d.geometry.PointCloud()
    pc_skin.points = o3d.utility.Vector3dVector(skin_layer[:, :3])
    layers.append(pc_skin)

    pc_skull = o3d.geometry.PointCloud()
    pc_skull.points = o3d.utility.Vector3dVector(skull_layer[:, :3])
    layers.append(pc_skull)

    pc_CSF = o3d.geometry.PointCloud()
    pc_CSF.points = o3d.utility.Vector3dVector(CSF_layer[:, :3])
    pc_CSF.paint_uniform_color([0.8509, 0.6470, 0.6980])
    layers.append(pc_CSF)

    return layers


# Generate meshes from layer point clouds
def get_mesh_from_point_cloud(pc):
    #Compute distance of every point to nearest neighbours
    distances = pc.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 5 * avg_dist  #Choose a radius larger than the average distance

    #Generate normals from Cloud Points
    pc.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamRadius(radius=20)
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


# Mesh smoothing
def get_smooth_mesh_from_triangle_mesh(mesh, iterations):
    smooth_mesh = mesh.filter_smooth_simple(number_of_iterations=iterations)
    smooth_mesh.compute_vertex_normals()
    return smooth_mesh.remove_unreferenced_vertices()


def render(model):
    o3d.visualization.draw_geometries([model])


def render_layers(layers):
    o3d.visualization.draw_geometries(layers)


# Example
layers = get_layers_pc()
meshes = []
for layer in layers:
    meshes.append(
        get_smooth_mesh_from_triangle_mesh(get_mesh_from_point_cloud(layer),
                                           1))
    print("done")

render_layers(meshes)