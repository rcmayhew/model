# this is the first id to check ('JNXUYY8wbaaDmk3BPzlWw', 7968)

file_review = "yelp_academic_dataset_review.json"
file_location = "C:\Data\yelp"
json_review = "%s\%s" % (file_location, file_review)
tested_id = "JNXUYY8wbaaDmk3BPzlWw"


def check_bus_id(review, biz_id="JNXUYY8wbaaDmk3BPzlWw"):
    checked_id = review[89:110]

    if checked_id == biz_id:
        return True
    return False


def tuple_data(review):
    stars = review[120]
    text = review[151:600]
    return text, stars


def get_reviews(biz_id):
    data = []
    loop = 0
    for line in open(json_review, encoding="utf8"):
        if loop % 100000 == 0:
            print("loop: %s" % loop)
        if check_bus_id(line, biz_id):
            data.append(tuple_data(line))
        loop = loop + 1

    print(len(data))
    return data


def add_data(data, name_of_var):
    with open('mod\data_lists.py', 'a') as f:
        f.write(name_of_var + " = " + str(data))


review_list = get_reviews(tested_id)
add_data(review_list, "selected_reviews")
