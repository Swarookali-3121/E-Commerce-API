from fastapi import Depends, Request
from sqlalchemy.orm import Session
from settings import database
from models import models, schemas
from handlers.authhandler import UserHandler
from utils.exceptions import ErrorHandler
from sqlalchemy.orm import joinedload


def Create_Order(req: schemas.Order, db: Session = Depends(database.get_db)):
    new_order = models.Order(req.model_dump(exclude={"products"}))
    db.add(new_order)
    db.commit()

    for items in req.product:
        product_data = models.Products(items.model_dump(exclude=None))
        db.add(product_data)
        db.commit()
    return [req]

def Cancel_Order(order_id: int, request:Request, db: Session = Depends(database.get_db)):
    current_user = UserHandler(request, db)
    user_order = db.query(models.Order).filter(models.Order.user_id == order_id).first()
    
    if order_id not in [order.order_id for order in user_order]:

        ErrorHandler.Forbidden("You are not authorized to cancel this order")
    cance_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    db.delete(cance_order)
    db.commit()
    return {"message": "Order and associated products cancelled"}

def Get_User_Orders(user_id: int, request: Request, db: Session = Depends(database.get_db)):
    current_user = UserHandler(request, db)
    if current_user.user_id == user_id:
        orders = db.query(models.Order).filter(models.Order.user_id == user_id).all()
        return orders
    ErrorHandler.Forbidden("You are not authorized to view this order")

def Get_Order_By_ID(order_id: int, db:Session):
    order = db.query(models.Order).filter(joinedload(models.Order.products)).filter(models.Order.order_id == order_id).first()
    if order is None:
        ErrorHandler.NotFound("Order not found")
    order_columns = order.__table__.columns
    order_dict = {c.name: getattr(order, c.name) for c in order_columns}

    if order.products:
        product_columns = order.products[0].__table__.columns
        order_dict['products'] = [{c.name: getattr(product, c.name) for c in product_columns} for product in order.products]
    return [order_dict]

def Get_Order_Status(order_id: int, db: Session = Depends(database.get_db)):
    order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not order:
        ErrorHandler.NotFound("Order not found")
    return order