Criar virtualenv e instalar dependências

(No Windows, usar sempre o CMD, e nas instalações usar ele no modo ADM e não usar o console do VsCode)
Caso não tenha o virtualenv instalado, instalar com:

$ pip install virtualenv
 
Em seguida, criar o ambiente virtual para instalar as dependências do python para o projeto
############Linux############
$ virtualenv venv
$ source venv/bin/activate
 
############Windows##########
$ python -m venv venv
$ venv\Scripts\activate
 
#####Após o processso########
(venv) $ pip install -r requirements.txt
 
Inicializar banco de dados
 
(Para funcionar no windows, geralmente você terá que mudar o 'python3' por 'python' apenas)
 
$ python3 manage.py makemigrations
$ python3 manage.py migrate
 
 
 
Popular banco de dados
Para popular o banco com as informações default, como: nomes dos países, cidades, estados, titulações e tipos de inscrições, nós solicitamos ao sqlite que leia os dados do arquivo db_default.sql e importe para o db.sqlite3, que é o nosso banco de dados.
Se postgres
$ sudo -u postgres psql mydb < 'db.default.sql'
 
Se mysqlite3
$ sqlite3 db.loja < db.default.sql
 
 
 
<h1>Inicalizar servidor de desenvolvimento</h1>
 
(Para funcionar no windows, geralmente você terá que mudar o 'python3' por 'python' apenas)
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
