from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import Product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
async def root():
    return {"message": "Hello"}


def format(pk: str):
    product = Product.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.get('/products')
async def get_all_products(): 
    return [format(pk) for pk in Product.all_pks()]


@app.post('/products')
async def create_product(product: Product):
    return product.save()


@app.get('/products/{pk}')
async def get_product(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
async def delete_product(pk: str):
    return Product.delete(pk)


