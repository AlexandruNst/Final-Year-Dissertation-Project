from render.render import render_point_cloud, render_two_point_clouds
from process.registration import registration
from process.icp import icp_quaternion as icp
from evaluation.hausdoff import calculate_hausdorff_distance
from evaluation.rms import calculate_rms_distance
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp
from preprocess.feature_points import subject_1_fp, subject_2_fp, subject_3_fp, subject_4_fp, subject_5_fp, subject_6_fp, subject_7_fp, subject_8_fp, subject_9_fp, subject_10_fp, atlas_fp
from preprocess.point_cloud_top_of_head import subject_1_top_of_head_cp, subject_2_top_of_head_cp, subject_3_top_of_head_cp, subject_4_top_of_head_cp, subject_5_top_of_head_cp, subject_6_top_of_head_cp, subject_7_top_of_head_cp, subject_8_top_of_head_cp, subject_9_top_of_head_cp, subject_10_top_of_head_cp, atlas_top_of_head_cp
from metrics_calc.calc_metrics import calc_metrics
from metrics_calc.calc_metrics_top_of_head import calc_metrics_top_head
import time
from evaluation.volume_points import calculate_volume_points_percentage
from stl_handling.stl import ben_head_reduced_cp, ben_reduced_cp
from process.rotate import rotate_to_match, rotate_to_face_front, rotate_to_match_bad
from ply_handling.handle_ply_input import get_point_cloud_from_user_input, get_top_of_head_from_user_input, write_registered_points


def register_icp():
    top_head = get_top_of_head_from_user_input()
    whole_head = get_point_cloud_from_user_input()
    transformed_top_head, transformed_whole_head = icp(top_head,
                                                       top_head,
                                                       atlas_cp,
                                                       body=whole_head)
    write_registered_points(transformed_whole_head)
    time.sleep(3)
    return True


def handle_file(file_contents):
    new_file_contents = []
    int_arr = []
    for row in file_contents:
        new_row = [str(float(elem) + 100) for elem in row]
        new_file_contents.append(new_row)
        new_row_int = [(float(elem)) for elem in row]
        int_arr.append(new_row_int)
    return new_file_contents, int_arr