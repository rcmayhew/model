from mod import data_review as dl
import matplotlib.pyplot as plt

data = dl.selected_reviews
image_location = "images"


def rating_dist(data):
    rating = [0, 0, 0, 0, 0]
    for element in data:
        star = int(element[1])
        base = rating[star - 1]
        rating[star - 1] = base + 1
    return rating


def star_distribution(stars):
    plt.xlabel("Stars")
    plt.ylabel("Number Of Ratings")
    plt.title("Star Distribution")
    plt.bar([1, 2, 3, 4, 5], stars)
    plt.savefig(image_location + "\\" + "Star_distribution.pdf")
    plt.show()
    return 0


def star_rates(rate):
    plt.xlabel("Stars")
    plt.ylabel("Chance Of Rating")
    plt.title("Star Distribution")
    plt.bar([1, 2, 3, 4, 5], rate)
    plt.savefig(image_location + "\\" + "Star_rates.pdf")
    plt.show()
    return 0


def rate_of_distribution(stars):
    total = 0
    for z in stars:
        total = total + z
    rate = [x / total for x in stars]
    return rate


def graphing():
    reviews = rating_dist(data)
    star_distribution(reviews)
    rate = rate_of_distribution(reviews)
    star_rates(rate)


def find_word(review, start):
    place = start
    while place < len(review):
        space, length = find_space(review, place)
        if space and place == start:
            start = start + length
        elif space:
            break
        place = place + 1
    word = review[start:place]
    print(word)
    return word, place


def find_space(review, location):
    char = review[location]
    long_char = review[location:location + 2]
    med_char = review[location:location + 1]

    single_char_punctuation = [' ', '.', ',', ';', '!', '?', '(', ')', '-']
    med_char_punctuation = ['--']
    long_char_punctuation = ["\\n", '\\"']

    if char in single_char_punctuation:
        return True, 1
    if med_char is med_char_punctuation:
        return True, 2
    if long_char in long_char_punctuation:
        return True, 3

    return False, 0

# need to convert words to all lower case to see the ammount of words
# then order the words


def word_count():
    next_start = 0
    words = {}
    loop = 0
    for x in data:
        if loop % 1000:
            print(loop)
        loop = loop + 1
        if loop < 8000:
            review = x[0]
            while next_start < len(review):
                word, next_start = find_word(review, next_start)
                if word in words:
                    words[word] = words[word] + 1
                else:
                    words[word] = 1
            next_start = 0
        else:
            break
    print(words)


word_count()
