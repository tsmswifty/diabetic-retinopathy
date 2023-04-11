import splitfolders

# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(
    "data_512",
    output="data_512_split",
    seed=1337,
    ratio=(0.8, 0.2),
    group_prefix=None,
    move=False,
)  # default values
