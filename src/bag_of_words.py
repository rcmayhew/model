from src import mod as dl
import matplotlib.pyplot as plt

data = dl.data_lists.selected_reviews


def rating_dist(data):
    rating = {0, 0, 0, 0, 0}
    for element in data:
        star = int(element[1])
        base = rating[star - 1]
        rating[star - 1] = base + 1
    return rating


def save_fig(figure):
    return 0


def star_distibution(data):
    plt.xlabel("Stars")
    plt.ylabel("Number Of Ratings")
    plt.title("Star Distribution")
    plt.hist(data)
    plt.show()
    return 0

reviews = rating_dist(data)
star_distibution(reviews)
