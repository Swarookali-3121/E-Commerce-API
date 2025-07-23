from fastapi import APIRouter,Depends,status
from settings import database
from sqlalchemy.orm import Session
from handlers.authhandler import Verify_Admin
from handlers.adminhandler import Update_Admin, Get_All_Order, Update_Order_Status, Get_Order_By_Status
from models import schemas
from typing import List

router = APIRouter(tags=["Admin"])

@router.put("/update-to-admin/{user_id}", status_code=status.HTTP_200_OK)
async def update_to_admin(user_id: int, admin: bool = Depends(Verify_Admin), db: Session = Depends(database.get_db)):
    updated_user = Update_Admin(user_id, db)
    return updated_user

@router.get("/get_allorders", status_code=status.HTTP_200_OK)
async def all_orders(admin: bool = Depends(Verify_Admin), db: Session = Depends(database.get_db)):
    orders = Get_All_Order(db)
    return orders

@router.put("/order/update/status/{order_id}", response_model=List[schemas.OrderStatus], status_code=status.HTTP_200_OK)
async def update_order_by_status(status:str, admin:bool=Depends(Verify_Admin), db: Session = Depends(database.get_db)):
    status = update_order_by_status(status, db)
    return status

@router.get("/getorders-bystatus",response_model=List[schemas.OrderStatus], status_code=status.HTTP_200_OK)
async def get_orders_by_status(status: str, admin: bool = Depends(Verify_Admin), db: Session = Depends(database.get_db)):
    order_by_status = Get_Order_By_Status(status, db)
    return order_by_status