class ClientServiceOrder:
    def __init__(self, order):
        self.order_id = order['client_id']
        self.client_id = order['client_id']
        self.orders = order['orders']
