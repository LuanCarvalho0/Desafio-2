# Desafio-2
API em FastAPI

# Documentação da API CRUD PRODUTOS

## Visão geral
Esta documentação descreve as operações CRUD (Create, Read, Update, Delete) disponíveis na API.

## Base URL
A URL base para todas as solicitações é: `http://127.0.0.1:8000/`

## Endpoints

### 1. Produtos

#### 1.1 Listar produtos
Retorna uma lista de todos os produtos disponíveis.

- **URL:** `/products`
- **Método:** GET
- **Parâmetros da consulta:** Nenhum
- **Resposta de sucesso:** 200 OK
  - **Exemplo de resposta:**
    ```json
    [
      {
        "productKey": 214,
        "productSubcategoryKey": 31,
        "productSKU": "HL-U509-R",
        "productName": "Sport-100 Helmet, Red",
        "modelName": "Sport-100",
        "productDescription": "Universal fit, well-vented, lightweight , snap-on visor.",
        "productColor": "Red",
        "productSize": "0",
        "productStyle": "0",
        "productCost": 13.0863,
        "productPrice": 34.99
    },
    {
        "productKey": 215,
        "productSubcategoryKey": 31,
        "productSKU": "HL-U509",
        "productName": "Sport-100 Helmet, Black",
        "modelName": "Sport-100",
        "productDescription": "Universal fit, well-vented, lightweight , snap-on visor.",
        "productColor": "Black",
        "productSize": "0",
        "productStyle": "0",
        "productCost": 12.0278,
        "productPrice": 33.6442
    }
    ]
    ```

#### 1.2 Obter um produto
Retorna os detalhes de um produto específico.

- **URL:** `/products/{id_produto}`
- **Método:** GET
- **Parâmetros da URL:**
  - `id_produto` (inteiro) - O ID do produto desejado.
- **Resposta de sucesso:** 200 OK
  - **Exemplo de resposta:**
    ```json
    {
        "productKey": 214,
        "productSubcategoryKey": 31,
        "productSKU": "HL-U509-R",
        "productName": "Sport-100 Helmet, Red",
        "modelName": "Sport-100",
        "productDescription": "Universal fit, well-vented, lightweight , snap-on visor.",
        "productColor": "Red",
        "productSize": "0",
        "productStyle": "0",
        "productCost": 13.0863,
        "productPrice": 34.99
    }
    ```

#### 1.3 Criar um produto
Cria um novo produto.

- **URL:** `/products`
- **Método:** POST
- **Parâmetros da solicitação:**
  - `productKey` (inteiro) 
  - `productSubcategoryKey` (inteiro) 
  - `productSKU` (string)
  - `productName` (string)
  - `modelName` (string)
  - `productDescription` (string)
  - `productColor` (string)
  - `productSize` (string)
  - `productStyle` (string)
  - `productCost` (float)
  - `productPrice` (float)
- **Resposta de sucesso:** 201 Created
  - **Exemplo de resposta:**
    ```json
    {
        "productKey": 214,
        "productSubcategoryKey": 31,
        "productSKU": "HL-U509-R",
        "productName": "Sport-100 Helmet, Red",
        "modelName": "Sport-100",
        "productDescription": "Universal fit, well-vented, lightweight , snap-on visor.",
        "productColor": "Red",
        "productSize": "0",
        "productStyle": "0",
        "productCost": 13.0863,
        "productPrice": 34.99
    }
    ```

#### 1.4 Atualizar um produto
Atualiza os detalhes de um produto existente.

- **URL:** `/products/{id_produto}`
- **Método:** PUT
- **Parâmetros da URL:**
  - `id_produto` (inteiro) - O ID do produto a ser atualizado.
- **Parâmetros da solicitação:**
  - `productName` (string) - O novo nome do produto.
- **Resposta de sucesso:** 200 OK
  - **Exemplo de resposta:**
    ```json
    {
        "productKey": 214,
        "productSubcategoryKey": 31,
        "productSKU": "HL-U509-R",
        "productName": "Sport-100 Helmet, Red",  (Recurso atualizado)
        "modelName": "Sport-100",
        "productDescription": "Universal fit, well-vented, lightweight , snap-on visor.",
        "productColor": "Red",
        "productSize": "0",
        "productStyle": "0",
        "productCost": 13.0863,
        "productPrice": 34.99
    }
    ```

#### 1.5 Excluir um produto
Exclui um produto existente.

- **URL:** `/products/{id_produto}`
- **Método:** DELETE
- **Parâmetros da URL:**
  - `id_produto` (inteiro) - O ID do produto a ser excluído.
- **Resposta de sucesso:** 204 No Content
 ```json
 {
   "Produto Excluido com Sucesso! {'productName': 'Road-750 Black, 52', 'productDescription': 'Entry level adult bike; offers a comfortable ride cross-country or down the block. Quick-release hubs and rims.', 'productSize': '52', 'productCost': 343.6496, 'modelName': 'Road-750', 'productSubcategoryKey': 2, 'productSKU': 'BK-R19B-52', 'productKey': 606, 'productColor': 'Black', 'productStyle': 'U', 'productPrice': 539.99}"
   }
   ```
