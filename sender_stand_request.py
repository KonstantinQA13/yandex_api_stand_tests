import configuration
import requests
import data


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
                         headers=data.headers)


response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())