from pydantic import BaseModel
from typing import Optional

class ProdutoBase(BaseModel):
    productKey: int
    productSubcategoryKey: int
    productSKU: Optional[str] = None
    productName: str
    modelName: str
    productDescription: str
    productColor: Optional[str] = None
    productSize: str
    productStyle: str
    productCost: float
    productPrice: float

class CriarProduto(ProdutoBase):
    pass

class AtualizarProduto(BaseModel):
 
    productSubcategoryKey: Optional[int] = None
    productSKU: Optional[str] = None
    productName: Optional[str] = None
    modelName: Optional[str] = None
    productDescription: Optional[str] = None
    productColor: Optional[str] = None
    productSize: Optional[str] = None
    productStyle: Optional[str] = None
    productCost: Optional[float] = None
    productPrice: Optional[float] = None

class Produto(ProdutoBase):
    pass

    class Config:
        orm_mode = True