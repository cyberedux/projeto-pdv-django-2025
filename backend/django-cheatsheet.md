# Django Cheatsheet 

### Antes de tudo...
Crie uma pasta para seu projeto e abra com o Visual Studio Code (VSCode).

### Instalação (todo sistema)
```
pip install django
```

### Instalação pipenv
De dentro da pasta do seu projeto rode:
```
pipenv install django
```
isso irá instalar o Django em um ambiente virtual e criar dois novos arquivos:
```
pasta_projeto\
    Pipfile
    Pipfile.lock
```

Após isso selecione o interpretador Python do ambiente virtual com as teclas `Ctrl`+`Shift`+`p` e digite `Select Interpreter` ou `Selecionar Interpretador` caso seu VSCode esteja em Português, por fim, **selecione a opção que possui o nome da pasta do projeto**. 

### Criando um novo projeto
Utilizando o terminal do VSCode de dentro da pasta criada para o projeto rode o comando:
```
django-admin startproject nome_do_seu_projeto .
```
Isso irá criar uma pasta com o nome do seu projeto e um arquivo `manage.py`:
```
pasta_projeto\
    manage.py
    nome_do_seu_projeto\
        ...
```
