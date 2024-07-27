# Curso de FastAPI do ZERO com o 🦖 Dunossauro
FastAPI é um framework Python moderno, projetado para simplicidade, velocidade e eficiência. A combinação de diversas funcionalidades modernas do Python como anotações de tipo e suporte a concorrência, facilitando o desenvolvimento de APIs.

# Aula 01 Configurando o Ambiente de Desenvolvimento
## Configurando o Ambiente de Desenvolvimento

Verificando a instalação do Python.
~~~shell
python --version
~~~

Instalação do pyenv no Windows, recomendo usar o pyenv-windows.
~~~shell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
~~~

Após o pyenv-windows instalado, verificar qual versão do python deseja e instale.
~~~shell
pyenv update
pyenv install 3.12:latest
~~~

Definiar uma versão global do Python.
~~~shell
pyenv global 3.12.x
~~~

Instalação de ferramentas recomendadas.
~~~shell
pip install pipx
~~~

~~~shell
pipx install poetry
~~~

Após o poetry instalado é necessário executar o comando abaixo, feche e reabra o terminal:
~~~shell
pipx ensurepath
~~~

~~~shell
pipx install ignr
~~~

## Criação do Projeto FastAPI e Instalação das Dependências
Entrar no diretório onde criará o projeto.
~~~shell
cd C:\projetos\projetos-GIT\
~~~

Criando o projeto.
~~~shell
poetry new fast_zero_v2
~~~

Entrar no projeto.
~~~shell
cd fast_zero_v2
~~~

Definir qual a versão do Python será utilizada nesse projeto/diretório. O script abaixo criará um arquivo que contém a versão do Python.
~~~shell
pyenv local 3.12.4
~~~

Esse comando criará um arquivo oculto chamado `.python-version` na raiz do projeto.

Configurar o arquivo `pyproject.toml`.
[...]

Crie o ambiente virtual do projeto.
~~~shell
poetry install
~~~

Instalando a biblioteca Python do FastAPI.
~~~shell
poetry add fastapi
~~~

## Primeira Execução de um "Hello, World!"
Criação do app.
~~~shell
echo > fast_zero_v2/app.py
~~~
[melhorar esta criação pelo terminal]


Acessando e codificando no app.
~~~shell
code fast_zero_v2/app.py
~~~
[... codificando ...]

Executar a função pelo terminal em modo interativo para chamar a função.
~~~shell
python -i .\fast_zero_v2\app.py
~~~

Depois execute a função para obter o resultado.
~~~shell
>>> read_root()
~~~

[... codificando ...]

Antes de iniciar a aplicação, habilitar o ambiente virtual, para que o python consiga enxergar as dependências instaladas.
~~~shell
poetry shell
~~~

## Testando o ambiente: iniciar nosso servidor FastAPI para iniciar nossa aplicação
~~~shell
fastapi dev fast_zero_v2/app.py
~~~

## Instalando + ferramentas de desenvolvimento
~~~shell
poetry add --group dev pytest pytest-cov taskipy ruff httpx
~~~

Após a instalação das ferramentas de desenvolvimento, precisamos definir as configurações de cada uma individualmente no arquivo `pyproject.toml`.
[... atentar para os nomes dos projetos que influencia neste arqvuivo ...]


Após arquivo configurado, pode testar os comandos criados para o taskipy:
~~~shell
task lint
~~~

~~~shell
task format
~~~

~~~shell
task lint
~~~

## Introdução ao Pytest: Testando o "Hello, World!"
~~~shell
task test
~~~

Gera um relatório de cobertura de testes em formato HTML. Pode abrir esse arquivo no navegador e entender exatamente quais linhas do código não estão sendo testadas.
~~~shell
coverage html
~~~

### Escrevendo o teste
Criação dos arquivos de teste.
~~~shell
echo > tests/test_app.py
~~~
[...]

~~~shell
task test
~~~

Por não coletar nenhum teste, o pytest ainda retornou um "erro". Para ver a cobertura, precisaremos executar novamente o post_test manualmente:
~~~shell
task post_test
~~~

