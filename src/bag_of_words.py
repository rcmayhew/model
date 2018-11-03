from src import mod as dl

data = dl.data_lists.selected_reviews


def rating_dist(data):
    rating = {0, 0, 0, 0, 0}
    for element in data:
        star = int(element[1])
        base = rating[star - 1]
        rating[star - 1] = base + 1
    return rating

def graph(data):
    return 0