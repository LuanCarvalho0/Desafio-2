from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import produtos
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependencias 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_main():
    return {"mensagem": "API Hackathon 2023 "}


# Rota - GET http://127.0.0.1:8000/products/
@app.get("/products/", response_model=list[schemas.Produto])
def obter_produtos(db: Session = Depends(get_db)):
    db_produtos = produtos.obter_produtos(db)
    return db_produtos

# Rota - GET http://127.0.0.1:8000/products/id_produto
@app.get("/products/{id_produto}", response_model=schemas.Produto)
def obter_produto_por_id(id_produto: int, db: Session = Depends(get_db)):
    db_produto = produtos.obter_produto_por_id(db, id_produto=id_produto)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado ")
    return db_produto


# Rota - POST http://127.0.0.1:8000/products/
@app.post("/products/", response_model=schemas.Produto)
def novo_produto(produto: schemas.CriarProduto, db: Session = Depends(get_db)):
    db_produto = produtos.obter_produto_por_id(db, id_produto=produto.productKey)
    if db_produto:
        raise HTTPException(status_code=400, detail="Codigo de produto ja cadastrado")
    return produtos.novo_produto(db=db, produto=produto)

# Rota - PUT http://127.0.0.1:8000/products/id_produto
@app.put("/products/{id_produto}", response_model=schemas.Produto)
def alterar_produto(id_produto: int, produto: schemas.AtualizarProduto, db: Session = Depends(get_db)):
    db_produto = produtos.obter_produto_por_id(db, id_produto=id_produto)

    if db_produto:
        return produtos.alterar_produto(db=db, id_produto=id_produto ,produto=produto)
    else:
        raise HTTPException(status_code=400, detail='Produto não encontrado com o ID fornecido')


# Rota - DELETE http://127.0.0.1:8000/products/id_produto
@app.delete("/products/{id_produto}")
def excluir_produto(id_produto: int, db: Session = Depends(get_db)):
    db_produto = produtos.obter_produto_por_id(db=db, id_produto=id_produto)
    if db_produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrada com o ID fornecido')
    produto = produtos.excluir_produto(db, id_produto)
    return f"Produto Excluido com Sucesso! {produto}"

