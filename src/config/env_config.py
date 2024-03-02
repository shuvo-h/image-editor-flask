from os import getenv

envs= {
    'APP_SECRET_KEY': getenv('APP_SECRET_KEY','default_secret_key'),
    'DB_NAME': getenv('DB_NAME','default_db_name'),

    # database config 
    'DB_USERNAME': getenv('DB_USERNAME',None),
    'DB_PASSWORD': getenv('DB_PASSWORD',None),
    'DB_HOST': getenv('DB_HOST',None),
    'DB_NAME': getenv('DB_NAME',None),


    # jwt envs 
    'ACCESS_TOKEN_SECRET': getenv('ACCESS_TOKEN_SECRET',None),
    'REFRESH_TOKEN_SECRET': getenv('REFRESH_TOKEN_SECRET',None),
}