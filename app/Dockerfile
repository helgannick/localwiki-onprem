# Usando uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copiar o código da aplicação para o container
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instalar mysql-connector-python
RUN pip install mysql-connector-python

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "wiki.py"]
