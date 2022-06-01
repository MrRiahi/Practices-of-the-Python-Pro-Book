import unittest

from product import Product
from shipping_cart import ShippingCart


class ShippingCartTestCase(unittest.TestCase):

    def test_add_product(self):
        """
        Integration test case for adding product.
        :return:
        """

        product = Product(name='shoes', color='black', size='S')
        shipping_cart = ShippingCart()

        # Add product
        shipping_cart.add_product(product=product)

        expected_value = {'SHOES-S-BLACK': {'quantity': 1}}

        self.assertEqual(first=shipping_cart.products, second=expected_value)

    def test_remove_product(self):
        """
        Integration test case for removing product
        :return:
        """

        product = Product(name='shoes', color='black', size='S')
        shipping_cart = ShippingCart()

        # Add product
        shipping_cart.add_product(product=product)

        # Remove product
        shipping_cart.remove_product(product=product)

        expected_value = {'SHOES-S-BLACK': {'quantity': 0}}

        self.assertEqual(first=shipping_cart.products, second=expected_value)
