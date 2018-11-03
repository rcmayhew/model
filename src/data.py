# data updated 10/30/2018
# location of data on personal machine: C:\Data\yelp
# name of data: yelp_academic_dataset_review.json
# <a href="/biz_attribute?biz_id=VJ6UJWMQqBat4s_sNUlEiw" class="link-more icon-wrapper mapbox-edit">
#   it looks like the id is VJ6UJWMQqBat4s_sNUlEiw
#   "business_id": "VJ6UJWMQqBat4s_sNUlEiw"
"""
so need to find the business id of the exacat location
then pull all reviews from that business
then pull only the string and the star reviews of each review
then store as either csv, numpy array, or pandas dataframe
"""

from src import mod as dl

file_location = "C:\Data\yelp"
store_location = "C:\\User\\1robb\PycharmProjects\hwhelp\mod"
file_review = "yelp_academic_dataset_review.json"
file_biz = "yelp_academic_dataset_business.json"
json_review = "%s\%s" % (file_location, file_review)
json_biz = "%s\%s" % (file_location, file_biz)


def check_num_reviews(data_given):
    return data_given.size()


def check_bus_id(review, biz_id="VJ6UJWMQqBat4s_sNUlEiw"):
    checked_id = review[89:110]

    if checked_id == biz_id:
        return True
    return False


def give_bus_id(review):
    return review[89:110]


def give_stars(review):
    return review[121:122]


def tuple_data(review):
    stars = review[120]
    text = review[151:600]
    return text, stars


def get_review():
    data = []
    limiter = 0
    loop = 0
    for line in open(json_review, encoding="utf8"):
        loop = loop + 1
        if loop % 100000 == 0:
            print("loop: %s" % loop)
        if check_bus_id(line):
            limiter = limiter + 1
            data.append(tuple_data(line))
        if limiter > 10:
            break

    print(data)
    return data


def get_biz_ids():
    data = {}
    loop = 0
    for line in open(json_review, encoding="utf8"):
        loop = loop + 1
        if loop % 100000 == 0:
            print("biz loop: %s" % loop)
        name = give_bus_id(line)
        if name not in data:
            data[name] = 1
        else:
            data[name] = data[name] + 1
    return data


def add_data(data, name_of_var, threshold=0):
    for element in data:
        if int(element[2]) < threshold:
            del data[element[0]]
    sorted(data.values())
    biz_ids = sorted(data.items(), reverse=True, key=lambda x: x[1])
    with open(store_location + 'data_lists.py', 'a') as f:
        f.write(name_of_var + " = " + str(biz_ids))


def get_top():
    biz = dl.data_lists.biz_ids
    last_key = 0
    for key, value in enumerate(biz):
        if value[1] < 1000:
            last_key = key
            break
    biz = dl.biz_ids[0:last_key]
    return biz

"""
find a biz that is not a uniform distribution. that makes it less likely to randomly overfit the data.
so need to make sure that there are a both a varied number of star reviews, and the variation is high
"""

def get_star_amount(top_biz):
    biz_key = []
    for key, value in top_biz:
        biz_key[value[0]] = {0, 0, 0, 0, 0}
    for line in open(json_review, encoding="utf8"):
        name = get_biz_ids()
        star = int(give_stars(line))
        if name in biz_key:
            base = biz_key[name]
            base[star] = base[star] + 1
            biz_key[name] = base


"""
by = get_top()
add_data(by, "top_biz_id")
"""


