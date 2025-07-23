from fastapi import APIRouter,Depends,status
from settings import database
from sqlalchemy.orm import Session
from models import schemas
from utils.jwt_token import verify_token
from typing import List
from starlette.requests import Request
from handlers.orderhandler import Create_Order, Cancel_Order, Get_User_Orders, Get_Order_By_ID, Get_Order_Status

router = APIRouter(tags=["Order"], dependencies=[Depends(verify_token)])

@router.post("/createorder",status_code=status.HTTP_201_CREATED)
async def create_order(req: schemas.Order, db: Session = Depends(database.get_db)):
    new_order = Create_Order(req, db)
    return new_order

@router.delete("/cancel-order/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_order(order_id: int, request: Request, db: Session = Depends(database.get_db)):
    cancelled_order = Cancel_Order(order_id, request, db)
    return cancelled_order

@router.get("/user/order/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_order(user_id: int, request: Request, db: Session = Depends(database.get_db)):
    orders = Get_User_Orders(user_id, request, db)
    return orders

@router.get("/order/status/{order_id}", status_code=status.HTTP_200_OK,response_model=schemas.OrderStatus)
async def get_order_status(order_id: int, db: Session = Depends(database.get_db)):
    order_status = Get_Order_Status(order_id, db)
    return order_status

@router.get("/users/orders/{order_id}", response_model=List[schemas.Order], status_code=status.HTTP_200_OK)
async def get_order_by_id(order_id: int, db: Session = Depends(database.get_db)):
    orders = Get_Order_By_ID(order_id, db)
    return orders