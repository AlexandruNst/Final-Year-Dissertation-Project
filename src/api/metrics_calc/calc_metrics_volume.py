from process.registration import registration
from process.icp import icp_quaternion as icp
from evaluation.hausdoff import calculate_hausdorff_distance
from evaluation.rms import calculate_rms_distance
from evaluation.volume_points import calculate_volume_points_percentage
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp
from preprocess.feature_points import subject_1_fp, subject_2_fp, subject_3_fp, subject_4_fp, subject_5_fp, subject_6_fp, subject_7_fp, subject_8_fp, subject_9_fp, subject_10_fp, atlas_fp

# Automate volume overlap approximation tests


def calc_metrics_volume():
    cps = [
        subject_1_cp,
        subject_2_cp,
        subject_3_cp,
        subject_4_cp,
        subject_5_cp,
        subject_6_cp,
        subject_7_cp,
        subject_8_cp,
        subject_9_cp,
        subject_10_cp,
    ]

    fps = [
        subject_1_fp,
        subject_2_fp,
        subject_3_fp,
        subject_4_fp,
        subject_5_fp,
        subject_6_fp,
        subject_7_fp,
        subject_8_fp,
        subject_9_fp,
        subject_10_fp,
    ]

    volume_svd_file = open("./metrics/volume_svd.txt", "a")
    volume_icp_file = open("./metrics/volume_icp.txt", "a")

    for i in range(len(cps)):
        print("\n")
        print("--- SUBJECT " + str(i + 1) + "---")
        cp = cps[i]
        fp = fps[i]

        svd_cp = registration(cp, fp, atlas_fp)
        volume_points = calculate_volume_points_percentage(svd_cp, atlas_cp)
        print("Volume SVD registration: ")
        print("Volume: " + str(volume_points))
        print("\n")
        volume_svd_file.write(str(volume_points) + "\n")
        icp_top, icp_cp = icp(cp, cp, atlas_cp, cp)
        volume_points = calculate_volume_points_percentage(icp_cp, atlas_cp)
        print("Volume ICP registration: ")
        print("Volume: " + str(volume_points))
        print("\n")
        volume_icp_file.write(str(volume_points) + "\n")

    volume_svd_file.close()
    volume_icp_file.close()