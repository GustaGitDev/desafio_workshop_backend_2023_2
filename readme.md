# desafio_workshop_backend_2023_2
⚙ workshop fabrica de software 2023.2

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

## Realizando a **busca/consulta** de um nome especifico

- *GET*:
  rota_api/cadastrocliente/CadastroCliente/?nome=busca : Retorna os dados que contém 'busca' em seu NOME