from sqlalchemy.orm import Session
import models
import schemas
from fastapi.encoders import jsonable_encoder


def obter_produto_por_id(db: Session, id_produto: int):
    return db.query(models.Produto).filter(models.Produto.productKey == id_produto).first()

def obter_produtos(db: Session):
    return db.query(models.Produto).all()

def novo_produto(db: Session, produto: schemas.CriarProduto):
    db_produto = models.Produto(productKey=produto.productKey, 
                                 productSubcategoryKey=produto.productSubcategoryKey, 
                                 productSKU=produto.productSKU,
                                 productName=produto.productName, 
                                 modelName=produto.modelName, 
                                 productDescription=produto.productDescription, 
                                 productColor=produto.productColor, 
                                 productSize=produto.productSize, 
                                 productStyle=produto.productStyle,  
                                 productCost=produto.productCost, 
                                 productPrice=produto.productPrice)
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


def alterar_produto(db: Session , id_produto: int, produto: schemas.AtualizarProduto):
    db_produto = obter_produto_por_id(db, id_produto=id_produto)
    update_produto_encoded = jsonable_encoder(produto)
    try:
        if update_produto_encoded['productSubcategoryKey']:
            db_produto.productSubcategoryKey = update_produto_encoded['productSubcategoryKey']
    except:
        pass
    try:
        if update_produto_encoded['productSKU']:
            db_produto.productSKU = update_produto_encoded['productSKU']
    except:
        pass
    try:
        if update_produto_encoded['productName']:
            db_produto.productName = update_produto_encoded['productName']
    except:
        pass
    try:
        if update_produto_encoded['modelName']:
            db_produto.modelName = update_produto_encoded['modelName']
    except:
        pass
    try:
        if update_produto_encoded['productDescription']:
            db_produto.productDescription = update_produto_encoded['productDescription']
    except:
        pass
    try:
        if update_produto_encoded['productColor']:
            db_produto.productColor = update_produto_encoded['productColor']
    except:
        pass
    try:
        if update_produto_encoded['productSize']:
            db_produto.productSize = update_produto_encoded['productSize']
    except:
        pass
    try:
        if update_produto_encoded['productStyle']:
            db_produto.productStyle = update_produto_encoded['productStyle']
    except:
        pass
    try:
        if update_produto_encoded['productCost']:
            db_produto.productCost = update_produto_encoded['productCost']
    except:
        pass
    try:
        if update_produto_encoded['productPrice']:
            db_produto.productPrice = update_produto_encoded['productPrice']
    except:
        pass

    atualizar_produto = db.merge(db_produto)
    db.commit()
    return atualizar_produto


def excluir_produto(db: Session , id_produto: int):
    db_produto = obter_produto_por_id(db=db, id_produto=id_produto)
    produto = jsonable_encoder(db_produto)
    db.delete(db_produto)
    db.commit()
    return produto 

