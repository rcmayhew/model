from src.methods import BOW as bow
from src.shelf import data_review as dr

"echo \"Word\" | ./fastText/fasttext print-word-vectors wiki/result/fil9.bin"





# reviews = dr.selected_reviews
test = bow.BOW()
test.shelf_NN_words()
# words = test.give_NN_words()
# print(words)
