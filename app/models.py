from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String

class Account(Base):
    __tablename__ = 'account'
    AccountId = Column(Integer, primary_key=True, index=True)
    UserName  = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    FullName = Column(String, nullable=True)
    PhoneNumber = Column(String, nullable=False, default=True)
    CreateDate = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    UpdateDate = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
    Role = Column(String, nullable=True)
    
    basket = relationship('Basket', uselist=False, back_populates="Account")
    bill = relationship('Bill', back_populates="Account")
    
class Restaurant(Base):
    __tablename__ = 'restaurant'
    RestaurantId = Column(Integer, primary_key=True, index=True)
    RestaurantAdress  = Column(String, nullable=False)
    RestaurantDetail = Column(String, nullable=False)
    Distance = Column(String, nullable=True)
    PhoneNumber = Column(String, nullable=False, default=True)
    
    food = relationship("Food", back_populates="Restaurant")

class Food(Base):
    __tablename__ = 'food'
    FoodID = Column(Integer, primary_key=True, index=True)
    FoodName  = Column(String, nullable=False)
    Detail = Column(String, nullable=False)
    Quantity = Column(String, nullable=True)
    Price = Column(Integer, nullable=False)
    CreateDate = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    UpdateDate = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
    TypeFood = Column(Integer, nullable=False)
    StatusFood = Column(Integer, nullable=False)
    
    RestaurantId = Column("RestaurantId", Integer, ForeignKey(Restaurant.RestaurantId), nullable=True)
    
    restaurant = relationship("Restaurant", back_populates="Food")
    billdetail = relationship("BillDetail", back_populates="Food")
    
class Basket(Base):
    __tablename__ = 'basket'
    BasketId = Column(String, primary_key=True)
    AccountId = Column("AccountId", Integer, ForeignKey(Account.AccountId), nullable=True)
    FoodID = Column("FoodID", Integer, ForeignKey(Food.FoodID), nullable=True)
    
    account = relationship("Account", back_populates="Basket")
    food = relationship("Food", back_populates="Basket")

class Bill(Base):
    __tablename__ = 'bill'
    BillId = Column(Integer, primary_key=True, index=True)
    CreateDate = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    ReceiveDate = Column(TIMESTAMP(timezone=True),
                    nullable=False, server_default=func.now())
    CloseDate = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
    ShipPrice  = Column(Integer, nullable=False)
    BuyerNotification = Column(String, nullable=False)
    BillStatus = Column(String, nullable=True)
    BuyMethod = Column(String, nullable=False, default=True)
    TotalBill = Column(String, nullable=False, default=True)
    AccountShip = Column(Integer, nullable=False, default=True)
    ShipToBuyerDate = Column(String, nullable=False, default=True)
    
    AccountId = Column("AccountId", Integer, ForeignKey(Account.AccountId), nullable=True)
    
    account = relationship("Account", back_populates="Bill")
    billdetail = relationship("BillDetail", back_populates="Bill")
    
class BillDetail(Base):
    __tablename__ = 'billdetail'
    BillDetailID = Column(Integer, primary_key=True, index=True)
    Quantity = Column(String, nullable=True)
    Price = Column(Integer, nullable=False, default=True)
    
    bill = relationship("Bill", back_populates="BillDetail")
    food = relationship("Food", back_populates="BillDetail")
    
    BillId = Column("BillID", Integer, ForeignKey(Bill.BillId), nullable=True)
    FoodId = Column("FoodId", Integer, ForeignKey(Food.FoodID), nullable=True)
    
    
    

    
    

    