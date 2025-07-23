from sqlalchemy import Integer, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from pydantic import EmailStr
from settings.database import Base

class User(Base):
    __tablename__ = "users"
    user_id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True,autoincrement=True)
    name:Mapped[str]=mapped_column(String)
    email:Mapped[str] = mapped_column(String,nullable=False)
    password:Mapped[str] = mapped_column(String)
    time : Mapped[str] = mapped_column(TIMESTAMP,default=datetime.now())
    is_admin: Mapped[bool] =mapped_column(Boolean,default=False)

    order = relationship("Order", back_populates="users")

class Order(Base):
    __tablename__="orders"
    order_id: Mapped[int]=mapped_column(Integer,primary_key=True)
    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.user_id"))
    status: Mapped[str]=mapped_column(String,default="pending")

    users=relationship("User",back_populates="order")

    products = relationship("Products",back_populates="order",cascade="all, delete-orphan")


class ResetToken(Base):
    __tablename__ ="ResetTokens"
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    email:Mapped[str]=mapped_column(String,nullable=False)
    token:Mapped[str]=mapped_column(String)

class Products(Base):
    __tablename__="products"
    order_id:Mapped[int] = mapped_column(Integer,ForeignKey("orders.order_id"),primary_key=True)
    product_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String)
    price:Mapped[int] = mapped_column(Integer)
    quantity:Mapped[int] = mapped_column(Integer,default=1)
    total:Mapped[int]=mapped_column(Integer)
    order = relationship("Order",back_populates="products")
    