### Criando nosso repositório no git

[... deu muito ruim nessa parte do git, refazer outro projeto com cuidado]

Criar um arquivo `.gitignore` para não adicionar o ambiente virtual e outros arquivos desnecessários no versionamento de código.
~~~shell
ignr -p python > .gitignore
~~~

Criar um novo repositório no Git local para versionar o código e definir a branch main como padrão.
~~~shell
git init -b main
~~~


Para criar um repositório remoto no GitHub externo caso não exista.
~~~shell
gh repo create
~~~


#### Respostas do gh
- Create a new repository on GitHub from scratch
- fast_zero_sync_v2
- Código das aulas aprendidas no curso do Dunossauro (FASTAPI)
- Public
- N
- N
- y
- GNU General Public License v3.0
- Y
- Y

~~~shell
git remote add origin https://github.com/LuizPerciliano/fast_zero_sync_v2.git
~~~

~~~shell
git pull origin main
~~~

~~~shell
git add .
~~~

~~~shell
git commit -m "Configuração inicial do projeto"
~~~

~~~shell
git push
~~~

[... deu muito ruim nessa parte do git, refazer outro projeto com cuidado]


[🐍 ... VOLTAR DAQUI ...🐍]
# Aula 02 Introdução ao desenvolvimento WEB


[... desenvolvendo e incrementando o projeto ...]


# Aula 03 Estruturando o Projeto e Criando Rotas CRUD
Instalando + ferramentas de desenvolvimento
~~~shell
poetry add "pydantic[email]"
~~~


# Aula 04 Configurando o Banco de Dados e Gerenciando Migrações com Alembic


~~~shell
poetry add sqlalchemy
~~~



~~~shell
poetry add pydantic-settings
~~~


Agora, definiremos o DATABASE_URL no nosso arquivo de ambiente .env. Crie o arquivo na raiz do projeto e adicione a seguinte linha:

`DATABASE_URL="sqlite:///database.db"`

Finalmente, adicione o arquivo de banco de dados, database.db, ao .gitignore para garantir que não seja incluído no controle de versão. Adicionar informações sensíveis ou arquivos binários ao controle de versão é geralmente considerado uma prática ruim.
~~~shell
echo 'database.db' >> .gitignore
~~~


Instalando o Alembic e Criando a Primeira Migração
~~~shell
poetry add alembic
~~~

~~~shell
alembic init migrations
~~~

Com o Alembic devidamente instalado e iniciado, agora é o momento de gerar nossa primeira migração. Mas, antes disso, precisamos garantir que o Alembic consiga acessar nossas configurações e modelos corretamente. Para isso, faremos algumas alterações no arquivo migrations/env.py.
[...]


Para criar a migração, utilizamos o seguinte comando:
~~~shell
alembic revision --autogenerate -m "create users table"
~~~


Vamos acessar o console do sqlite e verificar se isso foi feito. Precisamos chamar sqlite3 nome_do_arquivo.db:
~~~shell
sqlite3 database.db
~~~
[...]


Para aplicar as migrações, usamos o comando upgrade do CLI Alembic. O argumento head indica que queremos aplicar todas as migrações que ainda não foram aplicadas:
~~~shell
alembic upgrade head
~~~
[...]

# Aula 05 Integrando Banco de Dados a API
[...]


# Aula 06 Autenticação e Autorização com JWT
## Gerando tokens JWT
Para gerar tokens JWT, precisamos de duas bibliotecas extras: pyjwt e pwdlib. A primeira será usada para a geração do token, enquanto a segunda será usada para criptografar as senhas dos usuários. Para instalá-las, execute o seguinte comando no terminal:
~~~shell
poetry add pyjwt "pwdlib[argon2]"
~~~

