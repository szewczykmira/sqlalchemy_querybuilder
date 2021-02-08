from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine('sqlite:///database.db')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()
