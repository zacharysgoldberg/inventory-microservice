from fastapi import FastAPI
# from threading import Thread
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from starlette.requests import Request
from database.database import Order
from consumer.complete_order import order_completed
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)
        
        
@app.get('/orders/{pk}')
async def get_order(pk: str):
    return Order.get(pk)


@app.post('/orders')
async def create_order(request: Request, background_tasks: BackgroundTasks):   
    body = await request.json() # id, quantity
    
    url = f"http://inventory:8000/products/{body['id']}"
    print(url)
    response = requests.get(url=url)
    product = response.json()
    
    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=round(0.2 * product['price'], 2),
        total=round(1.2 * product['price'], 2),
        quantity=body['quantity'],
        status='pending'
    )
    
    order.save()
    
    # thread = Thread(target=order_completed)
    # thread.daemon = True
    
    # thread.start()
    
    background_tasks.add_task(order_completed, order)
        
    return order

