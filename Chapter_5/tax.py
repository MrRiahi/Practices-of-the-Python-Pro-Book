from urllib.request import urlopen


def add_sales_tax(original_amount, country, region):
    """
    Get the tax fee
    :param original_amount:
    :param country:
    :param region:
    :return:
    """

    sales_tax_rate = urlopen(f'https://tax-api.com/{country}/{region}').read().decode()

    return original_amount * float(sales_tax_rate)
