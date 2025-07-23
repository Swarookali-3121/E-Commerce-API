from fastapi import HTTPException, Depends
from settings import database
from models import models, schemas
from sqlalchemy.orm import Session
from utils.exceptions import ErrorHandler
from handlers import userhandler
from sqlalchemy.orm import joinedload


def Update_Admin(user_id: int,db: Session = Depends(database.get_db)):
    try:
        user_data = userhandler.is_User(user_id, db)
        if user_data:
            user_update = db.query(models.User).filter(models.User.user_id == user_id).first()
            user_update.is_admin = True
            db.add(user_update)
            db.commit()
            db.refresh(user_update)
            return {"message": "User has been updated to admin successfully"}
        
    except Exception as e:
        ErrorHandler.Unauthorized(e)    

def Get_All_Order(db: Session = Depends(database.get_db)):
    orders = db.query(models.Order).options(joinedload(models.Order.products)).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No order found")
    order_list = []
    for order in orders:
        order_dict = {c.name: getattr(order, c.name) for c in order.__table__.columns}
        order_dict['products'] = [
            {c.name: getattr(product, c.name) for c in product.__table__.columns}
            for product in order.products
        ]
        order_list.append(order_dict)
    return order_list

def Update_Order_Status(order_id: int, status: str, db: Session = Depends(database.get_db)) -> schemas.OrderStatus:
    order = db.query(models.Order).filter(models.Order.order_id == order_id).first()

    if not order:
        ErrorHandler.NotFound("Order not found")
    order.status = status
    db.add(order)
    db.commit()
    db.refresh()

    return [order]

def Get_Order_By_Status(status: str, db: Session = Depends(database.get_db)):
    try:
        if status not in ["pending", "delivered", "cancelled"]:
            ErrorHandler.NotFound("Invalid status,status can be either pending,delivered or cancelled")
            orders = db.query(models.Order).filter(models.Order.status == status).all()
            if not orders:
                return {"message": "No order found"}
            return orders
    except Exception as e:
        ErrorHandler.Error(e)

        