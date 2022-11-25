class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://space_app:chester06011992@pg/space_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}