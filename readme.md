# desafio_workshop_backend_2023_2
⚙ workshop fabrica de software 2023.2

Este projeto tem como objetivo realizar o cadastro de clientes e armazenar os dados cadastrados em um banco de dados, além de implementar um método de filtragem e busca para atender a especificações requeridas. Isso inclui a possibilidade de buscar por nomes específicos, e-mails, números de telefone e até mesmo por gênero.

## Como executar:

1. clonar repositorio:
> via ssh
```bash
git clone git@github.com:GustaGitDev/desafio_workshop_backend_2023_2.git
```       

> via https
```bash
git clone https://github.com/GustaGitDev/desafio_workshop_backend_2023_2.git
```

2. entrar no diretorio do projeto e criar e ativar ambiente virtual:
> ambiente linux
```bash
cd desafio_workshop_backend_2023_2
python3 -m venv venv
source venv/bin/activate
```
> ambiente windows
```ps1
python -m venv venv
.\venv\Scripts\activate.ps1
```

3. fazer download das dependencias do projeto:
```bash
pip install -r requirements.txt
```

4. caso queira um banco de dados vazio, execute:
```bash
python manage.py makemigrations
python manage.py migrate
```
- para usar um banco de dados populado:
```bash
python create_db_from_backup.py
```

5. rodar o servidor:
```bash
python manage.py runserver
```

## Rotas:

**api/**
- *GET*: 
  rota_api/cadastrocliente/CadastroCliente : Retorna todos os dados da API
  rota_api/cadastrocliente/CadastroCliente/id : Retorna um dado específico da API pelo ID

- *POST*: Envio de novos dados para a API:
    > body requisicao:
    ```json
      {
      "nome": "",
      "sobrenome": "",
      "email": "",
      "senha": "",
      "nascimento": date,
      "numero": "",
      "genero": choice,
      }
    ```

**api/{id}/**
- *PUT*: atualiza dados de uma instancia a partir do id
    > body requisicao:
    ```json
      {
      "nome": "Arthur",
      "sobrenome": "Gustavo",
      "email": "gutolights0@gmail.com",
      "senha": "senha123",
      "nascimento": 03/12/2005,
      "numero": "83988221922",
      "genero": Masculino, **O genero irá ficar visivel após ser definido na rota Genero**
      }
    ```

- *DELETE*: exclui uma instancia a partir do id *rota_api/cadastrocliente/CadastroCliente/id*

 ## Acessando a rota de Genero

 - *GET*: 
  rota_api/cadastrocliente/Genero : Retorna todos os dados da API
  rota_api/cadastrocliente/Genero/id : Retorna um dado específico da API pelo ID

 - *POST*: Envio de novos dados para a API:
    > body requisicao:
    ```json
      {
      "Genero": "",
      }
    ```

**api/{id}/**
- *PUT*: atualiza dados de uma instancia a partir do id
    > body requisicao:
    ```json
      {
      "genero": Masculino,
      }
    ```
  *DELETE*: Deletando um dado específico da API: *rota_api/produto/produto/id*

## Realizando a **busca/consulta** de alguma especificação

  Ao utilizar o servidor local, será possivel visualizar uma opção chamada "FILTERS", onde deve ser digitado a especificação que se procura. EX: gustavo, teste@teste.com, 021981827567, masculino.

  Rota: http://API-ROTA/cadastrocliente/CadastroCliente/?search=NOME
  Rota: http://API-ROTA/cadastrocliente/CadastroCliente/?search=EMAIL
  Rota: http://API-ROTA/cadastrocliente/CadastroCliente/?search=NUMERO
  Rota: http://API-ROTA/cadastrocliente/CadastroCliente/?search=GENERO

## Banco de dados para armazenamento de dados

  O banco de dados utilizado foi o PostgreSQL, com a senha padrão "unipe", ip padrão "127.0.0.1", porta padrão "5432" e usuario padrão "postgres".

  É necessario a instalação do postgres em sua maquina para o funcionamento correto da API.