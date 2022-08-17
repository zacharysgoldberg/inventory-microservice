from database.database import Order, redis, Product
import time


def order_completed(order: Order):
    time.sleep(5)
    try:
        product = Product.get(order.product_id)
        print(product)
        if order.quantity <= product.quantity:
            order.status = 'completed'
            order.save()
            product.quantity = product.quantity - int(order.quantity)
            product.save()
            redis.xadd('order_completed', order.dict(), '*')
            print("\n----- Order Successfully Completed -----")
    
        else:
            order.status = 'refunded'
            order.save()
            redis.xadd('refund_order', order.dict(), '*')
            print("\n----- Order Refunded -----")
            
    except Exception as e:
        print("\n----- Product Not Found -----")