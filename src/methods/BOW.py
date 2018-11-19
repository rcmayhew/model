from src.shelf import dicts as al
from src.shelf import data_review as dr
import copy
import numpy as np


class BOW:
    def __init__(self):
        self.accepted_words = dict.fromkeys(al.words, 0)
        self.punctuation = [al.single_punctuation, al.double_punctuation, al.triple_punctuation]
        self.alpha_convertor = al.alpha

    def find_word(self, review, start):
        place = start
        while place < len(review):
            space, length = self.find_space(review, place)
            if space and place == start:
                start = start + length
            elif space:
                break
            place = place + 1
        word = review[start:place]
        return word, place

    def find_space(self, review, location):
        char = review[location]
        long_char = review[location:location + 2]
        med_char = review[location:location + 1]

        single_char_punctuation = self.punctuation[0]
        med_char_punctuation = self.punctuation[0]
        long_char_punctuation = self.punctuation[0]

        if char in single_char_punctuation:
            return True, 1
        if med_char is med_char_punctuation:
            return True, 2
        if long_char in long_char_punctuation:
            return True, 3

        return False, 0

    def convert_to_alpha(self, word):
        letters = []
        for ind, letter in enumerate(word):
            if letter in self.alpha_convertor:
                letters.append(self.alpha_convertor[letter])
            else:
                letters.append(letter)
        new_word = ''.join(letters)
        return new_word

    def parse_review(self, review):
        words_in_review = copy.deepcopy(self.accepted_words)
        next_start = 0
        while next_start < len(review):
            word, next_start = self.find_word(review, next_start)
            word = self.convert_to_alpha(word)
            if word in words_in_review:
                words_in_review[word] = words_in_review[word] + 1
        return BOW.parse_word_dict(words_in_review)

    @staticmethod
    def parse_word_dict(word_dict):
        array = [v for k, v in word_dict.items()]
        return array

    @staticmethod
    def convert_to_numpy(listed_data):
        return np.asarray(listed_data)

    def parse_business_reviews(self, verbose=True, threshold=8000):
        data = dr.selected_reviews
        data_list = [[]]
        class_labels = []
        loop = 0
        for review in data:
            if verbose:
                if loop % 1000 == 0:
                    print("Done with " + str(loop) + " loops")
            if loop < threshold:
                text = review[0]
                classification = review[1]
                array_split = self.parse_review(text)
                data_list.append(array_split)
                class_labels.append(classification)
            loop = loop + 1
        return BOW.convert_to_numpy(data_list), BOW.convert_to_numpy(class_labels)


tested_class = BOW()
data, classification = tested_class.parse_business_reviews()
print(data)
print(classification)
