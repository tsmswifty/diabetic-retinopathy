import os

import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


# hacky fix to get past the pickle loading error when num_workers > 0
class RetinaDataset(Dataset):
    def __init__(self, data_dir, labels_file, transform=None):
        self.data_dir = data_dir
        self.labels_df = pd.read_csv(labels_file)
        self.transform = transform

    def __len__(self):
        return len(self.labels_df)

    def __getitem__(self, idx):
        img_name = self.labels_df.iloc[idx, 0] + ".jpeg"
        img_path = os.path.join(self.data_dir, img_name)
        image = Image.open(img_path).convert("RGB")
        label = self.labels_df.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        return image, label

    def set_transform(self, transform):
        self.transform = transform
