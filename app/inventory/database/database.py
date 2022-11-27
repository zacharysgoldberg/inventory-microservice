# from typing import Union
from redis_om import get_redis_connection, HashModel


redis = get_redis_connection(
    host="inventory_microservice-redis-1",
    port=6379,
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity: int
    # description: Union[str, None] = None

    class Meta:
        database = redis
