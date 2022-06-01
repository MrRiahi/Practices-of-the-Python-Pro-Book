import unittest

from product import Product


class ProductTestCase(unittest.TestCase):

    def test_transform_name_for_sku(self):
        """
        Test case for transform_name_for_sku method in Product class.
        :return:
        """

        sku = Product(name='shoes', color='black', size='S')

        real_value = sku.transform_name_to_sku()
        expected_value = 'SHOES'

        self.assertEqual(first=real_value, second=expected_value)

    def test_transform_color_for_sku(self):
        """
        Test case for transform_color_for_sku method in Product class.
        :return:
        """

        sku = Product(name='shoes', color='black', size='S')

        real_value = sku.transform_color_to_sku()
        expected_value = 'BLACK'

        self.assertEqual(first=real_value, second=expected_value)