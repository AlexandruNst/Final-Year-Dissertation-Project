import numpy as np
from math import sqrt


# Performs the SVD registration algorithm.
# Arguments:
# cp1 - the cloud point to apply the final transformation to
# fp1 - the feature points of the shape to be transformed - we used the landmarks
# fp2 - the feature points of the shape to which the transformation is made - we used the landmarks
# Output: the transformed cp1
def registration(cp1, fp1, fp2):
    #Transpose point clouds
    subject = fp1.T
    atlas = fp2.T

    assert subject.shape == atlas.shape

    # find mean
    centroid_subject = np.mean(subject, axis=1)
    centroid_atlas = np.mean(atlas, axis=1)

    # make sure centroids are shape 3x1
    centroid_subject = centroid_subject.reshape(-1, 1)
    centroid_atlas = centroid_atlas.reshape(-1, 1)

    # subtract mean
    subject_centered = subject - centroid_subject
    atlas_centered = atlas - centroid_atlas

    H = 0.2 * (atlas_centered @ subject_centered.T)

    # find standard deviation for x
    summ = 0
    for x in subject_centered:
        for y in x:
            a = y**2
            summ += a
    std_subject_2 = summ * 0.2

    # find rotation
    U, D, Vt = np.linalg.svd(H)

    # find S
    S = np.eye(3)
    if np.linalg.det(U) * np.linalg.det(Vt) == -1:
        S[2][2] = -1

    # find rotation
    R = U @ S @ Vt

    # find scale
    s = (1 / std_subject_2) * (np.sum(D * np.diag(S)))

    # find translation
    t = s * -R @ centroid_subject + centroid_atlas

    # return registered subject
    return (s * np.matmul(R, cp1.T) + t).T