## Utilizando OAuth2PasswordRequestForm
A classe OAuth2PasswordRequestForm é uma classe especial do FastAPI que gera automaticamente um formulário para solicitar o username (email neste caso) e a senha. Este formulário será apresentado automaticamente no Swagger UI e Redoc, facilitando a realização de testes de autenticação.
Para usar os formulários no FastAPI, precisamos instalar o python-multipart:
~~~shell
poetry add python-multipart
~~~

Atualizando o repositório.

# Aula 07 Refatorando a Estrutura do Projeto
Agora, precisamos adicionar estes valores ao nosso arquivo .env.
~~~shell
DATABASE_URL="sqlite:///database.db"
SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

~~~

Atualizando o repositório.
~~~shell
git add .
git commit -m "Refatorando estrutura do projeto: Criado routers para Users e Auth; movido constantes para variáveis de ambiente."
~~~

# Aula 08 Tornando o sistema de autenticação robusto
~~~shell
poetry add --group dev factory-boy
~~~

~~~shell
poetry add --group dev freezegun
~~~


Atualizando o repositório.
~~~shell
git add .
git commit -m "Implementando o refresh do token e testes de autorização"
~~~


# Aula 09 Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI
## Criando a migração da nova tabela
~~~shell
alembic revision --autogenerate -m "create todos table"
~~~

Depois que a migração for criada, precisamos aplicá-la ao nosso banco de dados. Execute o comando alembic upgrade head para aplicar a migração.
~~~shell
alembic upgrade head
~~~



Atualizando o repositório.
~~~shell
git add .
git commit -m "Implementado os endpoints de tarefas"
~~~


# Aula 10 Dockerizando a nossa aplicação e introduzindo o PostgreSQL

## Criando nosso Dockerfile
Para criar um container Docker, escrevemos uma lista de passos de como construir o ambiente para execução da nossa aplicação em um arquivo chamado Dockerfile. Ele define o ambiente de execução, os comandos necessários para preparar o ambiente e o comando a ser executado quando um contêiner é iniciado a partir da imagem.

Uma das coisas interessantes sobre Docker é que existe um Hub de containers prontos onde a comunidade hospeda imagens "prontas", que podemos usar como ponto de partida. Por exemplo, a comunidade de python mantém um grupo de imagens com o ambiente python pronto para uso. Podemos partir dessa imagem com o python já instalado adicionar os passos para que nossa aplicação seja executada.

Aqui está um exemplo de Dockerfile para executar nossa aplicação:
~~~shell
FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app
~~~

## Criando a imagem
Para criar uma imagem Docker a partir do Dockerfile, usamos o comando docker build. O comando a seguir cria uma imagem chamada "fast_zero":
~~~shell
docker build -t "fast_zero" .
~~~

Então verificaremos se a imagem foi criada com sucesso usando o comando:
~~~shell
docker images
~~~

## Executando o container
~~~shell
docker run -it --name fastzeroapp -p 8000:8000 fast_zero:latest
~~~

~~~shell
curl http://localhost:8000
~~~

## Introduzindo o postgreSQL
~~~shell
docker run -d \
    --name app_database \
    -e POSTGRES_USER=app_user \
    -e POSTGRES_DB=app_db \
    -e POSTGRES_PASSWORD=app_password \
    -p 5432:5432 \
    postgres
~~~

No PostgreSQL, o diretório padrão para armazenamento de dados é /var/lib/postgresql/data. Mapeamos esse diretório para um volume (neste caso "pgdata") em nossa máquina host para garantir a persistência dos dados:
~~~shell
docker run -d \
    --name app_database \
    -e POSTGRES_USER=app_user \
    -e POSTGRES_DB=app_db \
    -e POSTGRES_PASSWORD=app_password \
    -v pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
~~~

## Adicionando o suporte ao PostgreSQL na nossa aplicação
~~~shell
poetry add "psycopg[binary]"
~~~

Para ajustar a conexão com o PostgreSQL, modifique seu arquivo .env para incluir a seguinte string de conexão:
~~~shell
DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
~~~

