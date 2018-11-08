import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


class SVM:
    def __init__(self, visual=True):
        self.visual = visual
        self.colors = {1: 'r', 2: 'b', 3: 'g', 4: 'y', 5: 'k'}
        if self.visual:
            pass

    def fit(self, data):
        self.data = data
        # { ||w||: [w,b] }
        opt_dict = {}

        transforms = [[1, 1],
                      [-1, 1],
                      [-1, -1],
                      [1, -1]]

        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feautre_value = max(all_data)

        #support

        step_sizes = [self.max_feature_value * 0.01,
                      self.max_feature_value * 0.001,
                      self.max_feature_value * 0.0001]

        b_range_multiple = 5
        b_multiple = 5
        lastest_optimum = self.max_feature_value*10

        for step in step_sizes:
            #corners cut?
            w = np.array([lastest_optimum, lastest_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-1*self.max_feature_value*b_range_multiple,
                                   self.max_feature_value*b_range_multiple,
                                   step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True
                        for i in self.data:
                            for xi in self.data[i]:
                                yi=i
                                if not yi*(np.dot(w_t, xi)+b) >= 1:
                                    found_option = False
                                    #opitional
                                    break
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t,b]
                if w[0] < 0:
                    optimized = True
                    print('optimized a step.')
                else:
                    #w - [step, step]
                    w = w - step
            norms = sorted([n for n in opt_dict])
            opt_choice = opt_dict[norms[0]]
            # { ||w||: [w,b] }
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0]+step*2

    @staticmethod
    def rbf_kernel(mat1, mat2, sigma):

        trnorms1 = np.mat([(v * v.T)[0, 0] for v in mat1]).T
        trnorms2 = np.mat([(v * v.T)[0, 0] for v in mat2]).T

        k1 = trnorms1 * np.mat(np.ones((mat2.shape[0], 1), dtype=np.float64)).T
        k2 = np.mat(np.ones((mat1.shape[0], 1), dtype=np.float64)) * trnorms2.T

        k = k1 + k2
        k -= 2 * np.mat(mat1 * mat2.T)
        k *= - 1. / (2 * np.power(sigma, 2))

        return np.exp(k)

    def predict(self, features):
        # sign(x.w + b)
        classification = np.sign(np.dot(np.array(features), self.w + self.b))

        return classification

