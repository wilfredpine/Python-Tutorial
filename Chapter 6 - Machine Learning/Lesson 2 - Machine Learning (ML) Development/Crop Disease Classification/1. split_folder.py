dataset = r".\datasets"
dataset_dir = r".\splited-datasets"

#pip install split-folders
import splitfolders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(dataset, output=dataset_dir,
    seed=1337, ratio=(.8, .1, .1), group_prefix=None, move=False) # default values