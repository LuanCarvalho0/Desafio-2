from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class Produto(Base):
    __tablename__ = "products"

    productKey = Column(Integer, primary_key=True)
    productSubcategoryKey = Column(Integer)
    productSKU = Column(String)
    productName = Column(String)
    modelName = Column(String)
    productDescription = Column(String)
    productColor = Column(String)
    productSize = Column(String)
    productStyle = Column(String)
    productCost = Column(Float)
    productPrice = Column(Float)

