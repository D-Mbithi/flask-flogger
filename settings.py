import os

SECRET_KEY = os.environ['SECRET_KEY']

# DB Conf settings
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_PORT = 5432
DB_NAME = os.environ['DATABASE_NAME']

# DB Connection Config
DB_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask settings
BLOG_NAME = os.environ['BLOG_NAME']
BLOG_POST_IMAGES_PATH = os.environ['BLOG_POST_IMAGES_PATH']
