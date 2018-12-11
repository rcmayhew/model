import codecs
from src.shelf import embedded_vec as ev
"""
vector dim is 100
"""

file_location = "shelf/word_parse.txt"
write_file = "shelf/embedded_vec.py"
x = [0, 9,]

def give_word_list(file_location):
    list_of_comma_sep = [[]]
    with codecs.open(file_location) as write:
        for line in write:
            counting = 0
            tracking = 0
            holder_sting = []
            string_holder = []
            for ind, word in enumerate(line):
                if tokenizer(word):
                    string_holder.append("".join(holder_sting))
                    holder_sting = []
                else:
                    holder_sting.append(word)
            #print(string_holder)
            list_of_comma_sep.append(string_holder)
        #print(list_of_comma_sep)
    write.close()
    return list_of_comma_sep


def write_word_list(file_write, data_list):
    with codecs.open(file_write, 'w', encoding='utf8') as embed:
        embed.write("embedded_vector = { \n")
        for indx, data in enumerate(data_list):
            for ind, elem in enumerate(data):
                if ind == 0:
                    embed.write("    " + '"' + str(elem) + '": [')
                else:
                    embed.write(str(elem) + ", ")
            embed.write("], \n")
    embed.close()



def tokenizer(word):
    if word == " ":
        return True
    return False

# def add_data(data, name_of_var, typed):
#     with codecs.open('mod\words.py', typed, 'utf-8') as f:
#         f.write(name_of_var + " = " + str(data))

# listed = give_word_list(file_location)
# write_word_list(write_file, listed)


embedding = ev.embedded_vector
print(embedding["$31"])

