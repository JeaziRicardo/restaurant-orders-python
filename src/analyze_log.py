import csv


def get_orders(path_to_file):
    if not path_to_file.endswith("csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, "r") as file:
            orders = dict()
            reader = csv.reader(file)
            for name, product, day in reader:
                orders.setdefault(name, {"products": {}, "days": {}})
                count_products = orders[name]["products"].get(product, 0) + 1
                count_day = orders[name]["days"].get(day, 0) + 1
                orders[name]["products"][product] = count_products
                orders[name]["days"][day] = count_day
            return orders
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def get_products_and_days(orders):
    products = set()
    days = set()
    for name in orders:
        products.update(orders[name]["products"])
        days.update(orders[name]["days"])
    return [products, days]


def analyze_log(path_to_file):
    orders = get_orders(path_to_file)
    products, days = get_products_and_days(orders)
    maria_max_products = max(
        orders["maria"]["products"], key=orders["maria"]["products"].get
    )
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria_max_products}\n"
            + f"{orders['arnaldo']['products']['hamburguer']}\n"
            + f"{products.difference(orders['joao']['products'].keys())}\n"
            + f"{days.difference(orders['joao']['days'].keys())}"
        )
