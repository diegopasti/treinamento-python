### 1. Conhecendo o Python
### 1.1. Executando o interpretador
````bash
python
````

### 1.2. Executando um arquivo

Podemos instruir o interpretador a executar um arquivo especifico. Fazemos isso passando o caminho do arquivo como parametro do comando que inicializa o interpretador.
````bash
python manage.py
````

Além de informar um arquivo podemos enviar outros parametros que o arquivo pode utilizar para executar o script de forma parametrizada.
````bash
python manage.py createsuperuser
````

Falar sobre os arquivos .pyc
```python
x = 'hello, python world!'
print(x.split(' '))
```