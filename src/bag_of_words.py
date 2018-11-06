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


def find_space(review):



def word_count():
    for x in data:
        y = x
    print(y[0])


word_count()
