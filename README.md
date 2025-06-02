# Projeto MongoDB com Python

Este é um projeto simples em Python que se conecta a um banco de dados MongoDB rodando em um container Docker. Será explorado operações simples como criar um banco, inserir documentos e realizar consultas usando a biblioteca `pymongo`. O contexto é um aplicativo que contém uma coleção de plantas.

## Pré-requisitos

- Python 3 instalado
- Docker instalado e em execução
- `pip` instalado

## Como rodar

1. **Inicie o MongoDB via Docker**:

```bash
docker run -d \
  --name mongo-auth \
  -e MONGO_INITDB_ROOT_USERNAME=root \
  -e MONGO_INITDB_ROOT_PASSWORD=senha123 \
  -p 27017:27017 \
  -v mongo_dados:/data/db \
  mongo
```

2. **Crie o ambiente virtual e ative**:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Execute o script Python**:

```bash
python main.py
```

## O que o script faz

- Conecta ao MongoDB com autenticação
- Cria uma base de dados chamada `plant_db`
- Cria a coleção `plants`
- Insere documentos de exemplo
- Faz consultas com filtros como `difficulty_level > 2`
- Permite deletar documentos por `_id`

## Dependências

- `pymongo`

Você pode listar as dependências automaticamente com:

```bash
pip freeze > requirements.txt
```
