# from typing import Union
from redis_om import get_redis_connection, HashModel


redis = get_redis_connection(
    host="redis-14080.c53.west-us.azure.cloud.redislabs.com",
    port=14080,
    password="CflC19i7IqxkcfGcUykRqwE6nHWBnoDt",
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity: int
    # description: Union[str, None] = None

    class Meta:
        database = redis