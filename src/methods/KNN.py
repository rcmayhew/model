import numpy as np

"""
need a distance formula
need a list of data
need a classifier:
        will search through the entire testing data
will split data later

!!!will need  data splitor, I think np has one
"""


class KNN:
    def __init__(self):
        self.feature_space_dimension = 0
        self.test_space_dimension = 0
        self.removed_features = []
        self.class_number = 0
        self.k = 0
        self.class_data = []
        self.data = []

    def __load_data__(self, np_data_array: np.array):
        self.data = np_data_array
        self.class_data = np.delete(self.data, -1, axis=1)

    def train(self, data):
        """
        create hyper planes from training data
        creates a plane per class
        :return:
        """
        self.__load_data__(data)

    def hyper_plane(self):
        """
        for 1 to K:

        :return:
        """

    def feature_selection(self):
        """
        will be ran in the train method
        :return:
        """
        pass

    def k_selecion(self):
        """
        will be ran in trainer
        :return:
        """

    @staticmethod
    def __distance__(a: np.array, b: np.array):
        return np.linalg.norm(a-b)

    def __test_voting_point__(self, voting_points: list, trial_point: tuple):
        """
        takes a testing point and checks if the new point is a
        contender to classify the instance being classified
        :param voting_points: list of (distance: float, class: int)
                            sorted by distance
        :param trial_point: (distance: float, class: int)
        :return: new voting_points:list, was it change:bool
        """
        if len(voting_points) < self.k:
            voting_points.append(trial_point)
            return voting_points, True
        elif trial_point[0] < voting_points[-1]:
            voting_points = self.__clean_voting_list__(voting_points)
            return voting_points, True
        else:
            return voting_points, False

    @staticmethod
    def __clean_voting_list__(voting_list):
        """
        can assume list size is k + 1
        :param voting_list:
        :return:
        """
        voting_list = sorted(voting_list, key=lambda x: x[0])
        voting_list.pop()
        return voting_list

    def __make_voting_list(self, test_vector):
        voting_list = []
        for index, row in enumerate(self.data):
            space = self.__distance__(row, test_vector)
            data_group = space, self.class_data[index]
            self.__test_voting_point__(voting_list, data_group)
        return voting_list

    def __tally_votes(self):
        pass

    def __single_instance_classify(self, test_vector):
        voting_list = self.__make_voting_list(test_vector)

    def classify(self, testing_data):
        pass

