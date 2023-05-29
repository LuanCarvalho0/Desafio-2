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
        "id": 1,
        "nome": "Recurso 1"
      },
      {
        "id": 2,
        "nome": "Recurso 2"
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
      "id": 1,
      "nome": "Recurso 1"
    }
    ```

#### 1.3 Criar um produto
Cria um novo produto.

- **URL:** `/products`
- **Método:** POST
- **Parâmetros da solicitação:**
  - `nome` (string) - O nome do novo recurso.
- **Resposta de sucesso:** 201 Created
  - **Exemplo de resposta:**
    ```json
    {
      "id": 3,
      "nome": "Novo Recurso"
    }
    ```

#### 1.4 Atualizar um produto
Atualiza os detalhes de um produto existente.

- **URL:** `/products/{id_produto}`
- **Método:** PUT
- **Parâmetros da URL:**
  - `id_produto` (inteiro) - O ID do produto a ser atualizado.
- **Parâmetros da solicitação:**
  - `nome` (string) - O novo nome do recurso.
- **Resposta de sucesso:** 200 OK
  - **Exemplo de resposta:**
    ```json
    {
      "id": 3,
      "nome": "Recurso Atualizado"
    }
    ```

#### 1.5 Excluir um produto
Exclui um produto existente.

- **URL:** `/products/{id_produto}`
- **Método:** DELETE
- **Parâmetros da URL:**
  - `id` (inteiro) - O ID do produto a ser excluído.
- **Resposta de sucesso:** 204 No Content
