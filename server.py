import logging
from threading import Thread
from flask import Flask, request, jsonify

from Components_logic.Food_ordering_system import *

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


@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(food_ordering_system.restaurant_data.__dict__)


# start the program execution
if __name__ == "__main__":
    # initialize server as a thread
    Thread(target=lambda: app.run(port=5004, host="0.0.0.0", debug=True, use_reloader=False)).start()
    food_ordering_system = FoodOrderingSystem()
