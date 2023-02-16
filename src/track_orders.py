class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def products_per_customer(self, customer):
        products = {}
        for name, product, _day in self.orders:
            if name == customer:
                products.setdefault(product, 0)
                products[product] += 1
        return products

    def get_most_ordered_dish_per_customer(self, customer):
        product_customer = self.products_per_customer(customer)
        return max(product_customer, key=product_customer.get)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
