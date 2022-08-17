from redis_om import get_redis_connection, HashModel

# [this should be a different database]
redis = get_redis_connection(
    host="redis-14080.c53.west-us.azure.cloud.redislabs.com",
    port=14080,
    password="CflC19i7IqxkcfGcUykRqwE6nHWBnoDt",
    decode_responses=True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str # pending, completed. refunded
    
    class Meta:
        database = redis


# should be imported from original app
inventory_redis = get_redis_connection(
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
        database = inventory_redis