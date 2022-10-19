# Import Standard Libraries
import cv2
import os
import numpy as np
from skimage.filters.rank import entropy
from skimage.morphology import square


class FeatureExtractor:
    """
    Perform the feature extraction over a given input image

    Attributes
        block_size_feature_extractor: Integer block size for feature extraction kernel
        down_sampling_factor: Integer scaling factor for image resizing
        resized_image: numpy.ndarray of resized image
        entropy_filter_kernel_size: Integer kernel size for computing local entropy

    Methods

    """

    def __init__(self):

        self.block_size_feature_extractor = 32
        self.down_sampling_factor = 2
        self.resized_image = []
        self.entropy_filter_kernel_size = 16
        self.local_entropy_threshold = 0.6
        self.valid_img_block_thresh = 0.7
        self.roi = []
        self.__frequency_bands = []
        self.__dct_matrices = self.__dctmtx(self.block_size_feature_extractor)
        self.__compute_frequency_bands()

    def __dctmtx(self, block_size):

        [mesh_cols, mesh_rows] = np.meshgrid(np.linspace(0, block_size - 1, block_size),
                                             np.linspace(0, block_size - 1, block_size))

        dct_matrix = np.sqrt(2 / block_size) * np.cos(np.pi * np.multiply((2 * mesh_cols + 1),
                                                                          mesh_rows) / (2 * block_size))

        dct_matrix[0, :] = dct_matrix[0, :] / np.sqrt(2)

        return dct_matrix

    def __compute_frequency_bands(self):

        current_scale = self.block_size_feature_extractor

        matrix_indices = np.zeros((current_scale, current_scale))

        for i in range(current_scale):
            matrix_indices[0: max(0, int(((current_scale - 1) / 2) - i + 1)), i] = 1

        for i in range(current_scale):
            if (current_scale - ((current_scale - 1) / 2) - i) <= 0:
                matrix_indices[0:current_scale - i - 1, i] = 2
            else:
                matrix_indices[int(current_scale - ((current_scale - 1) / 2) - i - 1): int(current_scale - i - 1), i] = 2

        matrix_indices[0, 0] = 3

        self.__frequency_bands.append(matrix_indices)

    def resize_image(self, img, rows, cols):

        self.resized_image = cv2.resize(img,
                                        (int(cols / self.down_sampling_factor),
                                         int(rows / self.down_sampling_factor)))

    def compute_roi(self):
        """
        Compute the ROI (Region of Interest) of the image based on the maximum local entropy and predefined threshold.
        ROI are identified by '1' pixels
        :return: numpy.ndarray of image's ROI
        """

        # Compute the image local entroy
        local_entropy = self.entropy_filter(self.resized_image)

        # Compute ROI of image
        self.roi = 1.0 * (local_entropy > self.local_entropy_threshold * np.max(local_entropy))

    def get_single_resolution_features(self, block):

        dct_matrix = self.__dct_matrices
        dct_coeff = np.abs(np.matmul(np.matmul(dct_matrix, block), np.transpose(dct_matrix)))
        temp = np.where(self.__frequency_bands[0] == 0)
        high_freq_components = dct_coeff[temp]
        high_freq_components = sorted(high_freq_components)

        return high_freq_components

    def extract_feature(self):
        extracted_features = []
        rows = np.shape(self.resized_image)[0]
        cols = np.shape(self.resized_image)[1]
        for i in range(0, rows, self.block_size_feature_extractor):
            for j in range(0, cols, self.block_size_feature_extractor):
                if self.is_image_block_valid(i, j):
                    block = self.resized_image[i: i + self.block_size_feature_extractor,
                            j: j + self.block_size_feature_extractor]
                    if (np.shape(block)[0] == self.block_size_feature_extractor) and (
                    (np.shape(block)[1] == self.block_size_feature_extractor)):
                        features = self.get_single_resolution_features(block)
                        extracted_features.append(features)
        return extracted_features

    def is_image_block_valid(self, i, j):
        block = self.roi[i: i + self.block_size_feature_extractor, j: j + self.block_size_feature_extractor]
        val = np.sum(block) / np.prod(np.shape(block))
        return val > self.valid_img_block_thresh

    def entropy_filter(self, image):
        """
        Local entropy is related to the complexity contained in the given neighborhood (entropy_filter_kernel_size).
        The entropy filter can detect subtle variations in the local gray level distribution.
        Compute the local entropy for each pixel of the image
        :param image: numpy.ndarray input image
        :return: numpy.ndarray of image entropy
        """

        # Create a 1-value Entropy Kernel of dimension 'entropy_filter_kernel_size x entropy_filter_kernel_size'
        entropy_kernel = square(self.entropy_filter_kernel_size)

        return entropy(image, entropy_kernel)

    def clear_object(self):
        self.resized_image = []
        self.roi = []
        self.__frequency_bands = []
