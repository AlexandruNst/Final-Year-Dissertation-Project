from render.render import render_point_cloud, render_two_point_clouds
from process.registration import registration
from process.icp import icp_quaternion as icp
from evaluation.hausdoff import calculate_hausdorff_distance
from evaluation.rms import calculate_rms_distance
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp
from preprocess.feature_points import subject_1_fp, subject_2_fp, subject_3_fp, subject_4_fp, subject_5_fp, subject_6_fp, subject_7_fp, subject_8_fp, subject_9_fp, subject_10_fp, atlas_fp

# Automate "Whole" tests


def calc_metrics():
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

    hd_svd_file = open("./metrics/hausdorff_svd.txt", "a")
    rms_svd_file = open("./metrics/rms_svd.txt", "a")
    hd_icp_file = open("./metrics/hausdorff_icp.txt", "a")
    rms_icp_file = open("./metrics/rms_icp.txt", "a")
    hd_pre_file = open("./metrics/hausdorff_pre.txt", "a")
    rms_pre_file = open("./metrics/rms_pre.txt", "a")

    for i in range(len(cps)):
        print("\n")
        print("--- SUBJECT " + str(i + 1) + "---")
        cp = cps[i]
        fp = fps[i]

        # render_two_point_clouds(cp, atlas_cp)
        hausdorff = calculate_hausdorff_distance(cp, atlas_cp)
        rms = calculate_rms_distance(cp, atlas_cp)
        print("Distances before: ")
        print("Hausdorff: " + str(hausdorff))
        print("RMS: " + str(rms))
        print("\n")
        hd_pre_file.write(str(hausdorff) + "\n")
        rms_pre_file.write(str(rms) + "\n")

        svd_cp = registration(cp, fp, atlas_fp)
        # render_two_point_clouds(svd_cp, atlas_cp)
        hausdorff = calculate_hausdorff_distance(svd_cp, atlas_cp)
        rms = calculate_rms_distance(svd_cp, atlas_cp)
        print("Distances SVD registration: ")
        print("Hausdorff: " + str(hausdorff))
        print("RMS: " + str(rms))
        print("\n")
        hd_svd_file.write(str(hausdorff) + "\n")
        rms_svd_file.write(str(rms) + "\n")

        icp_cp = icp(cp, cp, atlas_cp)
        # render_two_point_clouds(icp_cp, atlas_cp)
        hausdorff = calculate_hausdorff_distance(icp_cp, atlas_cp)
        rms = calculate_rms_distance(icp_cp, atlas_cp)
        print("Distances ICP registration: ")
        print("Hausdorff: " + str(hausdorff))
        print("RMS: " + str(rms))
        print("\n")
        hd_icp_file.write(str(hausdorff) + "\n")
        rms_icp_file.write(str(rms) + "\n")

    hd_svd_file.close()
    rms_svd_file.close()
    hd_icp_file.close()
    rms_icp_file.close()
    hd_pre_file.close()
    rms_pre_file.close()