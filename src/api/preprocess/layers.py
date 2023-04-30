import numpy as np

# Read atlas layers

atlas_layers_cp = np.loadtxt("./data/atlas_nodes.txt", max_rows=1000000)
atlas_labels = np.loadtxt("./data/atlas_region.txt", max_rows=1000000)

skin = []
skull = []
CSF = []
gray_matter = []
white_matter = []

for i in range(atlas_labels.shape[0]):
    label = int(atlas_labels[i])
    if label == 1:
        skin.append(atlas_layers_cp[i])
    elif label == 2:
        skull.append(atlas_layers_cp[i])
    elif label == 3:
        CSF.append(atlas_layers_cp[i])
    elif label == 4:
        gray_matter.append(atlas_layers_cp[i])
    elif label == 5:
        white_matter.append(atlas_layers_cp[i])

skin = np.array(skin)
skull = np.array(skull)
CSF = np.array(CSF)
gray_matter = np.array(gray_matter)
white_matter = np.array(white_matter)

rnd_indices = np.random.choice(len(skin), size=40000, replace=False)
skin_reduced_cp = skin[rnd_indices]

rnd_indices = np.random.choice(len(skull), size=20000, replace=False)
skull_reduced_cp = skull[rnd_indices]

rnd_indices = np.random.choice(len(CSF), size=10000, replace=False)
CSF_reduced_cp = CSF[rnd_indices]

rnd_indices = np.random.choice(len(gray_matter), size=10000, replace=False)
gray_matter_reduced_cp = gray_matter[rnd_indices]

rnd_indices = np.random.choice(len(white_matter), size=10000, replace=False)
white_matter_reduced_cp = white_matter[rnd_indices]

rows = np.where(skin_reduced_cp[:, 2] < -15)
skin_layer = skin_reduced_cp[rows]

rows = np.where(
    np.logical_and(skull_reduced_cp[:, 2] > -50, skull_reduced_cp[:, 2] < 5))
skull_layer = skull_reduced_cp[rows]

rows = np.where(gray_matter_reduced_cp[:, 2] > -20)
CSF_layer = gray_matter_reduced_cp[rows]
