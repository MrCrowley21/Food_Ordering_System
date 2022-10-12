import logging
from threading import Thread
from flask import Flask, request, jsonify

from Components_logic.Food_ordering_system import *
from Components_logic.Client_service_order import *

# initialize the logger mode
logging.basicConfig(level=logging.DEBUG)

# initialize the server (app)
app = Flask(__name__)


# define server function to get registration data from restaurants
@app.route('/register', methods=['POST'])
def register():
    received_registration = request.json  # extract sent data
    logging.info(f'Get registration data from restaurant {received_registration["restaurant_name"]}')
    food_ordering_system.register_restaurant(received_registration)
    return jsonify(received_registration)


@app.route('/order', methods=['POST'])
def get_orders():
    order = request.json  # extract sent data
    logging.info(f'Received the order from the client {order["client_id"]}')
    client_service_order = ClientServiceOrder(order)
    Thread(target=food_ordering_system.distribute_order_to_dinning_halls, args=(client_service_order,))
    return jsonify(order)


@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(food_ordering_system.restaurant_data.__dict__)


# start the program execution
if __name__ == "__main__":
    # initialize server as a thread
    Thread(target=lambda: app.run(port=5004, host="0.0.0.0", debug=True, use_reloader=False)).start()
    food_ordering_system = FoodOrderingSystem()
