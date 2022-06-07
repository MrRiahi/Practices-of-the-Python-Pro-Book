
class Product:
    """
    A product class for an e-commerce system.
    Stock Keeping Unit (SKU).
    """

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    @staticmethod
    def remove_space(name):
        return ''.join(name.split())

    def transform_name_to_sku(self):
        return self.remove_space(name=self.name.upper())

    def transform_color_to_sku(self):
        return self.color.upper()

    def generate_sku(self):
        """
        Generates a SKU for this product.
        Example:
            >>> small_black_shoes = Product('shoes', 'S', 'black')
            >>> small_black_shoes.generate_sku()
        'SHOES-S-BLACK'
        :return:
        """

        name = self.transform_name_to_sku()
        color = self.transform_color_to_sku()

        sku = f'{name}-{self.size}-{color}'

        return sku
