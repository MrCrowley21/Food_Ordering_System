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
        self.order_id = 1
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

    def update_restaurant_data(self):
        restaurants = []
        for restaurant in self.restaurant_data.restaurants_data:
            updates = requests.get(f'{restaurant["address"]}update_data').json()
            restaurant['rating'] = updates['rating']
            if updates['is_available']:
                restaurants.append(restaurant)
        return {'restaurants': len(restaurants), 'restaurants_data': restaurants}

    def distribute_order_to_dinning_halls(self, orders):
        responses = []
        logging.info(f'{orders}')
        client_id = orders.client_id
        for individual_order in orders.orders:
            restaurant_id = individual_order['restaurant_id']
            individual_order['client_id'] = client_id
            logging.info(f'Sending received order to the restaurant {restaurant_id}')
            response = requests.post(f'{self.restaurant_routes[restaurant_id]}v2/order', json=individual_order).json()
            logging.info(f'Receiving response from the restaurant {response["restaurant_id"]} with the following '
                         f'structure:\n{response}')
            responses.append(response)
        logging.info(f'Order of client {orders.client_id} has been successfully sent to the dinning hall')
        return {'order_id': client_id, 'orders': responses}
