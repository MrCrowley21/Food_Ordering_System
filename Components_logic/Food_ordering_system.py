import logging
from threading import Lock
from copy import copy
import requests

from Components_logic.Restaurant_data import *


class FoodOrderingSystem:
    def __init__(self):
        self.restaurant_data = RestaurantData()
        self.restaurant_routes = {}
        self.lock = Lock()

    def register_restaurant(self, restaurant_registration):
        with self.lock:
            self.restaurant_data.restaurants += 1
            self.restaurant_data.restaurants_data.append(restaurant_registration)
            restaurant_id = self.restaurant_data.restaurants_data['restaurant_id']
            restaurant_path = self.restaurant_data.restaurants_data['address']
            self.restaurant_routes[restaurant_id] = restaurant_path
            logging.info(f'The restaurant {restaurant_registration["restaurant_name"]} has been registered into '
                         f'the food ordering system')
            logging.info(f'{self.restaurant_data.__dict__}')

    def distribute_order_to_dinning_halls(self, orders):
        for individual_order in orders.orders:
            restaurant_id = individual_order.restaurant_id
            order_to_send = copy(individual_order)
            order_to_send.pop('restaurant_id', None)
            logging.info(f'Sending received order to the restaurant {restaurant_id}')
            requests.post(f'{self.restaurant_routes[restaurant_id]}receive_prepared_order',
                          json=order_to_send)
        logging.info(f'Order of client {orders.client_id} has been successfully sent to the dinning hall')

