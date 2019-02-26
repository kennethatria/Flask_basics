class BaseConfig(object):
    'Base config class'
    SECRET_KEY = 'A_random_secret_key'
    DEBUG = True
    TESTING = False
    #SQLALCHEMY_DATABASE_URI="postgresql://localhost/towMyCar"
    
    SQLALCHEMY_DATABASE_URI = \
        '{dialect}+{driver}://{user}:{password}@{host}:{port}/{dbname}'\
        .format(
            dialect='postgresql',
            driver='psycopg2',
            user='kennethatria',#os.environ['RDS_USERNAME'],
            password='',#os.environ['RDS_PASSWORD'],
            host='localhost',#os.environ['RDS_HOSTNAME'],
            port=5432,#os.environ['RDS_PORT'],
            dbname='towMyCar'#os.environ['RDS_DB_NAME']
    )
    
class ProductionConfig(BaseConfig):
    'Production specific config'
    DEBUG = False
    #SECRET_KEY = open('/path/to/secret/file').read()
class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True
class DevelopmentConfig(BaseConfig):
    'Development environment specific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Another_random_secret_key'
    DEVELOPMENT = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

