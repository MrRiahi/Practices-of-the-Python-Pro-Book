import io
import unittest
from unittest import mock

from tax import add_sales_tax


class SalesTaxTestCase(unittest.TestCase):

    @mock.patch('tax.urlopen')
    def test_add_sales_tax_from_api(self, mock_urlopen):
        """
        Test case for add_sales_tax using mock.
        :param mock_urlopen:
        :return:
        """

        tax_rate = 1.06
        mock_urlopen.return_value = io.BytesIO(str(tax_rate).encode('utf-8'))

        real_value = add_sales_tax(original_amount=5, country='USA', region='MI')
        expected_value = 5 * tax_rate

        self.assertEqual(first=real_value, second=expected_value)
