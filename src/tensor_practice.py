import tensorflow as tf

"""
https://www.tensorflow.org/tutorials/eager/custom_training
Recurrent Convolutional Neural Networks for Text Classification
https://code.google.com/archive/p/word2vec/
https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
https://fasttext.cc/docs/en/crawl-vectors.html

@inproceedings{grave2018learning,
  title={Learning Word Vectors for 157 Languages},
  author={Grave, Edouard and Bojanowski, Piotr and Gupta, Prakhar and Joulin, Armand and Mikolov, Tomas},
  booktitle={Proceedings of the International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
}
https://fasttext.cc/docs/en/unsupervised-tutorial.html
"""

"""
notes:
make a recurrent neural net: RNN
    for the processing of the sentence
    bias to word at the end of the sentence
make convolutional neural net: CNN
    made to handle the bias made by the RNN
    
to merge them paper wants a recurrent convolutional neural network: RCNN
"""

"""
TODO:
create embedded word model
    use google word to vect fuction
    take the wikipedia dump
create tensor model
    figure out method to read in sentences.
    change bag of words tokenizer to have an option that keep puncuation
set the default values
create the max pooling layer
"""

