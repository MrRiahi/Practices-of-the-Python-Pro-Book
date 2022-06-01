from collections import defaultdict


class ShippingCart:
    """
    Add and remove a product by managing the data in a dictionary
    """

    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))

    def add_product(self, product, quantity=1):
        """
        Add the product's quantity.
        :param product: product
        :param quantity: int value for product quantity
        :return:
        """

        sku = product.generate_sku()
        self.products[sku]['quantity'] += quantity

    def remove_product(self, product, quantity=1):
        """
        Remove the product's quantity
        :param product:
        :param quantity:
        :return:
        """

        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity

        if self.products[sku] == 0:
            del self.products[sku]
