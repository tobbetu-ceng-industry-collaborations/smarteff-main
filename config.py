# Statement for enabling the development environment
DEBUG = True

# Define the database_uri - we are working on
SQLALCHEMY_DATABASE_URI = 'sqlite:///smarteff.db'

# Set modification track false - adds significant overhead
SQLALCHEMY_TRACK_MODIFICATIONS = False