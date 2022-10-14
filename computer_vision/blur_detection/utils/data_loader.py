# Import Standard Libraries
from torch.utils.data import Dataset, DataLoader
import numpy as np


class TrainDataset(Dataset):
    """
    Extend the class torch.utils.data.Dataset to easily manage data for the training process

    Attributes
        data: numpy.ndarray of Extracted Image Features
        dimension: Integer length of each Extracted Image Feature
                   (it depends on the block_size_feature_extractor in feature_extraction.py)

    Methods
    """

    def __init__(self, data):
        """
        Instantiate the required variables for extending the class torch.utils.data.Dataset

        :param data: numpy.ndarray of Extracted Image Features
        """

        # Extracted features
        self.data = data

        #
        self.dimension = np.shape(self.data)[1] - 1

    def __len__(self):
        """
        Compute the number of extracted features
        :return: Integer number of extracted features
        """
        return np.shape(self.data)[0]

    def __getitem__(self, index):
        """

        :param index:
        :return:
        """
        x = self.data[index][0:self.dimension] / 255.0
        y = self.data[index][-1]
        return x, y


class TestDataset(TrainDataset):
    """
    Based on the class TrainDataset that extends the class torch.utils.data.Dataset to
    easily manage data for the training process

    Attributes
        data: numpy.ndarray of Extracted Image Features
        dimension: Integer length of each Extracted Image Feature
                   (it depends on the block_size_feature_extractor in feature_extraction.py)

    Methods
    """

    def __init__(self, data):
        super().__init__(data)

    def __getitem__(self, ind):
        x = self.data[ind][:] / 255.0
        return x
    