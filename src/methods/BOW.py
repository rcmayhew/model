from src.shelf import dicts as al
from src.shelf import data_review as dr
import copy
import codecs
import numpy as np


class BOW:
    def __init__(self):
        self.accepted_words = dict.fromkeys(al.words, 0)
        self.punctuation = [al.single_punctuation, al.double_punctuation, al.triple_punctuation]
        self.NN_punctuation = [[al.NN_words_single_punc, al.NN_words_double_punc, al.NN_words_triple_punc],
                              [al.NN_notwords_single_punc, al.NN_notwords_double_punc, al.NN_words_triple_punc]]
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
        if med_char in med_char_punctuation:
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

    def NN_word_parse(self, review, running_words_in_review):
        next_start = 0
        while next_start < len(review):
            word, next_start = self.find_word_NN(review, next_start)
            if word in running_words_in_review:
                running_words_in_review[word] = running_words_in_review[word] + 1
            else:
                running_words_in_review[word] = 1
        return running_words_in_review

    def give_NN_words(self, verbose=True, threshold=8000):
        #first list on datalist is empty!!!
        data = dr.selected_reviews
        loop = 0
        total_word_dict = {}
        for review in data:
            if verbose:
                if loop % 1000 == 0:
                    print("Done with " + str(loop) + " loops")
            if loop < threshold:
                text = review[0]
                total_word_dict = self.NN_word_parse(text, total_word_dict)
            loop = loop + 1
        return_dict = sorted(total_word_dict.items(), key=lambda kv: kv[0])
        return return_dict

    def find_word_NN(self, review, start):
        place = start
        while place < len(review):
            space, length, possible_word = self.find_NN_space(review, place)
            is_word = len(possible_word) > 0
            if space and place == start and not is_word:
                start = start + length
            elif space and place == start and is_word:
                place = place + length
                break
            elif space:
                break
            place = place + 1
        word = review[start:place]
        return word, place

    def find_NN_space(self, review, location):
        char = review[location]
        long_char = review[location:location + 2]
        med_char = review[location:location + 1]

        single_char_punctuation = self.NN_punctuation[1][0]
        med_char_punctuation = self.NN_punctuation[1][1]
        long_char_punctuation = self.NN_punctuation[1][2]

        single_punc_word = self.NN_punctuation[0][0]
        double_punc_word = self.NN_punctuation[0][1]
        triple_punc_word = self.NN_punctuation[0][2]

        if char in single_char_punctuation:
            return True, 1, ""
        if char in single_punc_word:
            return True, 1, char
        if med_char in med_char_punctuation:
            return True, 2, ""
        if med_char in double_punc_word:
            return True, 2, med_char
        if long_char in long_char_punctuation:
            return True, 3, ""
        if long_char in triple_punc_word:
            return True, 3, long_char

        return False, 0, ""

    def shelf_NN_words(self):
        data = self.give_NN_words()
        with codecs.open('shelf\parsed_words.txt', 'w', 'utf-8') as f:
            for elm in data:
                f.write(str(elm[0]) + " ")


    @staticmethod
    def parse_word_dict(word_dict):
        array = [v for k, v in word_dict.items()]
        return array

    @staticmethod
    def convert_to_numpy(listed_data):
        return np.asarray(listed_data)

    def parse_business_reviews(self, verbose=True, threshold=8000):
        #first list on datalist is empty!!!
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

        x = BOW.convert_to_numpy(data_list)
        y = BOW.convert_to_numpy(class_labels)
        return x[1:], y



# tested_class = BOW()
# data, classification = tested_class.parse_business_reviews()
# print(data)
# print(classification)
