import os

class Config():

    SECRET_KEY= os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):

    DEBUG=True
    MYSQL_HOST=os.getenv('MYSQL_HOST')
    MYSQL_USER=os.getenv('MYSQL_USER')
    MYSQL_PASSWORD=os.getenv('MYSQL_PASS')
    MYSQL_DB=os.getenv('MYSQL_DB')

class ProductionConfig(Config):

    DEBUG=False
    MYSQL_HOST=os.getenv('MYSQL_HOST')
    MYSQL_USER=os.getenv('MYSQL_USER')
    MYSQL_PASSWORD=os.getenv('MYSQL_PASS')
    MYSQL_DB=os.getenv('MYSQL_DB')

config = {
    "Development": DevelopmentConfig,
    "Production": ProductionConfig
}