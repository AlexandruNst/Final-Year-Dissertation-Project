import numpy as np

# Methods for initial alignment


# Rotate subject to match atlas
def rotate_to_match(subject_cp, atlas_cp, body=None):
    # calculate covariance matrix for subject data
    subject_covariance = (1 /
                          subject_cp.shape[0]) * (subject_cp.T @ subject_cp)

    # find subject eigenvector with biggest eigenvalue
    eigenvalues, eigenvectors = np.linalg.eig(subject_covariance)
    max_eig = float('-inf')
    max_eig_i = -1
    for i in range(len(eigenvalues)):
        if eigenvalues[i] > max_eig:
            max_eig = eigenvalues[i]
            max_eig_i = i
    subject_max_eigenvector = eigenvectors[:, max_eig_i]

    # calculate covariance matrix of atlas data
    atlas_covariance = (1 / atlas_cp.shape[0]) * (atlas_cp.T @ atlas_cp)

    # find subject eigenvector with biggest eigenvalue
    eigenvalues, eigenvectors = np.linalg.eig(atlas_covariance)
    max_eig = float('-inf')
    max_eig_i = -1
    for i in range(len(eigenvalues)):
        if eigenvalues[i] > max_eig:
            max_eig = eigenvalues[i]
            max_eig_i = i
    atlas_max_eigenvector = eigenvectors[:, max_eig_i]

    # We have the eigenvectors with the biggest eigenvalues for both point clouds
    # These represent the direction of biggest variance in data, which is from Inion to Nasion
    # We calculate the rotation matrix that rotates the subject eigenvector in the direction of the atlas eigenvector
    # Then we set apply the rotation along the z axis only to the entire subject dataset. This ensures the Inion-Nasion line
    #   for both the subject and the atlas are aligned

    # Calculate full rotation matrix
    cos = np.dot(subject_max_eigenvector, atlas_max_eigenvector)
    mat_mul = np.cross(subject_max_eigenvector, atlas_max_eigenvector)
    sin = np.linalg.norm(mat_mul)
    skew_symmetric = np.array([
        [0, -mat_mul[2], mat_mul[1]],  #
        [mat_mul[2], 0, -mat_mul[0]],  #
        [-mat_mul[1], mat_mul[0], 0]
    ])
    skew_symmetric_squared = skew_symmetric.dot(skew_symmetric)
    rotation_matrix = np.eye(3) + skew_symmetric + skew_symmetric_squared * (
        (1 - cos) / (sin**2))

    # Set the values that affect the z index to identity, making the rotation not affect the z axis
    rotation_matrix[0][2] = 0
    rotation_matrix[1][2] = 0
    rotation_matrix[2][0] = 0
    rotation_matrix[2][1] = 0
    rotation_matrix[2][2] = 1

    # Apply rotation to the subject point cloud
    rotated_subject_cp = np.matmul(rotation_matrix, subject_cp.T).T
    if body is not None:
        rotated_body_cp = np.matmul(rotation_matrix, body.T).T

    if body is None:
        return rotated_subject_cp
    else:
        return rotated_subject_cp, rotated_body_cp


