from datetime import datetime, timedelta
import random
import string


def gen_order_data_and_return_it():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_date():
        start_date = datetime(1970, 1, 1)
        end_date = datetime.now()

        random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        formatted_date = random_date.strftime('%Y-%m-%d')
        return (formatted_date)

    order_data = {}

    order_data["firstName"]= generate_random_string(10)
    order_data["lastName"]= generate_random_string(10)
    order_data["address"]= generate_random_string(10) + ' ' + str(random.randint(1, 900)) + ' ' + generate_random_string(3)
    order_data["metroStation"]= random.randint(1, 9)
    order_data["phone"]= '+7 '+ str(random.randint(1, 900)).zfill(3) + str(random.randint(0, 900)).zfill(3) \
                         + str(random.randint(0, 90)).zfill(2) + str(random.randint(0, 90)).zfill(2)
    order_data["rentTime"]= random.randint(1, 9)
    order_data["deliveryDate"]= generate_random_date()
    order_data["comment"]= generate_random_string(10)
    order_data["color"]= [random.choice(["BLACK", "GREY"])]

    return order_data



