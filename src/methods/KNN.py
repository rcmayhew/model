import numpy as np
from src.methods import BOW

from sklearn.model_selection import train_test_split  # for spliting data

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

    def __load_data__(self, np_data_array: np.array, y_data):
        self.data = np_data_array
        self.class_data = y_data

    def train(self, data, actual_class):
        """
        loads data into the class
        :return:
        """
        self.__load_data__(data, actual_class)

    def hyper_plane(self):
        """
        for 1 to K:

        :return:
        """
        pass

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
        pass

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
        if len(voting_points) < self.k or trial_point[0] < voting_points[-1]:
            voting_points.append(trial_point)
            voting_points = self.__clean_voting_list__(voting_points)
            return voting_points, True

        return voting_points, False

    def __clean_voting_list__(self, voting_list):
        """
        makes the voting list ordered and the right size to never be longer than k
        :param voting_list:
        :return: ordered list of votes size >= k
        """
        voting_list = sorted(voting_list, key=lambda x: x[0])
        if len(voting_list) > self.k:
            voting_list.pop()
        return voting_list

    def __make_voting_list__(self, test_vector):
        """
        takes a single row of test data and shows the k cloest data points
        :param test_vector: single instance test case
        :return: a list of k closest data points
        """
        voting_list = []
        for index, row in enumerate(self.data):
            print(row)
            space = self.__distance__(row, test_vector)
            data_group = space, self.class_data[index]
            self.__test_voting_point__(voting_list, data_group)
        return voting_list

    @staticmethod
    def __tally_votes__(voting_list):
        """
        takes a list of votes with distances and gives the class with the most votes
        :param voting_list: list of votes ordered by closest data points
        :return: the predicted class
        """
        vote_dict = []
        for vote in voting_list:
            if vote in vote_dict:
                vote_dict[vote] = vote_dict[vote] + 1
            else:
                vote_dict[vote] = 1
        vote_dict = sorted(vote_dict, reverse=True, key=lambda x: x[1])
        return vote_dict[0]

    def __single_instance_classify__(self, test_vector):
        """
        takes a row of data and classifies it
        :param test_vector: a row of data
        :return: the predicted class for that instance
        """
        voting_list = self.__make_voting_list__(test_vector)
        predicted_class = self.__tally_votes__(voting_list)
        return predicted_class

    def classify(self, testing_data, testing_class):
        """
        take the whole array and
        :param testing_data:
        :param testing_class:
        :return:
        """
        pass


# This is the area to test the program
# init the classes
test = KNN()
bag_of_words = BOW.BOW()

# grab data and split it into testing, training; and features and labels
x_data, y = bag_of_words.parse_business_reviews()
data_train, data_test, labels_train, labels_test = train_test_split(x_data, y, test_size=0.20, random_state=42)

# trains the model, then attempts to classify the issue
test.train(data_train, labels_train)
test.classify(data_test, labels_test)