# Rotate a point cloud to face parallel to the x-axis
def rotate_to_face_front(subject_cp):
    # calculate covariance matrix for subject data
    subject_covariance = (1 /
                          subject_cp.shape[0]) * (subject_cp.T @ subject_cp)

    # find subject eigenvector with biggest eigenvalue
    eigenvalues, eigenvectors = np.linalg.eig(subject_covariance)
    max_eig = float('-inf')
    max_eig_i = -1
    for i in range(len(eigenvalues)):
        if eigenvalues[i] > max_eig:
            max_eig = eigenvalues[i]
            max_eig_i = i
    subject_max_eigenvector = eigenvectors[:, max_eig_i]

    # Vector that points forward
    y_vector = np.array([0, 1, 0])

    # We have the eigenvectors with the biggest eigenvalues for the point cloud, as well the Ox parallel vector.
    # That represents the direction of biggest variance in data, which is from Inion to Nasion
    # We calculate the rotation matrix that rotates the subject eigenvector in the direction of the vector pointing forwards
    # Then we set apply the rotation along the z axis only to the entire subject dataset. This ensures the Inion-Nasion line
    #   for both the subject and the atlas are aligned

    # Calculate full rotation matrix
    cos = np.dot(subject_max_eigenvector, y_vector)
    mat_mul = np.cross(subject_max_eigenvector, y_vector)
    sin = np.linalg.norm(mat_mul)
    skew_symmetric = np.array([
        [0, -mat_mul[2], mat_mul[1]],  #
        [mat_mul[2], 0, -mat_mul[0]],  #
        [-mat_mul[1], mat_mul[0], 0]
    ])
    skew_symmetric_squared = skew_symmetric.dot(skew_symmetric)
    rotation_matrix = np.eye(3) + skew_symmetric + skew_symmetric_squared * (
        (1 - cos) / (sin**2))

    # Set the values that affect the z index to identity, making the rotation not affect the z axis
    rotation_matrix[0][2] = 0
    rotation_matrix[1][2] = 0
    rotation_matrix[2][0] = 0
    rotation_matrix[2][1] = 0
    rotation_matrix[2][2] = 1

    # Apply rotation to the point cloud
    rotated_subject_cp = np.matmul(rotation_matrix, subject_cp.T).T

    return rotated_subject_cp


# Rotation method that applies the z axis rotation as well, achieving the unwanted tilt effect
def rotate_to_match_bad(subject_cp, atlas_cp):
    # calculate covariance matrix for subject data
    subject_covariance = (1 /
                          subject_cp.shape[0]) * (subject_cp.T @ subject_cp)

    # find subject eigenvector with biggest eigenvalue
    eigenvalues, eigenvectors = np.linalg.eig(subject_covariance)
    max_eig = float('-inf')
    max_eig_i = -1
    for i in range(len(eigenvalues)):
        if eigenvalues[i] > max_eig:
            max_eig = eigenvalues[i]
            max_eig_i = i
    subject_max_eigenvector = eigenvectors[:, max_eig_i]

    # calculate covariance matrix of atlas data
    atlas_covariance = (1 / atlas_cp.shape[0]) * (atlas_cp.T @ atlas_cp)

    # find subject eigenvector with biggest eigenvalue
    eigenvalues, eigenvectors = np.linalg.eig(atlas_covariance)
    max_eig = float('-inf')
    max_eig_i = -1
    for i in range(len(eigenvalues)):
        if eigenvalues[i] > max_eig:
            max_eig = eigenvalues[i]
            max_eig_i = i
    atlas_max_eigenvector = eigenvectors[:, max_eig_i]

    # We have the eigenvectors with the biggest eigenvalues for both point clouds
    # These represent the direction of biggest variance in data, which is from Inion to Nasion
    # We calculate the rotation matrix that rotates the subject eigenvector in the direction of the atlas eigenvector
    # Then we set apply the rotation along the z axis only to the entire subject dataset. This ensures the Inion-Nasion line
    #   for both the subject and the atlas are aligned

    # Calculate full rotation matrix
    cos = np.dot(subject_max_eigenvector, atlas_max_eigenvector)
    mat_mul = np.cross(subject_max_eigenvector, atlas_max_eigenvector)
    sin = np.linalg.norm(mat_mul)
    skew_symmetric = np.array([
        [0, -mat_mul[2], mat_mul[1]],  #
        [mat_mul[2], 0, -mat_mul[0]],  #
        [-mat_mul[1], mat_mul[0], 0]
    ])
    skew_symmetric_squared = skew_symmetric.dot(skew_symmetric)
    rotation_matrix = np.eye(3) + skew_symmetric + skew_symmetric_squared * (
        (1 - cos) / (sin**2))

    # Apply rotation to the subject point cloud
    rotated_subject_cp = np.matmul(rotation_matrix, subject_cp.T).T

    return rotated_subject_cp