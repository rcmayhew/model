import io
import codecs
from src.linux import words


def load_vectors(fname, words):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    loop = 0
    for line in fin:
        if loop % 100000 == 0:
            print("done with loop: ", loop)
        tokens = line.rstrip().split(' ')
        possible_word = tokens[0]
        if possible_word in words:

            data[possible_word] = map(float, tokens[1:])
        #data[tokens[0]] = map(float, tokens[1:])
        loop = loop + 1
    return data


def add_data(data, name_of_var, typed):
    with codecs.open('embedded.py', typed, 'utf-8') as f:
        f.write(name_of_var + " = " + str(data))


def make_list_dict(word_list):
    word_set = {x[0] for x in word_list}
    return word_set


def make_text_file():
    pass

file = "G:\Data\\tars\cc.en.300.vec"

# important_words = words.ordered_words
# mapped_words = make_list_dict(important_words)
# vectors = load_vectors(file, mapped_words)
# print(vectors[1])
