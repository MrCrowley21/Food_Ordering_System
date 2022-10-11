import logging

from Components_logic.Restaurant_data import *


class FoodOrderingSystem:
    def __init__(self):
        self.restaurant_data = RestaurantData()

    def register_restaurant(self, restaurant_registration):
        self.restaurant_data.restaurants += 1
        self.restaurant_data.restaurants_data.append(restaurant_registration)
        logging.info(f'The restaurant {restaurant_registration["restaurant_name"]} has been registered into '
                     f'the food ordering system')
        logging.info(f'{self.restaurant_data.__dict__}')
