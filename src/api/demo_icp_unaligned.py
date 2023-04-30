from render.render import render_point_cloud, render_two_point_clouds
from process.icp import icp_quaternion as icp
from evaluation.hausdoff import calculate_hausdorff_distance
from evaluation.rms import calculate_rms_distance
from preprocess.point_cloud import subject_1_cp, subject_2_cp, subject_3_cp, subject_4_cp, subject_5_cp, subject_6_cp, subject_7_cp, subject_8_cp, subject_9_cp, subject_10_cp, atlas_cp
from stl_handling.stl import ben_head_reduced_cp, ben_reduced_cp
from process.rotate import rotate_to_match, rotate_to_face_front, rotate_to_match_bad

# Demo of ICP failing if the subject is not initially aligned

ben_head_pc = ben_head_reduced_cp
render_two_point_clouds(ben_head_pc, atlas_cp)

transformed_ben, transformed_ben_body = icp(ben_head_pc, ben_head_pc, atlas_cp,
                                            ben_head_pc)
render_two_point_clouds(transformed_ben, atlas_cp)

render_two_point_clouds(ben_head_pc, atlas_cp)

rotated_ben = rotate_to_match_bad(ben_head_pc, atlas_cp)
render_two_point_clouds(rotated_ben, atlas_cp)

rotated_ben, rotated_ben_body = rotate_to_match(ben_head_pc,
                                                atlas_cp,
                                                body=ben_reduced_cp)
render_two_point_clouds(rotated_ben, atlas_cp)

transformed_ben, transformed_ben_body = icp(rotated_ben,
                                            rotated_ben,
                                            atlas_cp,
                                            body=rotated_ben_body)
render_two_point_clouds(transformed_ben, atlas_cp)
render_two_point_clouds(transformed_ben_body, atlas_cp)

print("//BEFORE//")
print("Hausdorff ditance: ", end="")
print(calculate_hausdorff_distance(ben_head_pc, atlas_cp))
print("RMSE: ", end="")
print(calculate_rms_distance(ben_head_pc, atlas_cp))
print("//AFTER//")
print("Hausdorff ditance: ", end="")
print(calculate_hausdorff_distance(transformed_ben, atlas_cp))
print("RMSE: ", end="")
print(calculate_rms_distance(transformed_ben, atlas_cp))