Para que a instalação do psycopg esteja na imagem docker, precisamos fazer um novo build. Para que a nova versão do pyproject.toml seja copiada e os novos pacotes sejam instalados:
~~~shell
docker rm fastzeroapp 
docker build -t "fast_zero" 
docker run -it --name fastzeroapp -p 8000:8000 fast_zero:latest
~~~

~~~shell
docker exec -it fastzeroapp poetry run alembic upgrade head
~~~


## Simplificando nosso fluxo com docker-compose
Criação do compose.yaml
~~~shell
services:
  fastzero_database:
    image: postgres
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: app_user
      POSTGRES_DB: app_db
      POSTGRES_PASSWORD: app_password
    ports:
      - "5432:5432"

  fastzero_app:
    image: fastzero_app
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - fastzero_database
    environment:
      DATABASE_URL: postgresql+psycopg://app_user:app_password@fastzero_database:5432/app_db

volumes:
  pgdata:
~~~

~~~shell
docker-compose up
~~~

## Implementando o Entrypoint
Criamos um script chamado entrypoint.sh que irá preparar nosso ambiente antes de a aplicação iniciar:
~~~shell
#!/bin/sh

# Executa as migrações do banco de dados
poetry run alembic upgrade head

# Inicia a aplicação
poetry run uvicorn --host 0.0.0.0 --port 8000 fast_zero.app:app
~~~


## Adicionando o Entrypoint ao Docker Compose:

Incluímos o entrypoint no nosso serviço no arquivo compose.yaml, garantindo que esteja apontando para o script correto:

compose.yaml
~~~shell
  fastzero_app:
    image: fastzero_app
    entrypoint: ./entrypoint.sh
    build: .
~~~

~~~shell
docker-compose up --build
~~~

~~~shell
docker-compose up -d fastzero_database
~~~

~~~shell
poetry add --group dev testcontainers
~~~





Atualizando o repositório.
~~~shell
git add .
git commit -m "Dockerizando nossa aplicação e inserindo o PostgreSQL"
git push
~~~


# Aula 11 Automatizando os testes com Integração Contínua (CI)
Configurando o workflow de CI
As configurações dos workflows no GitHub Actions são definidas em um arquivo YAML localizado em um path especificado pelo github no repositório .github/workflows/. Dentro desse diretório podemos criar quantos workflows quisermos. Iniciaremos nossa configuração com um único arquivo que chamaremos de pipeline.yaml:
~~~shell
name: Pipeline
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
~~~


Para isso, devemos criar um step para cada uma dessas ações no nosso job test. Desta:
`.github/workflows/pipeline.yaml`
~~~shell
    steps:
      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instalar o poetry
        run: pipx install poetry

      - name: Instalar dependências
        run: poetry install

      - name: Executar testes
        run: poetry run task test
~~~

Atualizando o repositório.
~~~shell
git add .
git commit -m "Adicionando o checkout ao pipeline"
git push
~~~

## Configuração de variáveis de ambiente no Actions
[...]

~~~shell
gh secret set -f .env
~~~

`.github/workflows/pipeline.yaml`
~~~shell
jobs:
  test:
    runs-on: ubuntu-latest

    env:
      DATABASE_URL: ${{ secrets.DATABASE_URL }}
      SECRET_KEY: ${{ secrets.SECRET_KEY }}
      ALGORITHM: ${{ secrets.ALGORITHM }}
      ACCESS_TOKEN_EXPIRE_MINUTES: ${{ secrets.ACCESS_TOKEN_EXPIRE_MINUTES }}
~~~


Atualizando o repositório.
~~~shell
git add .
git commit -m "Adicionando as variáveis de ambiente para o CI"
git push
~~~

# Aula 12 Fazendo deploy no Fly.io
[...]

~~~shell
git add .
git commit -m "Adicionando arquivos gerados pelo Fly"
git push
~~~

# Aula 13 Despedida e próximos passos
[... ainda vai ter esta aula ...]


# Projeto final

---

XXX
~~~shell

~~~



~~~python
s = "Sintaxe do Pythong"
print s
~~~

    

