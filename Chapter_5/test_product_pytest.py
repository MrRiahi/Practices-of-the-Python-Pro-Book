from product import Product


class TestProduct:
    """
    Unit tests with pytest
    """

    @staticmethod
    def test_transform_name_for_sku():
        """
        Test case for transform_name_for_sku method in Product class.
        :return:
        """

        sku = Product(name='shoes', color='black', size='S')

        real_value = sku.transform_name_to_sku()
        expected_value = 'SHOES'

        assert real_value == expected_value

    @staticmethod
    def test_transform_space_name_for_sku():
        """
        Test case for transform_name_for_sku method for names with spaces.
        :return:
        """

        sku = Product(name='top tank', color='black', size='S')

        real_value = sku.transform_name_to_sku()
        expected_value = 'TOPTANK'

        assert real_value == expected_value

    @staticmethod
    def test_transform_color_for_sku():
        """
        Test case for transform_color_for_sku method in Product class.
        :return:
        """

        sku = Product(name='shoes', color='black', size='S')

        real_value = sku.transform_color_to_sku()
        expected_value = 'BLACK'

        assert real_value == expected_value

    @staticmethod
    def test_generate_sku():
        """
        Test case for generate sku method in Product class.
        :return:
        """

        sku = Product(name='shoes', color='black', size='S')

        real_value = sku.generate_sku()
        expected_value = 'SHOES-S-BLACK'

        assert real_value == expected_value
