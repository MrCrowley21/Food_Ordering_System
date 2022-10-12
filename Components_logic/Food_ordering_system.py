import logging
from threading import Lock
from copy import copy
import requests
import json

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
            restaurant_id = restaurant_registration['restaurant_id']
            restaurant_path = restaurant_registration['address']
            self.restaurant_routes[restaurant_id] = restaurant_path
            logging.info(f'The restaurant {restaurant_registration["restaurant_name"]} has been registered into '
                         f'the food ordering system')
            logging.info(f'{self.restaurant_data.__dict__}')

    def distribute_order_to_dinning_halls(self, orders):
        for individual_order in orders.orders:
            logging.info(f'121212 {individual_order}')
            restaurant_id = individual_order['restaurant_id']
            logging.info(f'1111111 {orders.orders}')
            # order_to_send = copy(individual_order)
            # order_to_send.pop('restaurant_id', None)
            # logging.info(f'{order_to_send}')
            logging.info(f'Sending received order to the restaurant {restaurant_id}')
            logging.info(f'4444444 {self.restaurant_routes[restaurant_id]}v2/order')
            requests.post(f'{self.restaurant_routes[restaurant_id]}order', json=individual_order)
        logging.info(f'Order of client {orders.client_id} has been successfully sent to the dinning hall')

