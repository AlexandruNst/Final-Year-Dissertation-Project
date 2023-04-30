import numpy as np
import open3d as o3d


# Calculate the volume overlap approximation
def calculate_volume_points_percentage(subject, atlas):
    #Generate all points in space
    points_in_atlas = 0
    points_in_subject = 0
    points_in_both = 0
    all_points = []
    volume_points = []
    for x in range(-100, 101, 10):
        for y in range(-100, 101, 10):
            for z in range(-100, 101, 10):
                all_points.append([x, y, z])
    all_points = np.array(all_points)
    len_all_points = len(all_points)

    #reduce number of points to half randomly
    rnd_indices = np.random.choice(len(subject),
                                   size=int(len(subject) / 2),
                                   replace=False)
    subject = subject[rnd_indices]
    rnd_indices = np.random.choice(len(atlas),
                                   size=int(len(atlas) / 2),
                                   replace=False)
    atlas = atlas[rnd_indices]

    #calculate
    subject_points, subject_normals = generate_points_and_normals(subject)
    atlas_points, atlas_normals = generate_points_and_normals(atlas)

    for index, point in enumerate(all_points):
        is_in_subject = is_point_in_shape(point, subject_points,
                                          subject_normals)
        is_in_atlas = is_point_in_shape(point, atlas_points, atlas_normals)

        if index % 500 == 0:
            print(str(index) + " --- " + str(len_all_points))
        if is_in_subject and is_in_atlas:
            points_in_both += 1
        elif is_in_subject:
            points_in_subject += 1
        elif is_in_atlas:
            points_in_atlas += 1

    total_points = points_in_both + points_in_atlas + points_in_subject
    volume_overlap = points_in_both / total_points
    return volume_overlap


def is_point_in_shape(point, subject_points, subject_normals):
    # If product [normal (dot_prod) (point - point_on_mesh)] is positive, then
    # the point is on the side of the normal
    # If a point is on the side of all normals (all prods are >0) then point
    # is inside shape
    for i in range(subject_points.shape[0]):
        prod = np.dot(subject_normals[i], (point - subject_points[i]))
        if prod < 0:
            return False
    return True


def generate_points_and_normals(subject):
    # Generate normals oriented inside the shape
    source = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(subject[:, :3])
    source.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamRadius(
        radius=50))
    source.orient_normals_towards_camera_location()
    source.normals = o3d.utility.Vector3dVector(np.asarray(source.normals) * 1)

    #Extract points and corresponding normals
    subject_points = np.asarray(source.points)
    subject_normals = np.asarray(source.normals)
    return subject_points, subject_normals