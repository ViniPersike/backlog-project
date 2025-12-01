# backlog-project
Para fazer a conexão do banco de dados você deve criar um arquivo .env na raíz do projeto.
Isso é o que você deve escrever no seu .env para conectar o pgadmin:
```
  DB_NAME=database_name
  DB_USER=your_username
  DB_PASSWORD=your_password
  DB_HOST=localhost
```
Substituindo os valores pelo nome do seu banco, seu usuário e sua senha, o localhost é o padrão do pgadmin.
Para fazer o backup do banco para realizar testes basta copiar o conteúdo do arquivo, abrir o query tool no pgadmin, colar e rodar.
## Observação: caso você não use o backup de dados, para acessar todas as funcionalidades deve-se registrar o seguinte usuário
```
Usuário: admin
Senha: 123
```
___

# backlog-project
This is my first project. It's a backlog for games

In order to make it work properly with your own database you have to create a .env file and set up your connection
This is what you should write on you .env file if you're working with postgres and pgadmin:
```
  DB_NAME=database_name
  DB_USER=your_username
  DB_PASSWORD=your_password
  DB_HOST=localhost
```
