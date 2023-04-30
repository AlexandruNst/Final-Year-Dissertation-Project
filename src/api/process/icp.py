# Implementation of ICP using the quaternion method ??
import numpy as np
from math import sqrt
import sys
from scipy.spatial import distance
import pprint
from evaluation.rms import calculate_rms_distance
from render.render import render_two_point_clouds


def get_delta(H):
    Hdiff = H - H.T
    A_12 = Hdiff[0][1]
    A_23 = Hdiff[1][2]
    A_31 = Hdiff[2][0]

    delta = [A_23, A_31, A_12]
    return delta


def calculate_R(eigv):
    q0 = eigv[0]
    q1 = eigv[1]
    q2 = eigv[2]
    q3 = eigv[3]

    R = np.zeros((3, 3))
    R[0][0] = q0**2 + q1**2 - q2**2 - q3**2
    R[0][1] = 2 * (q1 * q2 - q0 * q3)
    R[0][2] = 2 * (q1 * q3 + q0 * q2)
    R[1][0] = 2 * (q1 * q2 + q0 * q3)
    R[1][1] = q0**2 + q2**2 - q1**2 - q3**2
    R[1][2] = 2 * (q2 * q3 - q0 * q1)
    R[2][0] = 2 * (q1 * q3 - q0 * q2)
    R[2][1] = 2 * (q2 * q3 + q0 * q1)
    R[2][2] = q0**2 + q3**2 - q1**2 - q2**2

    return R


# Makes the two sets of points of equal size by removing points at random
# from the set with more points
def make_equal_length(old_fp1, old_fp2):
    old_fp1_len = len(old_fp1)
    old_fp2_len = len(old_fp2)
    min_len = old_fp1_len if old_fp1_len < old_fp2_len else old_fp2_len

    rnd_indices = np.random.choice(len(old_fp1), size=min_len, replace=False)
    fp1 = old_fp1[rnd_indices]

    rnd_indices = np.random.choice(len(old_fp2), size=min_len, replace=False)
    fp2 = old_fp2[rnd_indices]

    return fp1, fp2


# Returns the list of points closest to the points in the first point cloud
# with corresponding indices
def correspondances(eq_fp1, eq_fp2):
    fp2 = []
    for point in eq_fp1:
        closest_index = distance.cdist([point], eq_fp2).argmin()
        fp2.append(eq_fp2[closest_index])
    fp2 = np.array(fp2)
    return fp2


# Performs the Iterative Closest Point algorithm.
# Arguments:
# pc - the point cloud to apply the final transformation to
# old_fp1 - the feature points of the shape to be transformed - we used the entire set
# old_fp2 - the feature points of the shape to which the transformation is made - we used the entire set
# body (optional) - an extension of the point cloud to apply the same transformation to
# Output: the transformed pc and optionally the transformed body
def icp_quaternion(pc, old_fp1, old_fp2, body=None):
    eq_fp1, eq_fp2 = make_equal_length(old_fp1, old_fp2)

    ### Center and scaling

    # Center
    subject = eq_fp1.T
    atlas = eq_fp2.T
    point_cloud = pc.T
    body = body.T

    # find mean
    centroid_subject = np.mean(subject, axis=1)
    centroid_atlas = np.mean(atlas, axis=1)

    # reshape centroid to 3x1
    centroid_subject = centroid_subject.reshape(-1, 1)
    centroid_atlas = centroid_atlas.reshape(-1, 1)

    # subtract mean
    subject_centered = subject - (centroid_subject - centroid_atlas)
    atlas_centered = atlas  # atlas remains unchanged
    point_cloud_centered = point_cloud - (centroid_subject - centroid_atlas)
    body_centered = body - (centroid_subject - centroid_atlas)

    eq_fp1 = subject_centered.T
    eq_fp2 = atlas_centered.T

    corrs = correspondances(eq_fp1, eq_fp2)

    # find scale
    subject_centered = eq_fp1.T
    atlas_centered = corrs.T

    H = 1 / eq_fp1.shape[0] * (atlas_centered @ subject_centered.T)

    summ = 0
    for x in subject_centered:
        for y in x:
            a = y**2
            summ += a
    std_subject_2 = summ / eq_fp1.shape[0]

    U, D, Vt = np.linalg.svd(H)
    s = (1 / std_subject_2) * (np.sum(D))

    eq_fp1 = s * eq_fp1
    pc = s * point_cloud_centered.T
    body = s * body_centered.T

    print("Centered and scaled!")
    print("Scale factor: " + str(s))

    ### Begin iterating

    fp1_0 = eq_fp1
    old_error = 0
    tau = 0.01

    for i in range(25):
        # stopping condition
        new_error = calculate_rms_distance(eq_fp1, old_fp2)
        print(new_error)
        if abs(new_error - old_error) < tau:
            break

        old_error = new_error

        fp2 = correspondances(eq_fp1, eq_fp2)
        fp1 = fp1_0

        subject = fp1.T
        atlas = fp2.T

        assert subject.shape == atlas.shape

        # find mean
        centroid_subject = np.mean(subject, axis=1)
        centroid_atlas = np.mean(atlas, axis=1)

        # reshape to 3 x 1
        centroid_subject = centroid_subject.reshape(-1, 1)
        centroid_atlas = centroid_atlas.reshape(-1, 1)

        # center
        subject_centered = subject - centroid_subject
        atlas_centered = atlas - centroid_atlas

        H = 1 / fp1.shape[0] * (atlas_centered @ subject_centered.T)

        # calculate Q
        tr_H = np.trace(H)
        delta = get_delta(H)
        cov_sum = H + H.T - [[tr_H, 0, 0], [0, tr_H, 0], [0, 0, tr_H]]

        Q = np.zeros((4, 4))
        Q[0][0] = tr_H
        Q[0][1] = Q[1][0] = delta[0]
        Q[0][2] = Q[2][0] = delta[1]
        Q[0][3] = Q[3][0] = delta[2]
        for i in range(1, 4):
            for j in range(1, 4):
                Q[i][j] = cov_sum[i - 1][j - 1]

        # get eigenvector with biggest eigenvalue
        w, v = np.linalg.eig(Q)
        max_eig = float('-inf')
        max_eig_i = -1
        for i in range(len(w)):
            if w[i] > max_eig:
                max_eig = w[i]
                max_eig_i = i
        max_eig_v = v[:, max_eig_i]

        R = calculate_R(max_eig_v)

        # qr is the max eigenvector
        qr = max_eig_v

        # calculate qT
        qt = centroid_atlas - R @ centroid_subject

        # last step, apply the transformation to the point cloud before next iteration
        eq_fp1 = (np.matmul(R, fp1_0.T) + qt).T

    # find a final scale factor
    summ = 0
    for x in subject_centered:
        for y in x:
            a = y**2
            summ += a
    std_subject_2 = summ / fp1.shape[0]

    U, D, Vt = np.linalg.svd(H)
    s = (1 / std_subject_2) * (np.sum(D))

    print("Scale factor: " + str(s))

    # register subject and optionally the body
    if body is None:
        return (s * np.matmul(R, pc.T) + qt).T
    else:
        return (s * np.matmul(R, pc.T) + qt).T, (s * np.matmul(R, body.T) +
                                                 qt).T
